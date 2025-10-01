# Claude Usage Guide

This document outlines the workflow for reviewing and getting feedback on deliverables for this project using Claude.

## Use Case

After initial development with Gemini, use Claude to review the final output. It is ideal for checking code quality, style, and getting feedback on potential issues.

## How to Use

To start Claude for a review session, type the following command in your terminal:

```bash
claude
```

---

### Project Overview

This directory, `HLTrigger`, is a package within the CMS (Compact Muon Solenoid) Software (CMSSW) framework. Its primary purpose is to define and implement the High-Level Trigger (HLT) system for the CMS experiment.

The HLT is a software-based trigger system that performs a fast reconstruction and selection of interesting physics events from the vast amount of data produced by the detector, reducing the data rate from millions of events per second to a few thousand that can be stored for offline analysis.

---

### Detailed Directory Descriptions

*   **`Configuration/`**: This is the control center for the HLT. It contains Python files (`.py`) that define the trigger paths, sequences, and final menus. Key files like `HLT_GRun_cff.py` assemble these paths into the complete menu for a specific era (e.g., proton-proton runs). The `scripts/` subdirectory contains tools for managing and deploying these configurations.

*   **`HLTcore/`**: Provides the essential building blocks for all HLT modules. It defines base classes like `HLTFilter`, which is the parent class for most C++ modules that make a selection decision in the HLT. It ensures a common interface and functionality.

*   **`HLTfilters/`**: Contains generic, physics-agnostic `EDFilter` modules. A prime example is `HLTHighLevel`, which can be configured to accept an event if it was accepted by another specified trigger path. This is useful for creating cross-triggers or triggers for monitoring streams.

*   **`<PhysicsObject>/plugins/` (e.g., `btau/`, `Egamma/`, `JetMET/`, `Muon/`)**: These directories house the specialized C++ code that does the physics-based filtering. They contain two main types of CMSSW modules:
    *   **`EDProducer`**: Takes data products as input and *produces* new data products. For example, a producer might take tracker hits and produce a collection of reconstructed tracks.
    *   **`EDFilter`**: Takes data products as input and decides whether the event should be kept or discarded based on some criteria. For example, `HLTEgammaEtFilter` inspects a collection of electrons and returns `true` only if at least one has transverse energy (Et) above a configured threshold.

*   **`btau/`**: Contains triggers for b-jets and tau leptons. These often rely on identifying particles with a finite lifetime, using information about displaced tracks and secondary vertices.

*   **`Egamma/`**: Focuses on electron and photon triggers. Filters here typically cut on transverse energy (Et), isolation (the amount of energy in a cone around the candidate), and variables related to the shape of the electromagnetic shower in the calorimeter.

*   **`JetMET/`**: Implements triggers for jets (collimated sprays of particles) and Missing Transverse Energy (MET). Common selections are based on the number of jets, their energy, and global event properties like HT (the scalar sum of all jet Et).

*   **`Muon/`**: Contains all muon-related trigger logic. Filters select muons based on their momentum (pT), isolation, and quality criteria related to matching track segments across different parts of the muon spectrometer (L1, L2, L3).

---

### Beginner's Tutorial: Creating a New Trigger

This tutorial will guide you through creating a simple, new single-muon trigger path named `HLT_MyNewMuon_v1`. The goal is to select events containing at least one high-quality muon with a transverse momentum (pT) greater than 20 GeV.

For simplicity and realism, we will reuse existing, well-tested C++ modules and focus on the Python configuration.

**Step 1: Understand the Building Blocks**

A trigger path is a sequence of modules. It starts with a Level-1 (L1) seed, which is a hardware-level decision. This is followed by a series of HLT modules that perform more detailed reconstruction and filtering.

Our path will look like this:
1.  **L1 Seed**: An L1 decision that found a muon candidate (e.g., `L1_SingleMu22`).
2.  **HLT Reconstruction**: Run reconstruction algorithms to build high-level muon objects (we will use the standard sequence).
3.  **HLT Filter**: Run a filter module to select events with a muon pT > 20 GeV.

**Step 2: Define the HLT Path in Python**

Open an appropriate configuration file, for instance, `HLTrigger/Configuration/python/HLT_GRun_cff.py`.

1.  **Find an existing path to copy**: Search for a similar single-muon trigger, like `HLT_IsoMu24_v`. This gives you a template for the reconstruction sequence.

2.  **Define your filter**: We can reuse the `HLTMuonL3SimplePreFilter`. We need to create a specific instance of it for our 20 GeV pT cut. Add the following Python code alongside other filter definitions:

    ```python
    hltL3fL1sSingleMu22L1f0L2f10L3Filtered20 = cms.EDFilter("HLTMuonL3SimplePreFilter",
        # ... (copy parameters from a similar filter like hltL3fL1sSingleMu22L1f0L2f10L3Filtered24)
        MinPt = cms.double(20.0), # Set our desired pT cut
        # ... (other parameters)
    )
    ```

3.  **Define your path**: Now, assemble the L1 seed, the standard muon reconstruction sequence, and your new filter into an `HLTPath`. Add this to the file:

    ```python
    HLT_MyNewMuon_v1 = cms.Path( 
        cms.Sequence( HLTBeginSequence, hltL1sSingleMu22, ... , HLTEndSequence ) # Copy the full sequence from a similar path
        + cms.Sequence( hltL3fL1sSingleMu22L1f0L2f10L3Filtered20 ) # Add your filter at the end
    )
    ```
    *Note: You must copy the full reconstruction sequence from an existing muon path to ensure the muon objects are correctly built before your filter runs.* 

**Step 3: Add the New Path to the Menu and a Stream**

1.  **Add to Final Paths**: At the end of the file, add your new path to the list of all paths:
    ```python
    HLTriggerFinalPath = cms.Path(
        # ... (many other paths)
        HLT_MyNewMuon_v1
    )
    ```

2.  **Assign to a Dataset**: Assign your path to a primary dataset. In the `HLTrigger_Datasets_GRun_cff.py` file, add your path to the appropriate dataset, for example `SingleMuon`:
    ```python
    cms.PSet(
        HLT_IsoMu24_v1 = cms.vstring( '' ),
        HLT_MyNewMuon_v1 = cms.vstring( '' ), # Add your path here
        # ...
    ),
    ```

**Step 4: Compile and Test**

1.  **Compile**: Since we only changed Python files, no C++ compilation is needed. If you had added a new C++ module, you would run:
    ```bash
    scram b -j8
    ```

2.  **Test**: You can now test your new configuration using `cmsRun` and a test configuration file. This will run the HLT on a sample of events and you can check if your path runs and fires as expected.

    ```bash
    cmsRun my_test_cfg.py
    ```
This completes the basic process of adding a new trigger path. Real-world trigger development requires careful validation of efficiency and performance, but these steps provide the fundamental workflow.

# Claude 사용 가이드

이 문서는 Claude를 사용하여 이 프로젝트의 결과물을 검토하고 피드백을 받는 워크플로우를 설명합니다.

## 사용 사례

Gemini로 초기 개발을 마친 후 Claude를 사용하여 최종 결과물을 검토하세요. 코드 품질, 스타일을 확인하고 잠재적인 문제에 대한 피드백을 받는 데 이상적입니다.

## 사용 방법

검토 세션을 위해 Claude를 시작하려면 터미널에 다음 명령을 입력하세요.

```bash
claude
```

---

### 프로젝트 개요

이 디렉토리 `HLTrigger`는 CMS(Compact Muon Solenoid) 소프트웨어(CMSSW) 프레임워크 내의 패키지입니다. 주요 목적은 CMS 실험을 위한 HLT(High-Level Trigger) 시스템을 정의하고 구현하는 것입니다.

HLT는 소프트웨어 기반 트리거 시스템으로, 검출기에서 생성되는 방대한 양의 데이터에서 흥미로운 물리적 이벤트를 신속하게 재구성하고 선택하여 데이터 속도를 초당 수백만 이벤트에서 오프라인 분석을 위해 저장할 수 있는 수천 개로 줄입니다.

---

### 자세한 디렉토리 설명

*   **`Configuration/`**: HLT의 제어 센터입니다. 트리거 경로, 시퀀스 및 최종 메뉴를 정의하는 Python 파일(`.py`)을 포함합니다. `HLT_GRun_cff.py`와 같은 주요 파일은 이러한 경로를 특정 시대(예: 양성자-양성자 실행)의 전체 메뉴로 조합합니다. `scripts/` 하위 디렉토리에는 이러한 구성을 관리하고 배포하기 위한 도구가 포함되어 있습니다.

*   **`HLTcore/`**: 모든 HLT 모듈의 필수 구성 요소를 제공합니다. HLT에서 선택 결정을 내리는 대부분의 C++ 모듈의 부모 클래스인 `HLTFilter`와 같은 기본 클래스를 정의합니다. 공통 인터페이스와 기능을 보장합니다.

*   **`HLTfilters/`**: 물리 현상에 구애받지 않는 일반적인 `EDFilter` 모듈을 포함합니다. 대표적인 예는 `HLTHighLevel`이며, 다른 지정된 트리거 경로에 의해 수락된 경우 이벤트를 수락하도록 구성할 수 있습니다. 이는 교차 트리거 또는 모니터링 스트림용 트리거를 만드는 데 유용합니다.

*   **`<PhysicsObject>/plugins/` (예: `btau/`, `Egamma/`, `JetMET/`, `Muon/`)**: 이 디렉토리에는 물리 기반 필터링을 수행하는 특수 C++ 코드가 있습니다. 여기에는 두 가지 주요 유형의 CMSSW 모듈이 포함됩니다.
    *   **`EDProducer`**: 데이터 제품을 입력으로 받아 새로운 데이터 제품을 *생산*합니다. 예를 들어, 생산자는 트래커 히트를 가져와 재구성된 트랙 모음을 생성할 수 있습니다.
    *   **`EDFilter`**: 데이터 제품을 입력으로 받아 일부 기준에 따라 이벤트를 유지할지 또는 폐기할지 결정합니다. 예를 들어, `HLTEgammaEtFilter`는 전자 모음을 검사하고 구성된 임계값 이상의 횡단 에너지(Et)를 가진 전자가 하나 이상 있는 경우에만 `true`를 반환합니다.

*   **`btau/`**: b-제트 및 타우 렙톤용 트리거를 포함합니다. 이들은 종종 변위된 트랙 및 2차 정점에 대한 정보를 사용하여 유한한 수명을 가진 입자를 식별하는 데 의존합니다.

*   **`Egamma/`**: 전자 및 광자 트리거에 중점을 둡니다. 여기의 필터는 일반적으로 횡단 에너지(Et), 격리(후보 주변 원뿔의 에너지 양) 및 열량계의 전자기 샤워 모양과 관련된 변수를 기준으로 자릅니다.

*   **`JetMET/`**: 제트(입자의 시준된 스프레이) 및 누락된 횡단 에너지(MET)에 대한 트리거를 구현합니다. 일반적인 선택은 제트 수, 에너지 및 HT(모든 제트 Et의 스칼라 합)와 같은 전역 이벤트 속성을 기반으로 합니다.

*   **`Muon/`**: 모든 뮤온 관련 트리거 로직을 포함합니다. 필터는 운동량(pT), 격리 및 뮤온 분광계의 다른 부분(L1, L2, L3)에서 트랙 세그먼트를 일치시키는 것과 관련된 품질 기준에 따라 뮤온을 선택합니다.

---

### 초보자 튜토리얼: 새 트리거 만들기

이 튜토리얼에서는 `HLT_MyNewMuon_v1`이라는 간단하고 새로운 단일 뮤온 트리거 경로를 만드는 과정을 안내합니다. 목표는 횡단 운동량(pT)이 20GeV보다 큰 고품질 뮤온이 하나 이상 포함된 이벤트를 선택하는 것입니다.

단순성과 현실성을 위해 기존의 잘 테스트된 C++ 모듈을 재사용하고 Python 구성에 중점을 둘 것입니다.

**1단계: 구성 요소 이해**

트리거 경로는 모듈의 시퀀스입니다. 하드웨어 수준 결정인 레벨-1(L1) 시드로 시작합니다. 그 다음에는 보다 자세한 재구성 및 필터링을 수행하는 일련의 HLT 모듈이 이어집니다.

경로는 다음과 같습니다.
1.  **L1 시드**: 뮤온 후보를 찾은 L1 결정(예: `L1_SingleMu22`).
2.  **HLT 재구성**: 재구성 알고리즘을 실행하여 고급 뮤온 객체를 빌드합니다(표준 시퀀스 사용).
3.  **HLT 필터**: 필터 모듈을 실행하여 뮤온 pT > 20GeV인 이벤트를 선택합니다.

**2단계: Python에서 HLT 경로 정의**

`HLTrigger/Configuration/python/HLT_GRun_cff.py`와 같은 적절한 구성 파일을 엽니다.

1.  **복사할 기존 경로 찾기**: `HLT_IsoMu24_v`와 같은 유사한 단일 뮤온 트리거를 검색합니다. 이는 재구성 시퀀스에 대한 템플릿을 제공합니다.

2.  **필터 정의**: `HLTMuonL3SimplePreFilter`를 재사용할 수 있습니다. 20GeV pT 컷에 대한 특정 인스턴스를 만들어야 합니다. 다른 필터 정의와 함께 다음 Python 코드를 추가합니다.

    ```python
    hltL3fL1sSingleMu22L1f0L2f10L3Filtered20 = cms.EDFilter("HLTMuonL3SimplePreFilter",
        # ... (hltL3fL1sSingleMu22L1f0L2f10L3Filtered24와 같은 유사한 필터에서 매개변수 복사)
        MinPt = cms.double(20.0), # 원하는 pT 컷 설정
        # ... (기타 매개변수)
    )
    ```

3.  **경로 정의**: 이제 L1 시드, 표준 뮤온 재구성 시퀀스 및 새 필터를 `HLTPath`로 조합합니다. 파일에 다음을 추가합니다.

    ```python
    HLT_MyNewMuon_v1 = cms.Path( 
        cms.Sequence( HLTBeginSequence, hltL1sSingleMu22, ... , HLTEndSequence ) # 유사한 경로에서 전체 시퀀스 복사
        + cms.Sequence( hltL3fL1sSingleMu22L1f0L2f10L3Filtered20 ) # 끝에 필터 추가
    )
    ```
    *참고: 필터가 실행되기 전에 뮤온 객체가 올바르게 빌드되도록 하려면 기존 뮤온 경로에서 전체 재구성 시퀀스를 복사해야 합니다.* 

**3단계: 메뉴 및 스트림에 새 경로 추가**

1.  **최종 경로에 추가**: 파일 끝에서 모든 경로 목록에 새 경로를 추가합니다.
    ```python
    HLTriggerFinalPath = cms.Path(
        # ... (다른 많은 경로)
        HLT_MyNewMuon_v1
    )
    ```

2.  **데이터 세트에 할당**: 경로를 기본 데이터 세트에 할당합니다. `HLTrigger_Datasets_GRun_cff.py` 파일에서 예를 들어 `SingleMuon`과 같은 적절한 데이터 세트에 경로를 추가합니다.
    ```python
    cms.PSet(
        HLT_IsoMu24_v1 = cms.vstring( '' ),
        HLT_MyNewMuon_v1 = cms.vstring( '' ), # 여기에 경로 추가
        # ...
    ),
    ```

**4단계: 컴파일 및 테스트**

1.  **컴파일**: Python 파일만 변경했으므로 C++ 컴파일은 필요하지 않습니다. 새 C++ 모듈을 추가한 경우 다음을 실행합니다.
    ```bash
    scram b -j8
    ```

2.  **테스트**: 이제 테스트 구성 파일을 사용하여 새 구성을 테스트할 수 있습니다. 이렇게 하면 이벤트 샘플에서 HLT가 실행되고 경로가 예상대로 실행되고 발생하는지 확인할 수 있습니다.

    ```bash
    cmsRun my_test_cfg.py
    ```
이것으로 새 트리거 경로를 추가하는 기본 프로세스가 완료됩니다. 실제 트리거 개발에는 효율성과 성능에 대한 신중한 검증이 필요하지만 이러한 단계는 기본적인 워크플로우를 제공합니다.

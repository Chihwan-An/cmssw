# Phase-II HLT Validation — condor 실행 안내

tamsa 클러스터(SNU)에서 Phase-II HLT validation을 입력 ROOT 파일당 condor job
하나씩으로 돌리기 위한 스크립트 모음입니다.

```
입력 .root ──(job 1개씩)──▶ DQMIO/*_DQM.root ──(harvest job 1개)──▶ DQM_V0001_...root
```

---

## 1. 파일 구성

| 파일 | 역할 |
|---|---|
| `../doPhaseIIValidation.py` | driver. jds/jobs.list 생성 + `condor_submit` |
| `runValSource.sh` | source job 실행체. 입력 1개 → DQMIO 1개 |
| `runValClient.sh` | harvest job 실행체. DQMIO 전부 → 최종 DQM 1개 |
| `jobcommon.sh` | 두 job이 공유하는 설정 (컨테이너 재진입, cmsenv, SITECONF, scratch) |
| `../../../../test.sh` | 진입점. 여기만 고쳐서 쓰는 걸 전제로 합니다 |
| `epr_snu/tools/fetchSample.sh` | 샘플 다운로드 (재개 가능, 터미널 분리) |

---

## 2. 새 샘플을 돌릴 때 — `src/test.sh`

보통은 이 세 줄만 바꾸면 됩니다.

```bash
SAMPLE_TAG=260922                                              # 라벨 (범례에 쓰임)
INPUTS=(
    "/gv0/Users/achihwan/phase2/260922/RelValZpTT_1500_14_D121_PU"
)
OUTDIR=/gv0/Users/achihwan/phase2/260922/hltval
```

`INPUTS`는 **디렉터리 / glob / 파일 경로** 아무거나 받습니다. 여러 개를 넣으면
디렉터리별로 묶여서 각각 별도 샘플로 처리됩니다.

> **glob에 따옴표를 치지 마세요.** 디렉터리를 따옴표로 감싸는 건 괜찮습니다
> (driver가 직접 확장합니다). glob을 따옴표로 감싸면 `*.root`가 문자열
> 그대로 전달됩니다.

---

## 3. detector 버전이 D121이 아니면 — **반드시 같이 바꿔야 합니다**

`runPhaseIIValSource_cfg.py`의 기본값은 **D121 전용**입니다.

| 옵션 | 기본값 |
|---|---|
| `geometry` | `ExtendedRun4D121` |
| `era` | `Phase2C22I13M9` |
| `globalTag` | `auto:phase2_realistic_T35` |

이 셋은 서로 맞아야 하고, 샘플과도 맞아야 합니다. 안 맞으면
`ModuleNotFoundError` 나 GlobalTag 에러가 납니다.

### 올바른 조합 찾는 법

릴리스 안의 workflow 표에 그대로 들어 있습니다.

```bash
grep -A5 "'Run4D121'" \
  $CMSSW_RELEASE_BASE/src/Configuration/PyReleaseValidation/python/upgradeWorkflowComponents.py
```

```python
'Run4D121' : {
    'Geom' : 'ExtendedRun4D121',
    'GT'   : 'auto:phase2_realistic_T35',
    'Era'  : 'Phase2C22I13M9',
}
```

샘플의 detector 버전은 보통 디렉터리 이름에 있습니다
(`RelValZpTT_1500_14_**D121**_PU`). 확실히 하려면 입력 파일의 provenance를
보세요:

```bash
edmProvDump <입력.root> | grep -o '[0-9]\{3\}X_mcRun4_realistic[A-Za-z0-9_]*' | sort -u
```

### 바꾸는 방법

`test.sh`의 driver 호출에 cfg 옵션을 덧붙이는 자리는 없으므로, 값을 바꾸려면
`runPhaseIIValSource_cfg.py`의 `options.register(...)` 기본값을 고치거나
`runValSource.sh`의 `cmsRun` 호출에 인자를 추가하세요.

```bash
cmsRun ... "geometry=ExtendedRun4D110" "era=Phase2C17I13M9" "globalTag=auto:phase2_realistic_T33"
```

> **주의:** CMSSW_20_1_0_pre1에서 Phase-2 이름 체계가 바뀌었습니다.
> `2026Dxx` → `Run4Dxx`. 예전 워크플로에 있던 `GeometryExtended2026D98Reco_cff`,
> `auto:phase2_realistic_T25`는 **릴리스에서 사라졌습니다**
> (`deprecatedDets` / `deprecatedSubdets` 목록 참조).

---

## 4. 사이트 의존 설정 — 다른 사람이 쓸 때 바꿔야 하는 것

### 4-1. SITECONF 우회 경로 (하드코딩되어 있음)

`jobcommon.sh`에 achihwan 계정 경로가 박혀 있습니다.

```bash
local siteconf=${HLTVAL_SITECONF:-/data6/Users/achihwan/tauwiki/epr_snu/siteconf/local}
```

다른 계정에서 쓰려면 환경변수로 덮거나, 자기 트리를 만드세요.

```bash
export HLTVAL_SITECONF=/data6/Users/<you>/siteconf/local
```

트리 만드는 법:

```bash
SC=/data6/Users/<you>/siteconf
mkdir -p "$SC/local/JobConfig"
cp /cvmfs/cms.cern.ch/SITECONF/local/JobConfig/site-local-config.xml "$SC/local/JobConfig/"
ln -sfn /cvmfs/cms.cern.ch/SITECONF/local/PhEDEx "$SC/local/PhEDEx"
ln -sfn /cvmfs/cms.cern.ch/SITECONF/T1_US_FNAL  "$SC/T1_US_FNAL"
```

**왜 필요한가:** 일부 워커 노드의 `/etc/cvmfs/CMS_SITECONF/`
(`/cvmfs/cms.cern.ch/SITECONF/local`이 가리키는 실제 경로)에 `T1_US_FNAL`이
없습니다. `site-local-config.xml`의 `<data-access>`가 참조하는 상대경로
`../T1_US_FNAL/storage.json`이 해석되지 않아 PoolSource가 죽습니다.
tamsa2에는 있고 워커에는 없는 노드가 있습니다.

**이건 임시방편입니다.** 근본 해결은 관리자가 워커 노드의
`/etc/cvmfs/CMS_SITECONF/`를 tamsa2와 동일하게 맞추는 것입니다.

### 4-2. CPU 아키텍처 requirement

```bash
--requirements '(Microarch =?= "x86_64-v3") || (Microarch =?= "x86_64-v4")'   # 기본값
```

CMSSW_20_1_0_pre1의 CORAL external에 x86-64-v2 빌드가 없어서 **v2 노드에서는
`illegal instruction`으로 죽습니다.** 풀 구성은 v3 301대 / v4 273대 / v2 4대라
실질적인 손해는 없습니다.

> **tamsa2 자체가 v2(Ivy Bridge)입니다.** 그래서 로그인 노드에서 `cmsRun`을
> 직접 돌릴 수 없고, harvest까지 condor로 보내야 합니다. 릴리스가 바뀌어
> v2 빌드가 생기면 이 requirement를 빼도 됩니다.

---

## 5. 샘플 받기 — `epr_snu/tools/fetchSample.sh`

데이터셋을 로컬 디스크로 내려받습니다. **이미 받은 파일은 크기를 대조해
건너뛰므로 몇 번을 다시 돌려도 안전합니다.**

### 먼저 grid proxy (필수)

```bash
voms-proxy-init -voms cms -valid 192:00
```

다운로드에 걸릴 시간보다 넉넉하게 잡으세요. proxy가 1시간 미만이면 스크립트가
시작을 거부합니다 — 중간에 끊기는 게 더 나쁘기 때문입니다.

### 데이터셋 이름 확인

```bash
tools/fetchSample.sh --dataset '/RelValZpTT_1500_14/*Run4D121*/GEN-SIM-RECO' --list
```

패턴이 정확히 1개로 좁혀지지 않으면 받기를 거부합니다.

### 받기 — 터미널을 꺼도 계속됩니다

```bash
tools/fetchSample.sh \
    --dataset '/RelValZpTT_1500_14/<정확한이름>/GEN-SIM-RECO' \
    --outdir  /gv0/Users/achihwan/phase2/260922/RelValZpTT_1500_14_D121_PU \
    --jobs 4 --detach
```

`--detach`가 `setsid`로 세션과 분리해 실행하므로 ssh를 끊어도 계속 받습니다.
로그 경로를 출력해 주고, 진행 상황은 이렇게 봅니다.

```bash
tail -f <outdir>/fetch_<날짜>.log      # 진행
grep -c '^\[ok  \]' <outdir>/fetch_*.log   # 완료 수
pkill -u $USER -f 'fetchSample.sh --dataset'  # 중단
```

### 동작 방식

- `.part` 임시 파일로 받고 **크기가 맞을 때만** 제자리로 옮깁니다 → 중단된
  전송이 완료된 것처럼 보이는 일이 없습니다
- 파일당 3회까지 재시도 (20초, 40초 간격)
- `xrdcp --cksum adler32:source`로 전송 중 체크섬 검증
- 끝나면 전체를 다시 대조해 빠진 것을 보고합니다. 다시 돌리면 그것만 이어받습니다
- `--dry-run`으로 받을 목록만 미리 볼 수 있습니다

### 다 받은 뒤

`test.sh`의 `INPUTS`는 디렉터리를 가리키므로 **수정할 것 없이** 그대로 다시
돌리면 됩니다. 늘어난 파일 수만큼 job이 생깁니다.

```bash
bash test.sh
```

> 기존 `<OUTDIR>/<샘플명>/DQMIO/`에 예전 결과가 남아 있으면 harvest가 그것까지
> 합칩니다. 새로 돌릴 때는 `OUTDIR`를 바꾸거나 `DQMIO/`를 비우세요.

---

## 6. 실행 순서

```bash
cd $CMSSW_BASE/src
cmsenv
scram b -j 16          # 최초 1회 (플러그인 없으면 job이 전부 실패합니다)

bash test.sh           # source job N개 제출
condor_q               # 완료 대기

python3 Validation/HLTrigger/test/doPhaseIIValidation.py \
    --mode harvest \
    --inputfiles "<INPUTS와 동일>" \
    --sampletag "<SAMPLE_TAG와 동일>" \
    --outdir "<OUTDIR와 동일>"
```

harvest는 `<OUTDIR>/<샘플명>/DQMIO/`에 있는 파일을 전부 긁어가므로, source job이
**다 끝난 뒤에** 돌려야 합니다. 일부만 끝난 상태로 돌리면 그만큼만 합쳐집니다.

### 결과물

```
<OUTDIR>/<샘플명>/
├── DQM_V0001_R000000001__HLT__Validation__<샘플명>.root   ← 최종
├── DQMIO/                                                  ← 입력 파일당 하나
└── condor/
    ├── <샘플명>.jds, jobs.list, <샘플명>_harvest.jds
    └── log/*.out, *.err, *.log
```

---

## 7. driver 옵션

```
--mode {local,condor,harvest}   local = 이 셸에서 순차 실행 (tamsa2에선 불가, §4-2)
--inputfiles ...                로컬 파일 / glob / 디렉터리
--inputdbsnames ...             DBS 데이터셋 이름 (condor 모드에선 건너뜁니다)
--sampletag TAG                 sampleLabel 로 전달
--outdir DIR                    출력 루트
--maxevents N                   job당 이벤트 수 (기본 -1 = 전부)
--cpus N                        RequestCpus   (기본 1)
--memory MB                     RequestMemory (기본 4000)
--requirements EXPR             condor requirements
--no-submit                     jds만 만들고 제출은 안 함
```

`--maxevents`로 짧게 돌려 파이프라인을 먼저 검증하는 걸 권합니다.

---

## 8. 트러블슈팅

| 증상 | 원인 | 조치 |
|---|---|---|
| `ModuleNotFoundError: ...GeometryExtended2026D98Reco_cff` | 릴리스에 없는 옛 geometry 이름 | §3 |
| `ValueError: ... phase2_realistic_T25` | 릴리스에 없는 GlobalTag | §3 |
| `illegal instruction` (스택에 `coral::`) | v2 CPU에서 실행됨 | §4-2. tamsa2에서 직접 돌린 건 아닌지 확인 |
| `Unable to construct any file locator` | 워커의 SITECONF 불완전 | §4-1 |
| `Fatal Exception ... plugin ... not found` | `scram b` 미실행 | §5 |
| `expected exactly one ROOT file in ...` | cmsRun이 출력을 안 냈거나 여러 개 냄 | `condor/log/*.err` 확인 |
| job이 오래 idle | cvmfs 콜드 캐시 | 첫 job만 느립니다 (7분 → 이후 1분 이내) |
| `HLT_AK8PFJet500 could not be found` 경고 | Phase-2 메뉴에 없는 경로 | **무해.** 해당 히스토그램만 비어 있습니다 |

로그는 항상 `<OUTDIR>/<샘플명>/condor/log/`에 있고, `stream_output`이 켜져
있어 job이 도는 중에도 실시간으로 볼 수 있습니다.

---

## 9. 참고 — 알아두면 헷갈리지 않는 것

- **PU200 Phase-2 RECO는 이벤트당 약 150 MB입니다.** 7.5 GB 파일에 이벤트가
  50개뿐입니다. job이 몇 초 만에 끝나도 정상입니다. 이벤트 수 확인:
  `edmFileUtil -f <파일>`
- **VarParsing은 `maxEvents`를 주면 출력 파일명에 `_numEvent<N>`을 붙입니다.**
  job 스크립트가 이름을 고정하지 않고 생성된 ROOT 파일을 찾는 이유입니다.
- **MessageLogger의 `reportEvery`가 1000입니다.** 이벤트가 그보다 적으면
  "Begin processing the 1st record" 한 줄만 찍힙니다. 처리가 안 된 게 아닙니다.

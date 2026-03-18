# Simulation Tutorials

서울대학교 계산재료 및 데이터과학 실습 강의 전담을 위해 정리한 Python 실습 자료 저장소입니다.  
2024년 가을학기 강의 자료를 기준으로 구성했으며, 강의자는 정석현(Seokhyun Choung)입니다.

이 저장소는 계산재료과학 실습을 따라가며 다음 흐름을 학습하도록 구성되어 있습니다.

- Python 기초
- ASE/GPAW 기반 DFT 실습
- 분자동역학(MD)
- 회귀와 feature engineering
- MACE/Open Catalyst Project 기반 machine learning potential(MLP)
- CatBench 및 간단한 benchmark workflow

## Repository Layout

```text
.
├── notebooks/                  # 실습 순서에 맞춘 메인 노트북
├── class_materials/            # 수업용 PDF 자료
├── data/                       # 실습 데이터셋
├── src/simulation_tutorials/   # 노트북에서 재사용하는 utility code
├── ads_site_search.py          # 기존 import 경로를 위한 compatibility wrapper
└── README.md
```

## Notebook Roadmap

| Order | Notebook | Topic |
| --- | --- | --- |
| 00 | `notebooks/00_intro_to_python.ipynb` | Python 기초 문법과 실습 환경 소개 |
| 01 | `notebooks/01_dft_setup_and_bulk.ipynb` | GPAW 설치, ASE 기본 구조, bulk 계산 |
| 02 | `notebooks/02_dft_surface.ipynb` | 표면 slab 생성과 시각화 |
| 03 | `notebooks/03_dft_adsorption.ipynb` | 흡착 구조 생성과 adsorption workflow |
| 04 | `notebooks/04_dft_adsorption_applications.ipynb` | 흡착 예제 확장 및 응용 |
| 05 | `notebooks/05_md_setup_and_simulation.ipynb` | MD 설정, trajectory 저장, GIF 시각화 |
| 06 | `notebooks/06_md_displacement_analysis.ipynb` | MD trajectory 해석과 displacement 분석 |
| 07 | `notebooks/07_ml_regression_and_feature_engineering.ipynb` | 회귀 모델, descriptor, feature engineering |
| 08 | `notebooks/08_mlp_intro_and_setup.ipynb` | MLP 설치와 기본 사용 흐름 |
| 09 | `notebooks/09_mlp_adsorption_workflows.ipynb` | MLP 기반 표면/흡착 계산 |
| 10 | `notebooks/10_mlp_benchmarking.ipynb` | Catalysis-Hub 계열 benchmark workflow |
| 11 | `notebooks/11_catbench.ipynb` | CatBench 예제와 응용 |

## Appendix Notebooks

| Notebook | Topic |
| --- | --- |
| `notebooks/appendix_advanced_dft_optimization.ipynb` | 추가 DFT 최적화 알고리즘 실습 |
| `notebooks/appendix_mace_calculator_setup.ipynb` | MACE calculator 로딩 및 예제 |
| `notebooks/appendix_open_catalyst_calculator_setup.ipynb` | Open Catalyst Project calculator 설정 |

## Utilities

반복되던 helper 함수는 `src/simulation_tutorials/`로 분리했습니다.

- `visualization.py`: 구조 렌더링, slab 반복 시각화, trajectory GIF 생성
- `optimization.py`: 구조 relaxation과 energy 계산 helper
- `surface_sites.py`: 표면 site 탐색 helper
- `progress.py`: 간단한 text progress bar

노트북 내부에는 기존 호출 방식을 최대한 유지하는 얇은 wrapper만 남겨 두었습니다.

## Class Materials

`class_materials/` 폴더에는 수업 시간에 사용한 PDF 자료가 들어 있습니다.  
노트북과 함께 보면 실습 흐름을 더 빠르게 따라갈 수 있습니다.

## Data

- `data/CO2RR_data.csv`: 회귀/feature engineering 실습에서 사용하는 데이터셋

## How To Use

### 1. Local Jupyter

저장소를 클론한 뒤 루트 디렉터리에서 Jupyter를 실행하면 됩니다.

```bash
git clone https://github.com/s-choung/Simulation_tutorials.git
cd Simulation_tutorials
jupyter lab
```

실습 노트북은 루트 또는 `notebooks/` 기준으로 `src/`를 자동 탐색하도록 정리되어 있습니다.

### 2. Google Colab

각 노트북 상단의 `Open in Colab` 배지를 통해 바로 열 수 있습니다.  
일부 노트북은 `src/simulation_tutorials/` 유틸 모듈이 필요할 때 저장소를 자동으로 clone 하도록 bootstrap 셀을 포함합니다.

## Notes

- 많은 노트북이 Colab 환경을 전제로 `apt-get` 또는 `pip install` 셀을 포함합니다.
- ASE, GPAW, pymatgen, MACE, Open Catalyst Project 관련 패키지는 노트북 주제에 따라 설치 범위가 다릅니다.
- 본 저장소는 교육용 실습 자료 중심이며, production-ready package 구성을 목표로 하지는 않습니다.

## Credits

- Course: 서울대학교 계산재료 및 데이터과학 실습 강의 전담
- Term: 2024 Fall
- Instructor: 정석현 (Seokhyun Choung)

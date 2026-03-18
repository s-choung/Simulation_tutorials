# Repository Refresh Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reorganize the teaching repository into a clearer course-oriented layout, extract reusable utility code, and rewrite the README for public reuse.

**Architecture:** Keep notebooks as the primary learning surface, but move reusable helpers into `src/simulation_tutorials/` and convert notebook-specific utility cells into thin wrappers. Group materials into `notebooks/`, `data/`, and `class_materials/` so the repository reads like a course package instead of a flat upload dump.

**Tech Stack:** Python, Jupyter notebooks, ASE, GPAW, MACE, pymatgen, Markdown

---

### Task 1: Define the canonical repository layout

**Files:**
- Create: `docs/plans/2026-03-18-repository-refresh.md`
- Modify: `README.md`
- Modify: repository root file layout

**Step 1: Normalize top-level directories**

Create or reuse:
- `notebooks/`
- `data/`
- `class_materials/`
- `src/simulation_tutorials/`

**Step 2: Rename notebooks into a course sequence**

Use a zero-padded naming scheme:
- `00_intro_to_python.ipynb`
- `01_dft_setup_and_bulk.ipynb`
- `02_dft_surface.ipynb`
- `03_dft_adsorption.ipynb`
- `04_dft_adsorption_applications.ipynb`
- `05_md_setup_and_simulation.ipynb`
- `06_md_displacement_analysis.ipynb`
- `07_ml_regression_and_feature_engineering.ipynb`
- `08_mlp_intro_and_setup.ipynb`
- `09_mlp_adsorption_workflows.ipynb`
- `10_mlp_benchmarking.ipynb`
- `11_catbench.ipynb`

**Step 3: Move supplemental notebooks into appendix-style names**

Use:
- `appendix_advanced_dft_optimization.ipynb`
- `appendix_mace_calculator_setup.ipynb`
- `appendix_open_catalyst_calculator_setup.ipynb`

### Task 2: Extract reusable utilities

**Files:**
- Create: `src/simulation_tutorials/__init__.py`
- Create: `src/simulation_tutorials/visualization.py`
- Create: `src/simulation_tutorials/optimization.py`
- Create: `src/simulation_tutorials/progress.py`
- Create: `src/simulation_tutorials/surface_sites.py`
- Modify: `ads_site_search.py`

**Step 1: Move repeated visualization logic into `visualization.py`**

Support:
- structure rendering
- repeated-slab rendering
- frame export for GIF generation
- trajectory-to-GIF conversion

**Step 2: Move repeated relaxation logic into `optimization.py`**

Support:
- optional calculator assignment
- optional atom copy
- optional cell relaxation
- optional return of relaxed atoms

**Step 3: Move the simple progress helper into `progress.py`**

Provide a reusable text progress bar for notebook loops.

**Step 4: Consolidate surface-site search helpers**

Move `ads_site_search.py` logic into `surface_sites.py`, and keep a compatibility wrapper at the original import path.

### Task 3: Update notebooks to use the utilities

**Files:**
- Modify: affected notebooks in `notebooks/`

**Step 1: Update Colab badge paths**

Point every badge to the new `notebooks/` location.

**Step 2: Insert a lightweight import bootstrap**

Allow local use from a cloned repository and Colab use by cloning the repository when `src/` is missing.

**Step 3: Replace large utility cells with thin wrappers**

Keep notebook call sites stable where possible by replacing bulky helper definitions with:
- imports from `simulation_tutorials`
- narrow compatibility wrappers for notebook-specific defaults

**Step 4: Update any moved data paths**

Change raw GitHub links or local paths to the new `data/` layout.

### Task 4: Rewrite the README

**Files:**
- Modify: `README.md`

**Step 1: Add course context**

Document:
- course identity
- institution
- semester
- instructor
- repository purpose

**Step 2: Add a curriculum map**

Summarize each notebook and appendix in reading order.

**Step 3: Add usage guidance**

Explain:
- local clone workflow
- Colab workflow
- dependency expectations
- repository layout

### Task 5: Verify the refactor

**Files:**
- Verify: renamed notebooks and moved assets
- Verify: notebook links and imports
- Verify: README paths

**Step 1: Check for stale references**

Search for old notebook names, old data paths, and old class material paths.

**Step 2: Check the duplicate `08` notebook issue**

Ensure only one canonical lesson-08 notebook remains in the final layout.

**Step 3: Review git status**

Confirm the repository reflects the intended moves, new modules, notebook edits, and README rewrite.

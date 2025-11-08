# STAT 159 HW03 – Elise Yi Gao
# Targets:
#   make env   – Create or update conda environment
#   make html  – Build local MyST HTML site
#   make clean – Remove build, figures, and audio outputs

# ---------- Config ----------
FIG_DIR   := figures
AUDIO_DIR := audio
BUILD_DIR := _build
ENV_FILE  := environment.yml

CONDA ?= conda

.PHONY: env html clean

# --------- Targets ----------
## env: create or update the environment (does NOT activate it)
env:
	@echo ">>> Creating or updating environment from $(ENV_FILE)…"
	@$(CONDA) env create -f $(ENV_FILE) || $(CONDA) env update -f $(ENV_FILE)
	@echo ">>> Done. Activate it manually with: conda activate <env_name>"

## html: build the local HTML for the MyST site
html:
	@echo ">>> Building MyST site (local HTML)…"
	myst build --html
	@echo ">>> Built site is in '$(BUILD_DIR)/html'"

## clean: remove build artifacts and generated media, keep folders/.gitkeep
clean:
	@echo ">>> Cleaning build and generated outputs…"
	@rm -rf $(BUILD_DIR)
	@mkdir -p $(FIG_DIR) $(AUDIO_DIR)
	@find $(FIG_DIR) -type f ! -name '.gitkeep' -delete
	@find $(AUDIO_DIR) -type f ! -name '.gitkeep' -delete
	@echo ">>> Clean complete."
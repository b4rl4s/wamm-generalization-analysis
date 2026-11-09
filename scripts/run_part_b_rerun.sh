#!/usr/bin/env bash
# Parametre adı hatası düzeltildikten sonra Bölüm B/C'nin yeniden çalıştırılması.
set -e
cd "$(dirname "$0")/.."
PY=.venv/bin/python
$PY scripts/09a_check_obfuscation.py > logs/09a_check.log 2>&1
for m in ds_aug_v2_random_s42 ds_aug_v2_family_0.8_s42 ds_base_random_s42 ds_base_family_0.8_s42; do
  $PY scripts/09_obfuscation.py "$m" > "logs/09_obf_$m.log" 2>&1
  $PY scripts/10_shap.py "$m" > "logs/10_shap_$m.log" 2>&1
done
$PY scripts/12_figures_bc.py > logs/12_figures.log 2>&1
echo BITTI

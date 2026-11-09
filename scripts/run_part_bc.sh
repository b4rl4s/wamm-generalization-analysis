#!/usr/bin/env bash
# Bölüm B ve C: eğitim bitince gizleme değerlendirmesi, SHAP ve ablasyonu sırayla çalıştırır.
set -e
cd "$(dirname "$0")/.."
PY=.venv/bin/python
MODELS="ds_aug_v2_random_s42 ds_aug_v2_family_0.8_s42 ds_base_random_s42 ds_base_family_0.8_s42"
for m in $MODELS; do
  while [ ! -f "models/$m/result.json" ]; do sleep 30; done
done
while pgrep -f "09_obfuscation.py ds_aug_v2_random_s42" >/dev/null; do sleep 30; done
for m in $MODELS; do
  [ -f "results/obfuscation/$m.json" ] || $PY scripts/09_obfuscation.py "$m" > "logs/09_obf_$m.log" 2>&1
done
for m in $MODELS; do
  [ -f "results/shap/$m.json" ] || $PY scripts/10_shap.py "$m" > "logs/10_shap_$m.log" 2>&1
done
for d in ds_aug_v2 ds_base; do for s in random family_0.8; do for f in hand tfidf; do
  $PY scripts/11_ablation.py $d $s $f >> logs/11_ablation.log 2>&1
done; done; done
echo "BITTI"

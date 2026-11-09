"""Bölüm B, B2: dönüşümlerin anlam koruma kontrolü ve sınıf bazında uygulanabilirlik oranları.

Her değişen satırda: tamamen çözülmüş + normalize edilmiş (dönüşüm geri alınmış) metin, orijinalle aynı olmalı.
Kullanım: python scripts/09a_check_obfuscation.py
"""
import sys,time,re; sys.path.insert(0,"src")
import numpy as np, pandas as pd
from wamm_data import load
from obfuscate import transform, TRANSFORMS, applicable
from families import decode

PARAM = re.compile(r"(?:^|[?&;\s])([A-Za-z0-9_\-\[\]%.]+)=")

def param_names(raw):
    """Ham istekteki parametre/cookie adları: dönüşüm bunları değiştirmemeli."""
    return PARAM.findall(raw)

def canon(s):
    s = decode(s, rounds=40).lower()
    s = s.replace("cb-listener.net","oastify.com").replace("/**/"," ").replace('""',"").replace("\t"," ")
    s = re.sub(r"(?<![.])\.(?=[/\\]\.\.)[/\\]", "", s)
    s = re.sub(r"(<\s*[a-z][a-z0-9]*)/", r"\1 ", s)
    s = re.sub(r"/(?=(on[a-z]+|src|href|style)\s*=)", " ", s)
    return s.replace("+"," ")

for name in ["ds_base","ds_aug_v2"]:
    df=load(name); lab=df.label.astype(str); rng=np.random.default_rng(0)
    rows=[]; bad=[]; t0=time.time()
    for c in sorted(lab.unique()):
        if "ormal" in c: continue
        idx=rng.choice(np.flatnonzero((lab==c).values),300,replace=False)
        r={"class":c}
        for t in TRANSFORMS:
            if not applicable(t,c): r[t]="-"; continue
            ch=0
            for i in idx:
                a=df.request.iloc[i]; b=transform(a,t,c,seed=int(i))
                if a!=b:
                    ch+=1
                    if t!="encoding_norm" and canon(a)!=canon(b): bad.append((t,c,i))
                    if t!="encoding_norm" and param_names(a)!=param_names(b): bad.append((t+"[param]",c,i))
                    if t=="encoding_norm" and decode(a,40)!=decode(b,40): bad.append((t,c,i))
            r[t]=round(100*ch/len(idx))
        rows.append(r)
    import collections
    print(name, f"{time.time()-t0:.0f}s", "anlam kontrolünden geçmeyen:", len(bad), collections.Counter(t for t,_,_ in bad))
    print(pd.DataFrame(rows).set_index("class").to_string())
    for t,c,i in bad[:5]:
        a=canon(df.request.iloc[i]); b=canon(transform(df.request.iloc[i],t,c,seed=int(i)))
        k=next(j for j in range(min(len(a),len(b))) if a[j]!=b[j]) if a!=b else 0
        print("  BAD",t,c,repr(a[max(0,k-60):k+60]),"\n      ",repr(b[max(0,k-60):k+60]))

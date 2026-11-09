# Payload aileleri: ds_aug_v2

- Satır: 704,665; benzersiz iskelet: 237,824
- Rastgele bölmede iskeleti eğitimde birebir bulunan test satırı: **68.4%**

## Eşik bazında özet

| Eşik | Aile | En büyük aile (satır, %) | Tekil aile | Karışık etiketli ailelerdeki satır | Rastgele bölmede ailesi eğitimde olan test % |
|---|---:|---:|---:|---:|---:|
| 0.5 | 2,104 | 313,205 (44.5%) | 1,555 | 696,761 | 99.8 |
| 0.6 | 3,555 | 303,640 (43.1%) | 2,711 | 691,618 | 99.6 |
| 0.7 | 7,236 | 298,689 (42.4%) | 5,665 | 666,489 | 99.1 |
| 0.8 | 33,570 | 298,689 (42.4%) | 26,984 | 502,280 | 95.9 |
| 0.9 | 125,998 | 298,689 (42.4%) | 104,999 | 368,022 | 84.2 |

## Sınıf bazında (eşik 0.5)

| Sınıf | Satır | Aile | En büyük aile payı |
|---|---:|---:|---:|
| 000 - Normal | 493,515 | 1,165 | 0.605 |
| 126 - Path Traversal | 17,718 | 166 | 0.891 |
| 1336 - SSTI | 1,897 | 23 | 0.974 |
| 248 - Command Injection | 2,597 | 51 | 0.942 |
| 66 - SQL Injection | 146,086 | 620 | 0.853 |
| 79 - Cross-Site Scripting | 2,894 | 21 | 0.978 |
| 88 - OS Command Injection | 36,114 | 149 | 0.724 |
| 918 - SSRF | 2,645 | 41 | 0.774 |
| 94 - Code Injection | 1,199 | 81 | 0.828 |

## Sınıf bazında (eşik 0.6)

| Sınıf | Satır | Aile | En büyük aile payı |
|---|---:|---:|---:|
| 000 - Normal | 493,515 | 1,919 | 0.605 |
| 126 - Path Traversal | 17,718 | 233 | 0.867 |
| 1336 - SSTI | 1,897 | 30 | 0.759 |
| 248 - Command Injection | 2,597 | 54 | 0.802 |
| 66 - SQL Injection | 146,086 | 1,213 | 0.832 |
| 79 - Cross-Site Scripting | 2,894 | 35 | 0.869 |
| 88 - OS Command Injection | 36,114 | 241 | 0.584 |
| 918 - SSRF | 2,645 | 55 | 0.656 |
| 94 - Code Injection | 1,199 | 90 | 0.547 |

## Sınıf bazında (eşik 0.7)

| Sınıf | Satır | Aile | En büyük aile payı |
|---|---:|---:|---:|
| 000 - Normal | 493,515 | 3,432 | 0.605 |
| 126 - Path Traversal | 17,718 | 387 | 0.756 |
| 1336 - SSTI | 1,897 | 42 | 0.427 |
| 248 - Command Injection | 2,597 | 60 | 0.373 |
| 66 - SQL Injection | 146,086 | 3,068 | 0.701 |
| 79 - Cross-Site Scripting | 2,894 | 49 | 0.431 |
| 88 - OS Command Injection | 36,114 | 475 | 0.501 |
| 918 - SSRF | 2,645 | 86 | 0.43 |
| 94 - Code Injection | 1,199 | 100 | 0.452 |

## Sınıf bazında (eşik 0.8)

| Sınıf | Satır | Aile | En büyük aile payı |
|---|---:|---:|---:|
| 000 - Normal | 493,515 | 15,839 | 0.605 |
| 126 - Path Traversal | 17,718 | 1,114 | 0.206 |
| 1336 - SSTI | 1,897 | 77 | 0.375 |
| 248 - Command Injection | 2,597 | 80 | 0.369 |
| 66 - SQL Injection | 146,086 | 15,760 | 0.344 |
| 79 - Cross-Site Scripting | 2,894 | 70 | 0.401 |
| 88 - OS Command Injection | 36,114 | 1,503 | 0.495 |
| 918 - SSRF | 2,645 | 155 | 0.428 |
| 94 - Code Injection | 1,199 | 120 | 0.177 |

## Sınıf bazında (eşik 0.9)

| Sınıf | Satır | Aile | En büyük aile payı |
|---|---:|---:|---:|
| 000 - Normal | 493,515 | 52,476 | 0.605 |
| 126 - Path Traversal | 17,718 | 3,387 | 0.039 |
| 1336 - SSTI | 1,897 | 220 | 0.366 |
| 248 - Command Injection | 2,597 | 122 | 0.24 |
| 66 - SQL Injection | 146,086 | 67,062 | 0.15 |
| 79 - Cross-Site Scripting | 2,894 | 167 | 0.395 |
| 88 - OS Command Injection | 36,114 | 3,861 | 0.365 |
| 918 - SSRF | 2,645 | 310 | 0.173 |
| 94 - Code Injection | 1,199 | 275 | 0.108 |

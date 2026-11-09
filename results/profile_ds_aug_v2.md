# Veri profili: ds_aug_v2

- Satır: **704,665**
- Boş istek: 0

## Sınıf dağılımı

| Sınıf | Satır | % |
|---|---:|---:|
| 000 - Normal | 493,515 | 70.04 |
| 66 - SQL Injection | 146,086 | 20.73 |
| 88 - OS Command Injection | 36,114 | 5.12 |
| 126 - Path Traversal | 17,718 | 2.51 |
| 79 - Cross-Site Scripting | 2,894 | 0.41 |
| 918 - SSRF | 2,645 | 0.38 |
| 248 - Command Injection | 2,597 | 0.37 |
| 1336 - SSTI | 1,897 | 0.27 |
| 94 - Code Injection | 1,199 | 0.17 |

## Birebir tekrar — ham istek

- Benzersiz: 312,256 / 704,665 → tekrar oranı **55.69%**
- Farklı etiketlerle görünen içerik: 99 anahtar, 3,757 satır

| Sınıf | Satır | Benzersiz | Tekrar % |
|---|---:|---:|---:|
| 000 - Normal | 493,515 | 132,171 | 73.22 |
| 126 - Path Traversal | 17,718 | 12,096 | 31.73 |
| 1336 - SSTI | 1,897 | 884 | 53.40 |
| 248 - Command Injection | 2,597 | 1,677 | 35.43 |
| 66 - SQL Injection | 146,086 | 133,651 | 8.51 |
| 79 - Cross-Site Scripting | 2,894 | 1,231 | 57.46 |
| 88 - OS Command Injection | 36,114 | 27,849 | 22.89 |
| 918 - SSRF | 2,645 | 2,065 | 21.93 |
| 94 - Code Injection | 1,199 | 751 | 37.36 |

## Birebir tekrar — method + payload (header'lar hariç)

- Benzersiz: 173,612 / 704,665 → tekrar oranı **75.36%**
- Farklı etiketlerle görünen içerik: 599 anahtar, 375,448 satır

| Sınıf | Satır | Benzersiz | Tekrar % |
|---|---:|---:|---:|
| 000 - Normal | 493,515 | 65,006 | 86.83 |
| 126 - Path Traversal | 17,718 | 11,224 | 36.65 |
| 1336 - SSTI | 1,897 | 193 | 89.83 |
| 248 - Command Injection | 2,597 | 281 | 89.18 |
| 66 - SQL Injection | 146,086 | 93,012 | 36.33 |
| 79 - Cross-Site Scripting | 2,894 | 343 | 88.15 |
| 88 - OS Command Injection | 36,114 | 3,579 | 90.09 |
| 918 - SSRF | 2,645 | 509 | 80.76 |
| 94 - Code Injection | 1,199 | 538 | 55.13 |

## Uzunluk (karakter)

| Sınıf | Ortalama | Medyan | Maks |
|---|---:|---:|---:|
| 000 - Normal | 313.4 | 181.0 | 440244.0 |
| 126 - Path Traversal | 656.7 | 355.0 | 20307.0 |
| 1336 - SSTI | 12210.5 | 11147.0 | 19543.0 |
| 248 - Command Injection | 10034.5 | 8186.0 | 19791.0 |
| 66 - SQL Injection | 929.1 | 531.0 | 12045.0 |
| 79 - Cross-Site Scripting | 12549.2 | 9317.0 | 24881.0 |
| 88 - OS Command Injection | 12531.1 | 12765.0 | 32776.0 |
| 918 - SSRF | 8063.4 | 7683.0 | 23220.0 |
| 94 - Code Injection | 5381.8 | 1818.0 | 26040.0 |

## Yapısal sinyaller (olası kısayollar)

| Sınıf | Body oranı | Ort. header | En sık method | En sık host |
|---|---:|---:|---|---|
| 000 - Normal | 0.015 | 2.58 | GET (481,746) | test-site.com (476,612) |
| 66 - SQL Injection | 0.021 | 4.26 | GET (136,314) | test-site.com (128,355) |
| 88 - OS Command Injection | 0.029 | 15.4 | GET (25,844) | studio.youtube.com (17,330) |
| 126 - Path Traversal | 0.037 | 3.93 | GET (16,755) | test-site.com (15,962) |
| 79 - Cross-Site Scripting | 0.01 | 15.43 | GET (2,071) | accounts.google.com (2,135) |
| 918 - SSRF | 0.029 | 15.43 | GET (1,509) | accounts.google.com (1,078) |
| 248 - Command Injection | 0.024 | 15.81 | POST (1,369) | accounts.google.com (1,669) |
| 1336 - SSTI | 0.0 | 15.53 | GET (1,221) | accounts.google.com (1,233) |
| 94 - Code Injection | 0.144 | 14.97 | GET (688) | www.yahoo.com (241) |

### User-Agent örtüşmesi

- Saldırı satırlarında benzersiz UA: 1,506; normal satırlarda: 1,256; ortak: 4
- UA'sı normal trafikte de görülen saldırı satırı oranı: **97.23%**

| Sınıf | En sık UA | Satır |
|---|---|---:|
| 000 - Normal | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 100,514 |
| 126 - Path Traversal | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 15,379 |
| 1336 - SSTI | `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0` | 1,872 |
| 248 - Command Injection | `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0` | 2,379 |
| 66 - SQL Injection | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 123,625 |
| 79 - Cross-Site Scripting | `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0` | 2,757 |
| 88 - OS Command Injection | `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0` | 33,324 |
| 918 - SSRF | `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0` | 2,388 |
| 94 - Code Injection | `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0` | 720 |

# Veri profili: ds_base

- Satır: **859,293**
- Boş istek: 0

## Sınıf dağılımı

| Sınıf | Satır | % |
|---|---:|---:|
| Normal | 476,674 | 55.47 |
| SQL Injection | 249,100 | 28.99 |
| Fake the Source of Data | 55,983 | 6.52 |
| HTTP Response Splitting | 19,668 | 2.29 |
| Path Traversal | 17,762 | 2.07 |
| Code Injection | 15,805 | 1.84 |
| Protocol Manipulation | 9,153 | 1.07 |
| OS Command Injection | 6,150 | 0.72 |
| HTTP Verb Tampering | 4,055 | 0.47 |
| Scanning for Vulnerable Software | 2,414 | 0.28 |
| Input Data Manipulation | 1,387 | 0.16 |
| Dictionary-based Password Attack | 1,142 | 0.13 |

## Birebir tekrar — ham istek

- Benzersiz: 471,918 / 859,293 → tekrar oranı **45.08%**
- Farklı etiketlerle görünen içerik: 559 anahtar, 4,680 satır

| Sınıf | Satır | Benzersiz | Tekrar % |
|---|---:|---:|---:|
| Code Injection | 15,805 | 15,210 | 3.76 |
| Dictionary-based Password Attack | 1,142 | 1,118 | 2.10 |
| Fake the Source of Data | 55,983 | 46,693 | 16.59 |
| HTTP Response Splitting | 19,668 | 19,498 | 0.86 |
| HTTP Verb Tampering | 4,055 | 4,055 | 0.00 |
| Input Data Manipulation | 1,387 | 1,381 | 0.43 |
| Normal | 476,674 | 119,070 | 75.02 |
| OS Command Injection | 6,150 | 6,150 | 0.00 |
| Path Traversal | 17,762 | 12,797 | 27.95 |
| Protocol Manipulation | 9,153 | 7,645 | 16.48 |
| SQL Injection | 249,100 | 236,498 | 5.06 |
| Scanning for Vulnerable Software | 2,414 | 2,373 | 1.70 |

## Birebir tekrar — method + payload (header'lar hariç)

- Benzersiz: 343,372 / 859,293 → tekrar oranı **60.04%**
- Farklı etiketlerle görünen içerik: 738 anahtar, 410,218 satır

| Sınıf | Satır | Benzersiz | Tekrar % |
|---|---:|---:|---:|
| Code Injection | 15,805 | 11,738 | 25.73 |
| Dictionary-based Password Attack | 1,142 | 1,118 | 2.10 |
| Fake the Source of Data | 55,983 | 43,953 | 21.49 |
| HTTP Response Splitting | 19,668 | 18,749 | 4.67 |
| HTTP Verb Tampering | 4,055 | 3,935 | 2.96 |
| Input Data Manipulation | 1,387 | 1,127 | 18.75 |
| Normal | 476,674 | 55,695 | 88.32 |
| OS Command Injection | 6,150 | 6,010 | 2.28 |
| Path Traversal | 17,762 | 11,652 | 34.40 |
| Protocol Manipulation | 9,153 | 4,656 | 49.13 |
| SQL Injection | 249,100 | 183,797 | 26.22 |
| Scanning for Vulnerable Software | 2,414 | 2,372 | 1.74 |

## Uzunluk (karakter)

| Sınıf | Ortalama | Medyan | Maks |
|---|---:|---:|---:|
| Code Injection | 591.4 | 583.0 | 1084.0 |
| Dictionary-based Password Attack | 591.8 | 593.0 | 951.0 |
| Fake the Source of Data | 351.5 | 371.0 | 909.0 |
| HTTP Response Splitting | 545.3 | 610.0 | 1009.0 |
| HTTP Verb Tampering | 421.3 | 412.0 | 964.0 |
| Input Data Manipulation | 633.2 | 647.0 | 1136.0 |
| Normal | 237.6 | 175.0 | 1157.0 |
| OS Command Injection | 689.2 | 678.0 | 1008.0 |
| Path Traversal | 385.7 | 341.0 | 854.0 |
| Protocol Manipulation | 419.8 | 423.0 | 940.0 |
| SQL Injection | 500.0 | 512.0 | 1044.0 |
| Scanning for Vulnerable Software | 172.7 | 169.0 | 247.0 |

## Yapısal sinyaller (olası kısayollar)

| Sınıf | Body oranı | Ort. header | En sık method | En sık host |
|---|---:|---:|---|---|
| Normal | 0.006 | 2.21 | GET (470,625) | test-site.com (476,612) |
| SQL Injection | 0.037 | 2.84 | GET (238,889) | test-site.com (249,095) |
| Fake the Source of Data | 0.054 | 2.9 | GET (51,583) | test-site.com (55,926) |
| HTTP Response Splitting | 0.053 | 2.87 | GET (18,568) | test-site.com (19,666) |
| Path Traversal | 0.049 | 2.88 | GET (16,889) | test-site.com (17,732) |
| Code Injection | 0.123 | 2.94 | GET (13,856) | test-site.com (15,803) |
| Protocol Manipulation | 0.137 | 2.87 | GET (7,377) | test-site.com (7,732) |
| OS Command Injection | 0.584 | 3.61 | POST (3,589) | test-site.com (6,148) |
| HTTP Verb Tampering | 0.03 | 3.02 | TRACK (886) | test-site.com (4,055) |
| Scanning for Vulnerable Software | 0.0 | 2.0 | GET (1,327) | 249.network5-175-62-15.static.network5.net (2,414) |
| Input Data Manipulation | 1.0 | 4.04 | POST (1,387) | test-site.com (1,387) |
| Dictionary-based Password Attack | 1.0 | 3.89 | POST (1,133) | test-site.com (1,142) |

### User-Agent örtüşmesi

- Saldırı satırlarında benzersiz UA: 807; normal satırlarda: 1,255; ortak: 61
- UA'sı normal trafikte de görülen saldırı satırı oranı: **98.03%**

| Sınıf | En sık UA | Satır |
|---|---|---:|
| Code Injection | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 15,174 |
| Dictionary-based Password Attack | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 984 |
| Fake the Source of Data | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 51,985 |
| HTTP Response Splitting | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 19,068 |
| HTTP Verb Tampering | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 3,472 |
| Input Data Manipulation | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 1,302 |
| Normal | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 100,514 |
| OS Command Injection | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 5,781 |
| Path Traversal | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 16,728 |
| Protocol Manipulation | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 7,409 |
| SQL Injection | `Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0` | 238,323 |
| Scanning for Vulnerable Software | `Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)` | 2,414 |

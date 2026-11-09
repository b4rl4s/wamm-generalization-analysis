# Gösterge varlığı — ds_base

Değerler: satırların yüzdesi (sınıf başına en fazla 3000 satır).

| Sınıf                            |    n |   sql |   xss |   cmd |   ssti |   path |   ssrf |   code |   kendi göstergesi |   hiç gösterge yok |
|:---------------------------------|-----:|------:|------:|------:|-------:|-------:|-------:|-------:|-------------------:|-------------------:|
| Code Injection                   | 3000 |  39.9 |  10.7 |   3.4 |   44.2 |    0   |      0 |   93.3 |               93.3 |                0.4 |
| Dictionary-based Password Attack | 1142 |  12.3 |   0.6 |   3.2 |    0.4 |    0.6 |      0 |    1   |              nan   |               86.1 |
| Fake the Source of Data          | 3000 |   0.1 |   5.3 |   0.4 |    5.5 |    0   |      0 |    0   |              nan   |               89.1 |
| HTTP Response Splitting          | 3000 |  12.5 |   5.5 |   0.2 |    1.2 |   11.5 |      0 |    0   |              nan   |               70.5 |
| HTTP Verb Tampering              | 3000 |   0.6 |   2.4 |   0.3 |    6   |    0   |      0 |    0   |              nan   |               91.1 |
| Input Data Manipulation          | 1387 |  24.1 |  74.8 |   6.9 |    9.2 |    8.1 |      0 |   10.1 |              nan   |               18   |
| Normal                           | 3000 |   1.3 |   0.2 |   0   |    0.4 |    0   |      0 |    0.4 |              nan   |               98.1 |
| OS Command Injection             | 3000 |  58.8 |  48.1 |  71.5 |    7.9 |   43.7 |      0 |    2.5 |               71.5 |                4.8 |
| Path Traversal                   | 3000 |   0   |   4.2 |   0.2 |    4.7 |   92.7 |      0 |    0   |               92.7 |                6.7 |
| Protocol Manipulation            | 3000 |  11.3 |   2.7 |   0.9 |    4.1 |    0.6 |      0 |    0.7 |              nan   |               81.8 |
| SQL Injection                    | 3000 |  87.2 |   3.6 |   8.3 |    4.7 |    0.7 |      0 |   14.8 |               87.2 |                9.7 |
| Scanning for Vulnerable Software | 2414 |   0   |   0   |   0   |    0   |    0.1 |      0 |    0   |              nan   |               99.9 |

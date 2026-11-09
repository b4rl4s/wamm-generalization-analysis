# Burp yoklama dizelerinin sınıflara dağılımı (DS-Augmented-v2)

Satır yüzdesi, sınıf başına en fazla 3000 satır, tamamen çözülmüş ham istek.

| Sınıf                     |    n |   polyglot `z'z"${{%{{ |   ' or N=N |   SSI <!--# |   {{ / ${ şablon |
|:--------------------------|-----:|-----------------------:|-----------:|------------:|-----------------:|
| 000 - Normal              | 3000 |                    0   |        0   |         0   |              0   |
| 126 - Path Traversal      | 3000 |                    0   |        0   |         0   |              0   |
| 1336 - SSTI               | 1897 |                    1.1 |        0   |        15.9 |              0.7 |
| 248 - Command Injection   | 2597 |                    0.8 |       39.5 |         0   |              0   |
| 66 - SQL Injection        | 3000 |                    0   |        1.9 |         0.2 |              0   |
| 79 - Cross-Site Scripting | 2894 |                    0.7 |        0   |         0   |              0   |
| 88 - OS Command Injection | 3000 |                   11.7 |        0   |         0   |              0   |
| 918 - SSRF                | 2645 |                    4.5 |        0   |         0   |              0   |
| 94 - Code Injection       | 1199 |                    0   |        0   |         0   |              0   |

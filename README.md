# Ilmaandmete lugemise rakendus
See on Pythoni-põhine konsooliprogramm, mis võimaldab kasutajal pärisajas vaadata maailma linnade
ilmaandmeid. Rakendus kasutab OpenWeatherMap API-t, et hankida andmeid temperatuuri,
õhuniiskuse ja ilmastiku kirjelduste kohta.

Programm on ehitatud, järgides objekt-orienteeritud programmeerimise (OOP) põhimõtteid ja on jaotatud loogilisteks 
mooduliteks:

1. <b>main.py:</b> Rakenduse sisenemispunkt. See haldab kasutajaliidest, küsib sisendit ja kutsub välja teenuskihi meetodid.

2. <b>weather_service.py:</b>  Teenuskiht, mis suhtleb välise API-ga. See kasutab requests raamatukogu HTTP-päringute tegemiseks ja veatöötluseks.

3. <b>weather_data.py:</b>  Andmemudel (Data Class), mis struktureerib API-st saadud toorandmed kasutajasõbralikuks objektiks.

4. <b>.env:</b>  Konfidentsiaalne fail API võtme hoidmiseks, et tagada turvalisus ja vältida tundlike andmete sattumist versioonihaldusesse.

### Rakenduse töövoog:
1. Kasutaja sisestab linna nime.

2. WeatherService koostab URL-i ja saadab GET-päringu API-le.

3. API vastab JSON-formaadis andmetega.

4. Teenus "pakib" andmed WeatherData objektiks.

5. WeatherApp prindib objekti sisu konsooli.

## Teoreetilised teemad, mida selle projektiga kaetakse
Andmetüübid ja muutujad: sõned (string), ujukomaarvud (float), sõnastikud (dict) andmete parsimiseks.

Tsüklid (while): kasutusel peamises töötsüklis, et programm ei sulguks pärast ühte päringut.

Tingimuslaused (if/else): kasutaja sisendi kontrollimiseks ja API vastuste valideerimiseks.

<b>Objekt-orienteeritud programmeerimine (OOP)</b>: 
<ul>Klassid ja objektid: rakendus on üles ehitatud klasside abil, et hoida kood organiseeritud ja taaskasutatav.</ul>

<ul> Konstruktor (__init__): kasutatakse objektide algseisundi seadistamiseks (nt API võtme edastamine).</ul>

<ul>Erimetoodid (__str__): kasutatud WeatherData klassis, et määrata, kuidas objekt end tekstina esitleb.</ul>

Samuti on projektile lisatud veahaldust erindite näol ning ühiktestid (k.a. Mocking API päringute simuleerimiseks testkeskkonnas).

### Lisadokumentatsiooni ja allikaid:
[OpenWeather API Docs](https://openweathermap.org/api/one-call-3?collection=one_call_api_3.0)

[Creating a Weather API with Python and OpenWeatherMap - Codez Up](https://codezup.com/creating-weather-api-python-openweathermap/)

## Käivitamisjuhend
Programmi käivitamiseks on vajalik Python versioon vähemalt 3.14. Alustamiseks klooni projekt:
```
git clone https://github.com/SwagMuffin88/weather-api-project.git
cd weather-api-project
```
Paigalda vajalikud moodulid:
```
pip install requests python-dotenv
```
Projekti juurkaustast leiad .env.example faili. Selleks, et python-dotenv saaks sellest lugeda välju,
tuleb see ümber nimetada: ```.env``` ja asendada näidisväärtus API võtmega.

Programmi käivitamiseks:
```python main.py```

Testide käivitamiseks: ```python test_weather.py```
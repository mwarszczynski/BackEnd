# DevOps Projects

## Main project 1 
Temat - dowolne pomysły, najciekawsze punktowane dodatkowo :)
Zbudować aplikację - 3-4 mikroserwisy API w oparciu o framework FLASK
Zaliczenie czy ocena ?
Nie oczekuję drugiego Netflixa lub Spotify
Praca w grupach
Dokumentacja


## Exercices
**Exercise_1** - Potrzebny jest program, który przekształci wprowadzony przez użytkownika ciąg cyfr na string: znaki, które nie są cyframi mają być ignorowane konwertujemy cyfry, nie liczby, a zatem: 544 to "pięć cztery cztery" 1002 to "jeden zero zero dwa"

**Exercise_2_konwerter** - Prawdziwy jest fakt, że woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita. Swtórz rozwiązanie "konwenter.py", który wyświetlać będzie tabelę przeliczeń stopni Celsjusza na Fahrenheita w następującym zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj, żeby wyświetlać znak plus/minus przy temperaturze.

**Exercise_3** - Zgodnie z informacją zamieszczoną na stronach rządowych Rejestr PESEL – Powszechny Elektroniczny System Ewidencji Ludności prowadzony jest od 1979 roku i zawiera dane osób przebywających stale na terytorium RP, zameldowanych na pobyt stały lub czasowy trwający ponad 2 miesiące a także osób ubiegających się o wydanie dowodu osobistego lub osób, dla których odrębne przepisy przewidują potrzebę posiadania numeru PESEL.
Budowa numeru PESEL jest następująca:
cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
cyfry 3-4 to dwie cyfry miesiąca urodzenia
cyfry 5-6 to dwie cyfry dnia urodzenia
cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
cyfra 11 suma kontrolna.

**Exercise_4** - Wykorzystując poznane metody na zajęciach oraz dokumentacje Pythona w wersji 3 stwórz prosty edytor tekstu w konsoli.
Wymogi:
Skorzystaj z obiektowości;
Wszelkie błędy w kodzie mają być obsłużone try,catch i logowane do pliku;
Wykorzystaj pętle while w celu uniknięcia ciągłego odpalania programu;
Za każdym razem jak wpisany zostanie “error” w pliku zostanie to przechwycone i zalogowane do pliku z logami;


**Exercise_5** - Wykorzystując przykłady z zajęć oraz dokumentacje Pythona3 i Flask’a napisz Api posiadające następujące endpointy:

/api/users -> zwraca użytkowników zdefiniowanych jako lista w aplikacji (zwraca plik json)
/api/users/delete/<user_id> -> usuwa użytkownika z konkretnym ID
/api/users/add/<user_id> -> tworzy nowego użytkownika na podstawie przekazanego user_id
/api/users/flush_db -> usuwa wszystkich użytkowników

**Exercise_7** - Przygotuj schemat dla projektu mikroserwis

**Exercise_8** - Przeprowadź migrację kodu do nowej struktury projektu - mikroserwis korzystając z blueprints


**Exercise_9** - Stwórz 2 instancję aplikacji Flask :
•	Pierwszy serwis zwracająca użytkownika : /api/user/<id>
•	Drugi serwis zwracający produkty z bazy danych: /api/product/<id>


## Main project 2
Stworzenie architektury dla naszej aplikacji utworzonej w ramach przedmiotu przetwarzanie równoległe;
Architektura prosta z wykorzystaniem wielu popularnych obecnie serwisów;
Stworzenie klastra bazy danych;
Stworzenie klastra Redis;
Stworzenie klastra RabbitMQ;
Przekierowanie nagłówków w HAPROXY;
NGINX dla naszej aplikacji.


## Exercices
**Exercise_1** - Nazwa zadania: Deployment nowego środowiska testowego
Opis zadania: Przygotuj proszę dla nas lokalne środowisko z wykorzystaniem docker-compose, posiadające następujące serwisy:
Serwer NGINX z php-fpm dostępny za pomocą portu 9080 oraz domeną app.localhost;
Bazę mysql 5.7 z podstawową konfiguracją oraz hasłem root: KrolKarolK0ral3;
Kontener z php-myadmin w celu wglądu do bazy danych;
Wolumen /var/lib/mysql ma być osobnym fs stworzonym w LVM;
Baza danych musi być w sieci secure;
Kontener dla frontendu z NodeJS;   -------------- ZDJECIE W WORDZIE ---------------

**Exercise_2** - Stwórz plik docker-compose.yml, który:
budować będzie obraz NGINX z Dockerfile;
NGINX wystawi dwa serwisy www:
api.mojadomena.com -> skonfigurować zgodnie z uWSGI;
mojadomena.com -> zwracać będzie plik index.html;
Volumeny dla serwisów mają być dostępne z poziomu hosta;
api.mojadomena.com wystawiona na porcie 9876;
Dla chętnych -> skonfigurować SSL - certyfikat self-signed wystarczy :)
									-------------- ZDJECIE W WORDZIE ---------------

**Exercise_3** - Utworzyć plik docker-compose, który zbuduje klaster (3) NoSQL scyllaDB:
•	udostępniony zostanie wolumen dla danych - /var/lib/scylla/data
•	sprawdzany będzie healthcheck czy dany węzeł działa poprawnie;
•	przygotowany będzie plik load_data.cql, który utworzy następujące keyspace przy starcie klastra: photos, company;
•	Keyspace company zawierać ma dwie tabele: employees oraz products i wypełniona zostanie przykładowymi danymi maks po 5 rekordów;
Dla chętnych: postawić do klastra scylla manager’a do monitorowania wydajności klastra i udostępnić serwis na porcie 80 dla localhosta (https://docs.scylladb.com/operating-scylla/manager/1.3/run-in-docker/)


**Exercise_4** -

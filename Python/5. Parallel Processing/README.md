# Python Projects

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

**Exercise_3_fibonaci** - 

**Exercise_4** - Zgodnie z informacją zamieszczoną na stronach rządowych Rejestr PESEL – Powszechny Elektroniczny System Ewidencji Ludności prowadzony jest od 1979 roku i zawiera dane osób przebywających stale na terytorium RP, zameldowanych na pobyt stały lub czasowy trwający ponad 2 miesiące a także osób ubiegających się o wydanie dowodu osobistego lub osób, dla których odrębne przepisy przewidują potrzebę posiadania numeru PESEL.
Budowa numeru PESEL jest następująca:
cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
cyfry 3-4 to dwie cyfry miesiąca urodzenia
cyfry 5-6 to dwie cyfry dnia urodzenia
cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
cyfra 11 suma kontrolna.

**Exercise_5** - Wykorzystując poznane metody na zajęciach oraz dokumentacje Pythona w wersji 3 stwórz prosty edytor tekstu w konsoli.
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
	•Pierwszy serwis zwracająca użytkownika : /api/user/<id>
	•Drugi serwis zwracający produkty z bazy danych: /api/product/<id>


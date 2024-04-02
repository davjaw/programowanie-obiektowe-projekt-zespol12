# programowanie-obiektowe-projekt

### 1. Etap 1 - Opis słowny działania programu

Aplikacja umożliwiająca tworzenie różnego typu wykresów, wykorzystująca web scraping ze strony IMDb. Użytkownik będzie miał możliwość filtrowania zakresu danych oraz ich kategorii. Dodatkowo wygląd oraz typ wykresu będą mogły być modyfikowane.

### 2. Etap 2 - Analiza MoSCoW
**MUST have (aplikacja będzie zawierać):**
- Wybór wykresów (kołowy, słupkowy, punktowy), 
- Modyfikacje danych wykresów ,
- Wybór gatunków,
- Wybór rocznika filmów, 
- Określenie ocen

**SHOULD have (aplikacja powinna zawierać):**
**Wyświetlenie wykresów:**

<ul>
<li> Wykres kołowy:
    <ul>
<li>% ocen w przedziale lat, </li>
<li>% ocen w przedziale gatunków, </li> 
<li>% gatunków w przedziale lat</li> 
    </ul>
</li>
</ul>

<ul>
<li>Wykres słupkowy: 
    <ul>
<li>średnia ocen na każdy gatunek,</li>
<li>średnia ocen na każdy rok </li> 
    </ul>
</li>
</ul>

<ul>
<li>Wykres punktowy: 
    <ul>
<li>oś x lata oś y wszystkie opinie,</li>
<li>oś x lata oś y % gatunków </li> 
    </ul>
</li>
</ul>

**COULD have (aplikacja może zawierać):**
- Porównywanie wykresów,
- Zmiana wyglądu wykresu,
- Wybór reżysera


**WON’T have (aplikacja na razie nie będzie zawierać):**
- Analizowania danych z innych stron,
- Analizowania danych z plików zewnętrznych 

### 3. Etap 3 - Diagram przypadków użycia

```mermaid
graph TD
subgraph "Aplikacja"
    A(Wybór typu wykresu) <-->|extend| B(Wybór zakresu danych)
    B <-->|extend| C(Pobieranie danych z serwisu)
    C <-->|extend| D(Wyświetlenie wyników)
    D -->|include| E(Modyfikacja danych do wykresu)
    E <-->|extend| C
end
```

### 5. Etap 5 - Wybranie systemu kontroli wersji oraz platformy hostingu dla niej, utworzenie repozytorium

Systemem kontroli wersji użytym w projekcie został **Git**. Głównymi powodami wyboru tego systemu są:

- możliwość jednoczesnej pracy przy kodzie przez kilka osób,
- transferowanie oraz łączenie zmian z różnych branchy,
- szybkość oraz wydajność systemu,
- możliwość pracy offline we własnym repozytorium.

Jako platformę hostingową dla systemu kontroli wersji wybrano **GitHub**. Wybór ten został uwarunkowany jej popularnością, wcześniejszym doświadczeniem z nią oraz szeroką gamą funkcjonalności umożliwiającymi w sposób wydajny rozwój własnego oprogramowania.

![Repozytorium na GitHub](github.png)

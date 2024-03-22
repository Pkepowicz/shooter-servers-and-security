# Shooters, servers and security
[Wykorzystane grafiki](https://thomasgvd.itch.io/top-down-shooter)  
[Wykorzystane tło](https://openverse.org/image/4973b527-1670-4f61-a045-af94de18c022?q=grass)

## About
Project made for a high-level programming languages course by Dawid Kowal and Paweł Kępowicz. A simple online game with client-server architecture developed using Pygame and Python's socket. Transmitted data is secured using AES cipher.

## Zad 1
Napisz metodę send_projectile, która przyjmuję obiekt klasy Projectile i przesyła go do serwera. Możesz wzorować się na kodzie metody send_player która znajduję się w tej samej klasie

## Zad 2
W klasie client zaimplementuj metode check_circle_overlap która sprawdzi czy koła o podanych parametrach się nakładają. Przyjmuje ona 4 argumenty:
1. pos1 - tablica dwuelementowa zawierająca współrzędne X i Y pierwszego obiektu (pos1[0] = x, pos1[1] = y)
2. radius1 - średnica pierwszego obiektu
3. pos2 - tablica dwuelementowa zawierająca współrzędne X i Y drugiego obiektu
4. radius2 - średnica drugiego obiektu  

Powinna zwrócić true jeśli oba koła się nakładają i false w każdym innym przypadku
## Zad3
W projekcie brakuję grafik dla graczy i pocisków. W konstruktorze klasy Client dodaj pola player_sprite i projectile_sprite do których za pomocą biblioteki pygame wczytasz odpowiednie pliki z rozszerzeniem .png. Pamiętaj o ich przeskalowaniu! Możesz skorzystać z plików w folderze assets, ale zachęcamy do kreatywności. Po wczytaniu obrazów wyszukaj w klasie Client miejsca w których wywoływana jest metoda draw na obiektach Player i Projectile i przekaż do nich odpowiednie pola.

## ZADANIE DODATKOWE 
Spróbuj połączyć się ze z inną osobą na sali :)

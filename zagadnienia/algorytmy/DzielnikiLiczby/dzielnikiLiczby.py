def dzielniki(n):

    # Po wprowadzeniu liczby typu np. float liczba konwertuje się na int
    n = int(n)
    
    # Jeśli liczba jest mniejsza od 1 zwróć komunikat o wprowadzenia poprawnej liczby
    if n < 1:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    if n == 0:
        return "!!!!Liczba nie może być zerem!!!!"

    # Utworzenie tablicy do której będą dodawane dzielniki liczby n
    nums = []
    
    # Dzielnik początkowy
    k = 1

    # Wykonuj pętle dopóki liczba jest większa lub równa od dzielnika
    while n >= k:
        # Wykonuj pętle dopóki reszta z dzielenia liczba n przez k będzie równa 0.
        while n % k == 0:
            
            nums.append(k)
            break

        k += 1

    # Funkcja która sortuje liczby od najmniejszej do największej.
    nums.sort()

    # Zwraca tablice dzielników liczby n
    return nums

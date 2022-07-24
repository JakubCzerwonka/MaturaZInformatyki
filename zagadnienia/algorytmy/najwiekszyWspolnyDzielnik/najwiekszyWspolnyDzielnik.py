def najwiekszy(x, y):

    # Jeśli liczba jest mniejsza od 1, równa 0 lub jest innego typu niż int zwróć komunikat o wprowadzenia poprawnej liczby
    if x == 0:
        return "!!!!Liczba nie może być zerem!!!!"
    elif y == 0:
        return "!!!!Liczba nie może być zerem!!!!"
    elif x < 1:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    elif y < 1:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    elif type(x) != int:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    elif type(y) != int:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"

    # Utworzenie tablic do której będą dodawane dzielniki liczby x i y 
    numsX = []
    numsY = []
    # Utworzenie tablicy do krórej będą wprowadzone liczby powatrzające się z tablic numsX i numsY
    numsD = []

    # Dzileniki liczb x i y    
    dX = 1
    dY = 1 

    # Wykonuj pętle dopóki liczba jest większa lub równa od dzielnika
    while x >= dX:
        # Wykonuj pętle dopóki reszta z dzielenia liczby x przez dX będzie równa 0.
        while x % dX == 0:
            
            numsX.append(dX)
            break
            
        dX += 1

    # Wykonuj pętle dopóki liczba jest większa lub równa od dzielnika
    while x >= dY:    
        # Wykonuj pętle dopóki reszta z dzielenia liczby y przez dY będzie równa 0.
        while y % dY == 0:

            numsY.append(dY)
            break
            
        dY += 1


    # Pętla sprawdzająca czy w tablicy numsY znajduje sie taka sama cyfra jak w numsX i jeśli się znajduje dodaję tę cyfrę do numsD
    for i in numsX:
        if i in numsY:
            numsD.append(i)
    
    # Zwraca największą liczbę z tablicy numsD (największy wspólny dzielnik liczb x i y)
    return max(numsD)

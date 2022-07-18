def rozloz(n):
    
    # Stworzenie kopi liczby n 
    d = n

    # Tworzenie pustej tablicy 'czynniki' oraz zmiennej pomocniczej 'k'
    nums = []
    k = 2
    
    # Jeśli liczba jest mniejsza od 1 lub równa 0 zwróć komunikat o wprowadzenia poprawnej liczby
    if n == 0:
        return "!!!!Liczba nie może być zerem!!!!"
    if n < 1:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"
    if type(n) != int:
        return "!!!!Wprowadź liczbę całkowitą naturalną!!!!"


    # Czy liczba jest różna od 1
    while n >= k: 
        # Czy po podzieleniu liczby zostaje jakaś reszta
        while n % k == 0:

            nums.append(k)
            n = n / k
        
        k += 1

    # Jeśli liczba ma tylko dwa dzielniki (1 i samą siebie), to jest liczbą pierwszą. W przypadku liczby 1 ma ona tylko jeden dzielnik.
    if len(nums) <= 1:
        return "Liczba: ", d, "jest liczbą pierwszą"
    

    return nums

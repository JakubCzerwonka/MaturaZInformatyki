def sortowanieBabelkowe(A):
    
    n = len(A)                                              # n = długość tablicy

    i = 0                                                   # iterator
    while i <= n:                                           # Dopóki iterator będzie większy lub równy długości tablicy
        
        j = 0                                               # Stworzenie nowego iteratora j    
        while j < n - i - 1:                                # Dopóki j będzie większe od długości tablicy - iterator - 1
            if A[j] > A[j + 1]:                             # Jeśli A[j] będzie mniejsze od A[j + 1]
                A[j], A[j + 1] = A[j + 1], A[j]             

            j += 1                                          
        i += 1

    return A

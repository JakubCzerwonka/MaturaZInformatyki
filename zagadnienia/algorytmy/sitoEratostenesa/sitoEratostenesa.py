def sitoEratostenesa(n):

    n += 1
    primes = []
    temp = [0] * (n + 1)
    for i in range(2,n):
        if temp[i] == 0:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                temp[j] = 1
    
    return primes

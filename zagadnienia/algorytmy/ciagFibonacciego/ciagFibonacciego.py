# Stworzenie funkcji rekurencyjnej
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

# Stworzenie tablicy w której umieszczane są numery fibonacciego
nums = []

# Dodanie do tablicy 20 liczb fibonacciego
for i in range(20):
    nums.append(fibonacci(i))

# Wyświetlenie tablicy w której umieszczone są numery fibonacciego
print(nums)

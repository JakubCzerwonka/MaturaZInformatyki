def potegowanieDoDrugiej(n):

    return n * n

def potegowanieDoTrzeciej(n):

    return n ** 3


x = float(input("Podaj liczbe: "))

print(potegowanieDoDrugiej(x))
print(potegowanieDoTrzeciej(x))

# Funckja wbudowana. Pierwszy argument to liczba którą chcemy podnieść do potęgi, a drugi argument to do ilu chcemy podnieść do potęgi liczbe z pierwszego argumentu. 
print(pow(x, 2))
print(pow(x, 3))

def palindrom(n):
    
    nMale = n.replace(' ', '').lower()

    if nMale == nMale[::-1]:
        return n,'Jest Palindromem' 
    else:
        return n,'Nie jest Palindromem'


x = input("Wpisz slowo: ")
print(palindrom(x))
 

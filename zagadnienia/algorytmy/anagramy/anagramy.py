def anagram(a,b):

    if len(a) != len(b):
        return a, "i", b, "to nie anagramy."
    else:
        aSorted = sorted(a)
        bSorted = sorted(b)

        if aSorted != bSorted:
            return a, "i", b, "to nie anagramy."
        else:
            return a, "i", b, "to anagramy."



slowaA = input("Podaj pierwsze slowo: ")
slowaB = input("Podaj drugie slowo: ")

print(anagram(slowaA, slowaB))

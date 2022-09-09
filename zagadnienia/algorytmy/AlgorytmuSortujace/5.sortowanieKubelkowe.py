def sortowanieKubelkowe(arr, k):                        # k = ilość kubełków       

    import CsortowaniePrzezWstawianie 

    arrH = []                                                      

    for i in range(k):                                           
        arrH.append([])                                         

    for i in arr:
        arrH[int(k * i)].append(i)                               

    for i in arrH:
        CsortowaniePrzezWstawianie.sortowaniePrzezWstawianie(i)    

    l = 0
    for i in range(k):                                             
        for j in range(len(arrH[i])):                            
            arr[l] = arrH[i][j]                                   
            l += 1                                            

    return arr

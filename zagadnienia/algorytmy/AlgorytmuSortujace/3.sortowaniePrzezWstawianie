def sortowaniePrzezWstawianie(A):
    
    n = len(A)                                      
    i = 1                                           

    while i < n:
        
        temp = A[i]                                 
        j = i - 1                                   

        while j >= 0 and temp < A[j]:              
            A[j+1] = A[j]                           
            j -= 1                                 
        A[j+1] = temp
        i += 1

    return A

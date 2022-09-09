def sortowanieBabelkowe(A):
    
    n = len(A)                                              

    i = 0                                                   
    while i <= n:                                           
        
        j = 0                                               
        while j < n - i - 1:                                
            if A[j] > A[j + 1]:                       
                A[j], A[j + 1] = A[j + 1], A[j]             

            j += 1                                          
        i += 1

    return A

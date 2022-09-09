def sortowaniePrzezWybieranie(A):

    n = len(A)
    i = 0                                       

    while i < n - 1:                            
     
        min = i                                 
        j = i + 1                               
        
        while j < n:                                                                
            if A[min] > A[j]:                   
                min = j                                                                            
            j += 1                                                                                                             
        
        if i != min:                                                                                                  
            A[i], A[min] = A[min], A[i]                                   
        i += 1                                                                                                                                
    
    return A

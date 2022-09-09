def partition(arr,l, r):
    
    pivot = arr[r]
    ptr = l
    for i in range(l, r):
        if arr[i] <= pivot:
            
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    
    arr[ptr], arr[r] = arr[r], arr[ptr]

    return ptr
 

 
def sortowanieSzybkie(arr, l, r):

    if len(arr) == 1:
        return arr
    if l < r:
        pi = partition(arr,l, r)
        sortowanieSzybkie(arr,l, pi-1)  
        sortowanieSzybkie(arr,pi+1, r)  
    return arr

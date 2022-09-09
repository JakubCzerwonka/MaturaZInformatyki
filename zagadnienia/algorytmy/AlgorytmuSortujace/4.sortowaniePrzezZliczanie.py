def sortowaniePrzezZliczanie(A, k):

    n = len(A)
    count = [0] * k
    output = [0] * n

    for i in range(0, n):                      
        count[A[i]] += 1

    for i in range(1, k):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1
        i -= 1

    return output

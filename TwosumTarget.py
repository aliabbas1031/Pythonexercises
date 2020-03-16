def two_sum_brute_force(A,arr):
    #A = [1,3,4,2,5,6,9,-2,-4,-9]
    #arr = 6

    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i] + A[j] == arr:
                return [A[i],A[j]]
    return [0,1]


print(two_sum_brute_force([1,3,4,2,5,6,9,-2,-4,-9], 7))
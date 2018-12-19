#-------------
# PSEUDOCODE
#-------------
#INSERTION-SORT(A)
#1 for j = 2 to A.length
#2     key = A[j]
#3     // Insert A[j] into the sorted sequence AOE1 : : j  1.
#4     i = j - 1
#5     while i > 0 and A[i] > key
#6         A[i + 1] = A[i]
#7         i = i - 1
#8         A[i + 1] = key

#Sample data (1-100 random sequence)
#[41, 62,  4, 50, 92, 61, 48, 60, 10, 89, 31, 28, 88, 97,  2, 65, 25, 21, 67,  6, 42, 95, 17, 93, 40, 78, 37, 72,  8, 20, 76, 14,100,  5, 15, 68, 86,  9, 33, 13, 22, 46, 83, 94,  3, 87, 30, 70, 39, 26, 57, 53, 80, 75, 54, 23, 98,  1, 90, 85, 66, 63, 55, 43, 29, 18, 52, 69, 73,  7, 71, 79, 45, 12, 58, 24, 38, 49, 51, 74, 56, 91, 16, 59, 19, 82, 34, 47, 84, 77, 96, 36, 99, 35, 81, 11, 32, 64, 27, 44]

def insertion_sort_inc(A):
    length = len(A)
    #1
    for j in range(1, length):
        #2
        key = A[j]
        #4
        i = j - 1
        #5
        while i >= 0 and A[i] > key:
            #6
            A[i+1] = A[i]
            #7
            i -= 1
        #8
        A[i+1] = key
    return A

#2.1-2
def insertion_sort_dec(A):
    length = len(A)
    #1
    for j in range(1, length):
        #2
        key = A[j]
        #4
        i = j - 1
        #5
        while i >= 0 and A[i] < key:
            #6
            A[i+1] = A[i]
            #7
            i -= 1
        #8
        A[i+1] = key
    return A
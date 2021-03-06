#
#
#   MERGE-SORT ALGORITHM
#
#
from itertools import combinations
# the intuitive first approach times out!
def naive_count_inversions(a):
    total = 0
    l = len(arr)
    for i,j in combinations(range(l),2):
        if a[i] > a[j]:
            total+= 1
    return total
    
###################################################   

# merge_sort takes an array as input an returs the sorted version of arr.
def mergesort(arr):
    n = len(arr)
    # a will contain the sorted array
    a = [e for e in arr]
    # we use temp as a global auxiliary variable
    temp = [0]*n
    merge_sort(a, temp, 0, n-1)
    return a
    
# This merge_sort sorts the array a[i:j+1] in place. 
# It doesn't return anything.
def merge_sort(a, temp, i, j):
    # Base case. A list of less than one element is sorted, by definition.
    if i >= j: 
        return
    # First divide the list in half and recursively sort both sublists
    mid = (i + j)//2
    merge_sort(a, temp, i, mid)
    merge_sort(a, temp, mid + 1, j)
    # Merge the sorted sublists
    merge(a, temp, i, mid+1, j)
    
def merge(a, temp, left_start, right_start, right_end):
    # idx keeps track of the index where we are adding the sorted 
    # elements of a to temp.
    idx = left_start
    # Add elements to the temp list.
    # i is the index of the left sublits and j of the right one.
    i = left_start
    j = right_start
    while i < right_start and j <= right_end:
        if a[i] <= a[j]:
            temp[idx] = a[i]
            i+= 1
        else:
            temp[idx] = a[j]
            j+= 1
            count+= right_start - i
        idx+= 1
    # Add the remaining of the lists to the result and copy .
    if i >= right_start:
        temp[idx:right_end+1] = a[j:right_end+1]
    else:
        temp[idx:right_end+1] = a[i:right_start]        
    # Now copy temp into a 
    a[left_start:right_end+1] = temp[left_start:right_end+1]
    
    
if __name__ == '__main__':
    q = int(input().strip())
    for i in range(q):
        count = 0
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        merge sort(arr)
        print(count)

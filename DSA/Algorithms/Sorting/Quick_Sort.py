# Quick Sort is another sorting algorithm which follows divide and conquer approach.
# It requires to chose a pivot, then place all elements smaller than the pivot on the left of the pivot and all elements larger on the right
# Then the array is partitioned in the pivot position and the left and right arrays followthe same procedure until the base case is reached.
# After each pass the pivot element occupies its correct position in the array.
# Time Complexity in Best and Average cases is O(nlog N) whereas in worst case it jumps up to O(n^2). Space complexity is O(log n)

#In this implementation, we will take the last element as pivot.
count = 0

def partition(array, left, right):
    smaller_index = left - 1
    pivot = array[right]
    for i in range(left, right):
        global count
        count += 1
        if array[i] < pivot:
            smaller_index += 1
            array[smaller_index], array[i] = array[i], array[smaller_index]
    array[smaller_index+1], array[right] = array[right], array[smaller_index+1]
    print(array)
    return (smaller_index+1)

def quick_sort(array, left, right):
    if left < right:
        partitioning_index = partition(array, left, right)
        print(partitioning_index)
        quick_sort(array,left,partitioning_index-1)
        quick_sort(array,partitioning_index+1,right)

array = [5,9,3,10,45,2,0]
quick_sort(array, 0, (len(array)-1))
print(array)
print(f'Number of comparisons = {count}')
'''
[0, 9, 3, 10, 45, 2, 5]
0
[0, 3, 2, 5, 45, 9, 10]
3
[0, 2, 3, 5, 45, 9, 10]
1
[0, 2, 3, 5, 9, 10, 45]
5
[0, 2, 3, 5, 9, 10, 45]
#Number of comparisons = 14
'''

sorted_array = [5,6,7,8,9]
quick_sort(sorted_array, 0, len(sorted_array)-1)
print(sorted_array)
print(f'Number of comparisons = {count}')
'''
[5, 6, 7, 8, 9]
4
[5, 6, 7, 8, 9]
3
[5, 6, 7, 8, 9]
2
[5, 6, 7, 8, 9]
1
[5, 6, 7, 8, 9]
Number of comparisons = 10
'''

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
quick_sort(reverse_sorted_array, 0, len(reverse_sorted_array) - 1)
print(reverse_sorted_array)
print(f'Number of comparisons = {count}')
'''
[-10, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, 9]
0
[-10, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, 9]
19
[-10, -9, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, 8, 9]
1
[-10, -9, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, 8, 9]
18
[-10, -9, -8, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, 7, 8, 9]
2
[-10, -9, -8, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, 7, 8, 9]
17
[-10, -9, -8, -7, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, 6, 7, 8, 9]
3
[-10, -9, -8, -7, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, 6, 7, 8, 9]
16
[-10, -9, -8, -7, -6, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, 5, 6, 7, 8, 9]
4
[-10, -9, -8, -7, -6, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, 5, 6, 7, 8, 9]
15
[-10, -9, -8, -7, -6, -5, 3, 2, 1, 0, -1, -2, -3, -4, 4, 5, 6, 7, 8, 9]
5
[-10, -9, -8, -7, -6, -5, 3, 2, 1, 0, -1, -2, -3, -4, 4, 5, 6, 7, 8, 9]
14
[-10, -9, -8, -7, -6, -5, -4, 2, 1, 0, -1, -2, -3, 3, 4, 5, 6, 7, 8, 9]
6
[-10, -9, -8, -7, -6, -5, -4, 2, 1, 0, -1, -2, -3, 3, 4, 5, 6, 7, 8, 9]
13
[-10, -9, -8, -7, -6, -5, -4, -3, 1, 0, -1, -2, 2, 3, 4, 5, 6, 7, 8, 9]
7
[-10, -9, -8, -7, -6, -5, -4, -3, 1, 0, -1, -2, 2, 3, 4, 5, 6, 7, 8, 9]
12
[-10, -9, -8, -7, -6, -5, -4, -3, -2, 0, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
8
[-10, -9, -8, -7, -6, -5, -4, -3, -2, 0, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
11
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
9
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Number of comparisons = 190
'''

#If the same algorithm is implemented with the pivot element = array[(right-left)//2], i.e., the  middle element of the array,
#then the number of comparisons for the reverse_sorted_array drops down to 91
#Number of comparisons for the sorted array = 6 and
#Number of comparisons for the first unsorted array = 11





def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)

def partition(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (a_list[right_mark], a_list[left_mark],)
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)






def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort_recursive(less_than_pivot) + [pivot] + quick_sort_recursive(greater_than_pivot)

arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_arr = quick_sort_recursive(arr)
print(sorted_arr)
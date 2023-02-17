from bisect import bisect_left, bisect_right

arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]

print(arr)
print(bisect_left(arr, -1))
print(bisect_left(arr, 5), bisect_right(arr, 5))

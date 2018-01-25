# -*- coding:utf-8 -*-
# 快速排序
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)
print quicksort([10,18,4,6,47,3])

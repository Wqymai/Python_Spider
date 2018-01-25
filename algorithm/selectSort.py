# -*- coding:utf-8 -*-
# 选择排序
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        # print 'arr['+str(i)+']:'+str(arr[i])+' smallest:'+str(smallest)
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    #返回最小值的索引
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

print selectionSort([5,83,9,1,10])
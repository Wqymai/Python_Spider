# -*- coding:utf-8 -*-
# 二分查找法
def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    count = 0
    while low <= high:
        mid = (low + high) / 2
        guess = lst[mid]
        count += 1
        if guess == item:
            print count -1
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [x for x in range(256)]
# print len(my_list)
binary_search(my_list, 255)


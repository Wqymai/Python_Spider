# from functools import reduce
# def make(x):
#     a = range(1,x+1)
#     print a
#     return a
#
# def mul(a,b):
#     print 'a=',str(a),'b=',str(b)
#     return  a*b
#
# l = reduce(mul,make(5))
# print l
print globals()
for name in globals().keys():
    print globals()[name]
#List
# alist = [9,6,10,7,1,4,3,5,2,8]
# print(alist)

#Sort
# alist.sort()
# print(alist)

#Sorted
# blist = sorted(alist)
# print(blist)

#vList = range(1,21)
# print(vList)
# print(list(vList))
##Functions
# def is_even(x):
#     return x%2 == 0
#
# vEvenNumbers = [num for num in vList if is_even(num)]
# print(vEvenNumbers)
#
# vEvenNumbersDescending = sorted(vEvenNumbers,reverse=True)
# print(vEvenNumbersDescending)

#Functions
vlist = range(1,21)
def is_even(x):
    return x%2 == 0

vEvenNumbers = sorted(filter(is_even,vlist),reverse=True)
print(vEvenNumbers)

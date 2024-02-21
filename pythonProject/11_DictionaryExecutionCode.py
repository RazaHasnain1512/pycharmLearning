#nums = [2,7,11,15,5,8,6,1,3]
#print(nums[0])
#print(nums[0],num[1])

# for i in nums:
#     print(i)

# result = [index for index, i in enumerate(nums)]
# print(result)

nums = [2,7,11,15,5,8,6,1,3]
#print(nums)
vInput = int(input('Enter a number : '))
#target = vInput
num_dict = {}

for i, num in enumerate(nums):
    complement = vInput - num
    print(complement)
    if complement in num_dict:
        vreturn = [num_dict[complement],i]
        print(vreturn)
        break
    num_dict[num] = i
    #print(num_dict)

# test_dict = {2:0, 7:1, 15:2}
# print(test_dict)
# print(test_dict.keys())
# print(test_dict.values())
# print(test_dict.items())
# print(test_dict[15])
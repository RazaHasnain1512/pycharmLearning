#nums = [2,7,11,15,5,8,6,1,3]
#print(nums[0])
#print(nums[0],num[1])

# for i in nums:
#     print(i)

# result = [index for index, i in enumerate(nums)]
# print(result)

nums = [2,7,11,15,5,8,6,1,3]
print(nums)

vInput = int(input('Enter a number : '))
target = vInput
num_dict = {}

for i, num in enumerate(nums):
    complement = target - num
    if complement in num_dict:
        vreturn = [num_dict[complement],i]
        print(vreturn)
        break
    num_dict[num] = i
    print(num_dict)

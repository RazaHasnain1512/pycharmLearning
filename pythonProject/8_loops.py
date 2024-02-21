# vnum = int(input ('Enter a number : '))
# for i in range(1,13):
#     print(f'{vnum} x {i} = {vnum*i}')
#     i += 1
#
# vMax = int(input('Enter first number : '))
# vMin = int(input('Enter second number : '))
# lcm = vMax
# while lcm % vMin != 0:
#     lcm += vMax
#     print (f'LCM of {vMax} and {vMin} is {lcm}')

user_input = input("Enter an English sentence or type 'quit' to exit : ")

while user_input.lower() != 'quit':
    print(f'You typed : {user_input}')
    user_input = input("Enter anoter English Sentence or type 'quit' to exit :")
print("Loop exited because typed 'quit' ")


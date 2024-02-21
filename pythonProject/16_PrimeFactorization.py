def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
        return True

    def prime_factors(n):
        factors = []
        divisor=2

        while n > 1:
            while n % divisor == 0 and is_prime(divisor):

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num//2+1):
        if num % i==0:
            return False
        return True

#Create a list of number from 1 to 101
numbers = list(range(1,101))

#Find prime numbers in the list
prime_numbers = [num for num in numbers if is_prime(num)]

#Print the list of numbers which are divisible by 5 and multiple of 8 between 2000 and 2500(both included)
# nums = []
# for i in range(2000, 2501):
#     if (i%5 == 0 and i%8 == 0):
#         nums.append(i)
# print(nums)

#Write a Python program to create the multiplication table (from 1 to 10) of a number getting input from the user
""" _num = int(input())

for i in range(1, 11):
    print(_num, "*", i, "=", _num*i) """

from tabnanny import check


def checkPrime(num):
    s = 0
    for i in range(1,num+1):
        if num%i==0:
            s = s + 1
    if(s>2):
        return False
    else:
        return True

print(checkPrime(5))
print(checkPrime(2))
print(checkPrime(12))
print(checkPrime(55))
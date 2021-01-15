## Day 8

#### 1. Write a program to create dictionary and access all elements with keys and values.

dic = {}
n = int(input("Enter dictionary element number\n"))
for i in range(n):
    key = input("key\n")
    value = int(input("value\n"))
    dic[key] = value
print(dic)
    

## Day 8

#### 1. Write a program to create dictionary and access all elements with keys and values.

dic = {}
n = int(input("Enter dictionary element number\n"))
for i in range(n):
    key = input("key\n")
    value = int(input("value\n"))
    dic[key] = value
print(dic)

#### 2. Write a Program to add a key to a dictionary.

-----------------------------------------------------------------------
    
dic = {}
n = int(input("Enter dictionary element number\n"))
for i in range(n):
    key = input("key\n")
    value = int(input("value\n"))
    dic[key] = value
print("Original Dictionary : "+str(dic))
key=input("Enter the key\n")
value=int(input("Enter the value\n"))
dic.update({key:value})
print("Updated dictionary is :\n"+str (dic))


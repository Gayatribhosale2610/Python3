## Day 10

#### 1.Write a program to remove a key from a dictionary.

dic1 = {}
a = int(input("Enter dictionary element\n"))
for i in range(a):
    key = input("key\n")
    value = int(input("value\n"))
    dic1[key] = value
print(dic1)
x = input("Enter key which you have to delete\n")
if x in dic1:
    del dic1[x]
print(dic1)

#### 2.Write a  program to multiply all the items in a dictionary.

dic1 = {}
n = int(input("Enter dictionary element\n"))
for i in range(n):
    key = input("key\n")
    value = int(input("value\n"))
    dic1[key] = value
print(dic1)
result=1
for j in dic1:
    result *= dic1[j]
print(result)

#### 3.Write a  program to map two lists into a dictionary.

lst1=[]
lst2=[]
n=int(input("Enter list element\n"))
for i in range(n):
    x=input()
    y=input()
    lst1.append(x)
    lst2.append(y)
print(lst1)
print(lst2)

dic=dict(zip(lst1,lst2))
print("Map two list\n"+str(dic))

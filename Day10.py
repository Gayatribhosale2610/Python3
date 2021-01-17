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

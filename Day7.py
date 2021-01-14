## Day 7

#### 1. Write a Python program to get the frequency of the elements in a list.

lst = []
freq = {}
n = int(input("Enter number of list\n"))
for i in range(n):
    a = int(input())
    lst.append(a)
print(lst)
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("frequency of elements in a list is :  "+str(freq))

#### 2. write a  program to count the number of elements in a list within a specified range.

list1 = []
c = 0
n = int(input("list elements \n"))
for i in range(n):
    a = int(input())
    list1.append(a)
print("List is :"+str(list1))

min = int(input("Enter the range\n"))
max = int(input("Enter the range\n"))
for j in list1:
    if j >= min and j <= max:
        c += 1
print("count the number of elements in a list within a range "
      +str(min) +" to "+str(max)+ " is  : " +str(c))

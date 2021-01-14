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

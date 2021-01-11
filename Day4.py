## Day 4

#### 1. A program to check a list is empty or not.

lst =[]
n = int(input("Enter list number:\n"))
for i in range(n):
    a = int(input())
    lst.append(a)
print(lst)
if not lst:
    print("List is empty")
else:
    print("List is not empty")
   
-----------------------------------------------------------

####  2. A program to find the list of words that are longer than n 

string = input ("Enter the string: \n")
a = string.split(" ")
b = []
n = int(input("enter the number : \n"))
for i in a:
    if len(i) > n:
        b.append(i)
print("List of words: ",b)

-------------------------------------------------------------

#### 3. A program to print the numbers of a specified list after removing even numbers from it.

lst = []
n = int(input("Enter list element:\n"))
for i in range(n):
    a = int(input())
    lst.append(a)
print(lst)
for i in lst:
    if i % 2 == 1:
         print(i)

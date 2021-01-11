## Day 4

#### A program to check a list is empty or not.

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

####  A program to find the list of words that are longer than n 

string = input ("Enter the string: \n")
a = string.split(" ")
b = []
n = int(input("enter the number : \n"))
for i in a:
    if len(i) > n:
        b.append(i)
print("List of words: ",b)

-------------------------------------------------------------

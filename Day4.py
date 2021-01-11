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

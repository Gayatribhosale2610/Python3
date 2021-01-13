  ## Day 6
  
#### 1.A program to get unique values from a list

list1 =[]
number1=int(input("enter length of list"))
print("enter element")
for i in range(int(number1)):
    l = int(input(""))
    list1.append(l)
print("list =",list1)
print("unique values =",list(set(list1)))

#### 2.A Program to check whether two list are circularly identical or not..

A=[]
n=int(input("length of list:"))
print("elements of first list:")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)

B=[]
n1=int(input("length of list:"))
print("Element of the Second List:")
for i in range(int(n1)):
   k=int(input(""))
   B.append(k)
if ' '.join(map(str, B)) in ' '.join(map(str, A * 2)):
   print("lists are circularly identical")
else:
    print("lists are not circularly identical")

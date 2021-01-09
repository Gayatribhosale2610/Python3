## Day 1

#### 1. Create list and displayed with append().

print("By using append() method")
lst = []
num = int(input("Enter list element : \n"))
for i in range(0,num):
    a = int(input())
    lst.append(a)
print("The appended list is : \n",lst)

print("without using append() method")
x = [21,32,43]
y = x + ['hello','welcome']
print("x is : \n",x)
print("appended list is : \n",y)
 
#### 2.Remove element from first, last and specific position.

print("Remove element from first location")
a = ['orange','apple','mango',34,7]
print("Given list is : \n",a)
a.remove(a[0])
print(a)

print("\nRemove element from last location")
b = ['orange','lichi','mango',6,54,'apple']
print("Given list is : \n",b)
b.remove(b[-1])
print(b)


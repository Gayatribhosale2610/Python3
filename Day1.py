## Day 1

### Create list and displayed with append().

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
 

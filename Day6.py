  ## Day 6
  
  #### program to get unique values from a list

list1 =[]
number1=int(input("enter length of list"))
print("enter element")
for i in range(int(number1)):
    l = int(input(""))
    list1.append(l)
print("list =",list1)
print("unique values =",list(set(list1)))

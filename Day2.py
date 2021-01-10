## Day 3

#### A program to get the number of occurrences of a specified element in an list.

lst = input("Enter your string\n")
count = 0
a = input("Enter which string you have to count\n")
for i in lst:
    
    if i == a:
        count = count+1
print("count of "+a+" is : "+str(count))

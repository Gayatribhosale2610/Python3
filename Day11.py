## Day 11

#### 1.Write a  program to print all unique values in a dictionary.

dict ={}
n=int(input("Enter Elements\n"))
for i in range(n):
    key =input("key\n")
    value =input("value\n")
    dict[key]=value
print("dictionary =",dict)
print("unique values in a dictionary =",set(dict.values()))

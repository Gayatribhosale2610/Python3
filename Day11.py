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

#### 2.Write a  program to find the highest 3 values in a dictionary.

dict ={}
n=int(input("Enter elements\n"))
for i in range(n):
     key =(input ("key\n"))
     value = int(input("value\n"))
     dict[key] = value
print ("Dictionary is : ", dict)
list = sorted (set (dict.values()))
print ("highest 3 values in dictionary : ", set (list [-3 :]))

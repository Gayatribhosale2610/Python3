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

-----------------------------------------------------------------------------------------------------------------------------------------

#### 2.Write a program to create and display all combinations of letters, selecting each letter from a different kay in a dictionary. 
dict={}
n=int(input("Enter Elements\n"))
for i in range(n):
    key=int(input("key\n"))
    value=eval(input("value\n"))
    dict[key]=value
print("dictionary is :",dict)
list1=list(dict.values())
for i in list1:
    for j in range(1,len(list1)):
        for a in list1[j]:
            dict1 =i+a
            print(dict1)

----------------------------------------------------------------------------------------------------------------------------------------
            
#### 3.Write a  program to find the highest 3 values in a dictionary.

dict ={}
n=int(input("Enter elements\n"))
for i in range(n):
     key =(input ("key\n"))
     value = int(input("value\n"))
     dict[key] = value
print ("Dictionary is : ", dict)
list = sorted (set (dict.values()))
print ("highest 3 values in dictionary : ", set (list [-3 :]))


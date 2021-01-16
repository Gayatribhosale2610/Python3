## Day 9

#### 1.Write a program to concatenate following dictionaries to create a new one. 

def dic1():
    d={}
    n=int(input("Enter elements\n"))
    for i in range(n):
        
        key=int(input("key\n"))
        value=int(input("value\n"))
        d[key]=value
    return d
d1=dic1()
d2=dic1()
d3=dic1()
print("dictionary 1=",d1,"\ndictionary 2=",d2,"\ndictionary 3=",d3)
dic4={}
for i in (d1,d2,d3):
    dic4.update(i)
print("Concatenated dictionary is: ",dic4)

#### 2.Write a Program to check whether a given key already exists in a dictionary.

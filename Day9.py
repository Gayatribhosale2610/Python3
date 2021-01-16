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

------------------------------------------------------------------------------------

#### 2.Write a Program to check whether a given key already exists in a dictionary.

dic = {}
n =int(input("Enter elements\n"))
for i in range(n):
    key=int(input("key\n"))
    value=int(input("value\n"))
    dic[key]=value
print("Dictionary: ",dic)
x=int(input("Enter key for checking\n"))
if x in dic:
    print("key exist in the dictionary")
else:
    print("key does not exist in dictionary")

-------------------------------------------------------------------------------------    
    
#### 3. Write a Program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

a=int(input("Enter any number\n"))
dic ={key:key * key for key in range(1,a+1)}
print("dictionary: ",dic)

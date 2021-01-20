## Day 15

#### 1.Write a program to print a dictionary line by line.
dic={}
n=int(input("enter element\n"))
for i in range(n):
    key=input("key\n")
    value=input("value\n")
    dic[key]=value
print(dic)

#### 2.Write a  program to  check multiple kays exists in a dictionary.
dic = {}
n = int(input("Enter dictionary element number\n"))
for i in range(n):
    key = input("key\n")
    value = int(input("value\n"))
    dic[key] = value
print(dic)
print("key exist in dictinary :",dic.keys()>={input()})
print("key exist in dictinary :",dic.keys()>={input()})

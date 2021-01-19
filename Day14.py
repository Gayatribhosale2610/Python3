## Day 14

#### 1.Write a  program to remove spaces from dictionary keys.

dic = {}
n = int(input("Enter dictionary element number\n"))
for i in range(n):
    key = input("key\n")
    value = int(input("value\n"))
    dic[key] = value
print(dic)
  
dic = {x.replace(' ', ''): v  
     for x, v in dic.items()} 
print (" New dictionary : ", dic)

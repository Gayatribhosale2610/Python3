## Day 3

#### A  program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

lst = []
n = int(input("length of a list: "))
print("Enter list elements: ")
count = 0;
for i in range(n):
    l1 = input()
    lst += [l1]
    if len(l1) > 1 and l1[0] == l1[-1]:
        count = count + 1
print("Given list is : ",lst)
print("number of strings having same first and last character in a list : ",count)

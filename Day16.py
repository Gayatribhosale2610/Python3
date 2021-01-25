## Day 20

#### Write a  program to count the number of characters (character frequency) in a string

freq = {}
str1 = input("Enter string : ")
for n in str1:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
print(freq)

---------------------------------------------------------------------------------------------------------------------------------------------------------

#### Write a  program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 

string = input("Enter the string\n")
a = string[0]
string = string.replace(a,'$')
string = a + string[1:]
print("All occurrences of its first char have been changed to '$'\ : ",string)

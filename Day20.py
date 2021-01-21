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

## Day 18

#### 1 Write a Python program to count and display the vowels of a given text.

string= input("Enter your string: ")
vowel = 0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'
         or i=='E' or i=='I' or i=='O' or i=='U'):
            vowel = vowel + 1
print("Number of vowels are:")


------------------------------------------------------------------------------

#### 2. Write a Python program to count occurrences of a substring in a string.

str1 = input("Enter the string\n")
count = 0
substr = input("Enter the substring\n")
for i in str1:
    
    count = str1.count(substr)
print("The occurences of substring in a string is: ", count)

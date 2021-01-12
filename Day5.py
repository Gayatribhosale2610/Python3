## Day 5

#### 2.A program to get the difference between the two lists.

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 60, 70]

print ("list1:", list1)
print ("list2:", list2)

print ("Difference elements:")
print (list (set(list1) - set (list2)))


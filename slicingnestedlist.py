# Slicing Nested List
x = [[10, 20, 30], 
	 [40, 50, 60], 
	 [70, 80, 90],
	 [11, 22, 33],
	 [44, 55, 66],
	 [77, 88, 99],
	 [12, 13, 14]]
print("Original List")
print(x)
print()
print("from 1st to 4th position")
a =x[1:5]
print(a)
print()
print("from 0 position tto to 6th position ")
b = x[0:7]
print(b)
print()
print("last 4 list ")
c = x[-4:]
print(c)
print() 

print("******upper function*****")
name = 'geekyshows' 
str1 = name.upper()
print(str1)
print()
print("*******lower function******") 
str2 = name.lower() 
print(str2) 
print() 
print("*******title function******")
str3= name.title() 
print(str3)
print() 
print("****** replace Function ******")
name = "Geekyshows"
old = "Geeky"
new = "New"
str1 = name.replace(old, new)
print(name)
print(str1)

print("****** split Function ******")
name = "Hello-how-are-you"
str1 = name.split('-')
print(name)
print(str1)

print("****** join Function ******")
name = ('Hello', 'How', 'Are', 'You')
str1 = "_".join(name)
print(name)
print(str1)
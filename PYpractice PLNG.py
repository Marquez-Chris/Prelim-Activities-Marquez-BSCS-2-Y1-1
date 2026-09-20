
txt =  'Hello, World!'
print (txt[5:7])
print (txt.upper())
name = "Python"
print (f"I love", (name))


print (10>9)
print (10 == 9)
print (10 < 9)


print(10>9)
print(10==9)
print(bool("Hello"))
print(bool(0))


a = 15 
b= 4
print (a%b, a//b, a**b)
a+=10
print (a)

collect = {"apple", "Banana", "Cherry"}
print(collect)

collect = {"apple", "Banana", "Cherry, Banana, apple"}
print(collect)

collect = ["apple", "Banana", "Cherry"]
collect.append("orange")
print(collect)


collect = ["apple", "Banana", "Cherry"]
collect.insert(2,"Dr. Maksuda Sultana")
print(collect)


collect = ["apple", "Banana", "Cherry"]
collect.insert(2,"Dr. Maksuda Sultana")
collect.remove("Dr. Maksuda Sultana")
print(collect)


collect = ["apple", "Banana", "Cherry"]
collect.pop(1)
print(collect)


collect = ["apple", "Banana", "Cherry"]
del collect[0]
print(collect)

collect = ["apple", "Banana", "Cherry"]
for i in range(len(collect)):
    print (collect)


collect = ["apple", "Banana", "Cherry", "Maxuda sultana"]
for i in range(len(collect)):
    print (collect)


collect = ["Red", "Green", "Blue"]
print (collect[0])
collect[1]="Yellow"
collect.append("Purple")
collect.remove("Red")
print(collect)


ht = "N", "A", "G", "I","G"
print (ht[-2]) 

collect = ("apple", "Banana", "Cherry","Melon","GinPomelo","Cuervo","tequilla")
print (collect[2:5])


a = 33 
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("A and is is equal")
elif a > b: 
    print("A is greater than B")


age = 20 

if age < 13:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("Gurang")


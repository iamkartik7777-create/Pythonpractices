name = "kartik singh"
age = 22
height =180.5

print(type(name))
print(type(age))
print(type(height))

print("My name is :",(name))
print("age is :",age)
print("and my height is :",(height))

print(len(name))
print(name.lower())
print(name.upper())
print (name.capitalize())
print(name.center(99))
print(name.title())
print(name.count("k"))
print(name.split())




x = 30
y = 30 
z = 30

x = str(x)
y = str(y)
z = str(z)

x =float(x)
y =float(y)
z =float(z)

print(x)
print(y)
print(z)


num1 = 2
num2 = 4
num3 = 6

print(num1,num2,num3)
print(num1, str(num1), float(num2), end=",")
print(num1+num2+num3)
print(num1-num2-num3)
print(num2/num3)
print(num1**4)
print(num3%2)

# Arithmetic operators example in one program

a = 20
b = 6

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponentiation (**):", a ** b)



first_name = "python"
print(first_name[1:4])
print(first_name[0:7])
print(first_name[-1])
print(first_name[-6:-1])

text ="python"
print(text.endswith("on"))
print(text.endswith("ou"))

text = "i love java" 
print(text.replace("java","python"))
print(text.find("love"))
print(text.find("java"))
print(text.count("a"))

My_list = [10,20,30,40,50,60]
value =My_list[1]
print(value - My_list[2])

My_tuple = (1,21,2,3,4,5,3,4,5,6)
print(My_tuple.count(3))
print(type(My_tuple))


d = {"name": "Kartik", "age": 20, "city": "Delhi"}

print(d.get("name") )     # Kartik
print(d.get("marks"))    # None

print(d.keys())    #dict_keys(['name', 'age', 'city'])

print(d.values())      #dict_values(['Kartik', 20, 'Delhi'])

print(d.items())      #dict_items([('name', 'Kartik'), ('age', 20), ('city', 'Delhi')])

d.update({"age": 21, "marks": 90})

d.pop("city")
d.popitem()
d.clear()
new_d = d.copy()
print(new_d)
d.setdefault("country", "India")

# print(d)
keys = ("a", "b", "c")
dict.fromkeys(keys, 0)
print(keys)






#[a-z, A-Z, _, 0-9]
name = "John"
# print(name)

# snake_case
my_name = "Vardan"
my_last_name = "Martirosyan"

# camelCase
myName = "Vardan"
myLastName = "Martirosyan"

#int -> Integer
myNumber = 33
print(myNumber)
print(type(myNumber))

#str -> String
myName = "John"
print(myName)
print(type(myName))

#float - > Float
myHeight = 180.5
print(myHeight)
print(type(myHeight))

#bool -> Boolean
amIFromArmenia = True
print(amIFromArmenia)
print(type(amIFromArmenia))

#______________________________________
print("_________________________")
print(myName, myLastName, my_name, my_last_name)

print("____________________________________")

number1 = 10
number2 = 2

print(number1, "-", number2, "=", number1 - number2)
print(number1, "+", number2, "=", number1 + number2)
print(number1, "*", number2, "=", number1 * number2)
print(number1, "/", number2, "=", number1 / number2)

print(type(number1))

str1 = "John"
str2 = "Smith"

print(str1, "+", str2, "=", str1 + str2)
print(str1, "*", number1, "=", str1 * number1)

x = 20
y = 3

summ = x + y
dev = x / y
mult = x * y
sub = x - y

print("Summ is: ", summ)
print("Dev is: ", dev)
print("Mult is: ", mult)
print("Sub is: ", sub)

print("___________________________________________")

print(myHeight)
myHeight = 182.5
print(myHeight)


x = 30
y = x
x = 40
y = x
print("X is: ", x)
print("Y is: ", y)

print("___________________________________________")

name = "Hello"
print(name.lower())
print(name.upper())
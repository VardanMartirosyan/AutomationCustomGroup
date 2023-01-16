
x = 6
y = 6
x1 = 7
y1 = 8
x2 = 7
y2 = 8

if y > x:
    print(y, "is greater then", x)
elif y == x:
    print(y, "equal to", x)
else:
    print(x, "is greater then", y)


# >  <  >=  <=  ==  !=  in

#if x > y:
#if x < y:
#if x >= y:
#if x <= y:
#if x == y:
#if x != y:
char = 'h'
word = "Hello"

if char in word:
    print(True)
elif char.lower() in word.lower():
    print("There are some uppercase or lowercase situation")
else:
    print(False)


userNum1 = int(input("Please input number: "))
userNum2 = int(input("Please input number: "))

if userNum1 < userNum2:
    pass
elif userNum1 == userNum2:
    print("Bad values inputed, please run again.")
    exit(3)
else:
    userNum1, userNum2 = userNum2, userNum1

while userNum1 <= userNum2:
    if userNum1 % 2 == 1:
        print(userNum1)
    userNum1 += 1

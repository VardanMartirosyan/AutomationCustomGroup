# https://www.w3schools.com/python/python_functions.asp
#
print(" 1. Write a function to multiply all the numbers in a given list")


def multiply_list_elements(someList):
    total = 1

    for i in someList:
        total *= i
    print(total)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
multiply_list_elements(myList)
multiply_list_elements([5, 7, 8])

print(" 2. Write a function that takes a list and returns a new list with unique elements of the first list")


def get_unique_elements(someList):
    mySet = set(someList)
    resultList = list(mySet)

    return resultList


myList = [1, 2, 3, 4, 2, 5, 1, 3, 3, 5, 6, 7, 8, 9]
expectedList = get_unique_elements(myList)
print(expectedList)
print(get_unique_elements([1, 1, 2, 2, 3, 3]))

print("# 3. Write a function to print the even numbers from a given list.")


def get_even_numbers(someList):
    listFromEvenNumbers = []
    for i in someList:
        if i % 2 == 0:
            listFromEvenNumbers.append(i)
        else:
            pass

    return listFromEvenNumbers


myList = [1, 2, 3, 4, 2, 5, 1, 3, 3, 5, 6, 7, 8, 9]
print(get_even_numbers(myList))

print(
    "# 4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.")


#      Sample String : 'The quick Brow Fox'
#      Expected Output :
#      No. of Upper case characters : 3
#      No. of Lower case Characters : 12

def show_uppercases_and_lowercases(text):
    uppercaseCount = 0
    lowercaseCount = 0

    for i in text:
        if i.isupper():
            uppercaseCount += 1
        elif i.islower():
            lowercaseCount += 1
        else:
            pass

    print(f"Uppercases count is:{uppercaseCount}")
    print(f"Lowercases count is: {lowercaseCount}")


show_uppercases_and_lowercases("Hello World")


# 5. Write a Python function that takes a number as a parameter and check the number is prime or not
def is_prime_number(numer):
    half = numer / 2
    if numer % 2 == 0:
        return False
    for i in range(3, int(half) + 1, 2):
        if numer % i == 0:
            print(i)
            return False

    return True

print(is_prime_number(99))
print(is_prime_number(239))
print(is_prime_number(21))
print(is_prime_number(17))


def prime_number(number):
    half = number / 2
    if number % 2 == 0:
        return False
    for i in range(2, int(half) + 1, 2):
        if number % i == 0:
            print(i)
            return False

    return True

print(prime_number(21))
print(prime_number(8))

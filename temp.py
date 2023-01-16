convertedList = [[1, [2, [2, [2, 2], 2], 2], 3], [4, [5, [5, 5], 5], 6], [7], [8, 9]]


def foo(myList):
    for i in myList:
        try:
            iter(i)
        except:
            yield i
        else:
            for elem in foo(i):
                yield elem

print(list(foo(convertedList)))







convertedList = [[1, [2, [2, [2, 2], 2], 2], 3], [4, [5, [5, 5], 5], 6], [7], [8, 9]]
def flatten(myList):
    result = []
    convertedList = [myList]
    while convertedList:
        current = convertedList.pop(-1)
        if isinstance(current, list):
            convertedList.extend(current)
        else:
            result.append(current)
    result.reverse()
    return result
print(flatten(convertedList))
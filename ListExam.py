myList = [1, [1, 2, [3, 3, [4, 4, 4, 4, ], 3, [5, 5, 5, 5, 5, 5, ]], 4], 3, [1, 2, [2, 2, 2, 2], 4], 5]
simpleList = [1, [2, 2], 3, [4, 4]]


def foo(baseList: list, childList: list, baseListIndex = 0):
    for i in childList:
        baseListIndex += 1
        if isinstance(i, list):
            for i in childList:
            baseList.insert(foo(i))
        else:
            pass

    return myList



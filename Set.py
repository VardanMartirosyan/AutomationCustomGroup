# Set

mySet = {"apple", "orange", "kiwi", "apple", "ananas", "kakach"}
mySecondSet = {"a", "b"}
print(mySet)
mySet.add("limone")
print(mySet)
mySet.pop()
print(mySet)
mySet.remove("apple")
print(mySet)
myCopySet = mySet.copy()
print(myCopySet)
print(mySet)
mySet.add("aa")
myCopySet.add("bb")
print(myCopySet)
print(mySet)
mySet.update(mySecondSet)
print(mySet)

mySet1 = {"A", "B", "C"}
mySet2 = {"A", "C", "B"}

if mySet1 == mySet2:
    print(True)
else:
    print(False)

myNumsSet = {-1, 2, 5, 3, -7, 1, 4, 11, -88, 12, -111, 0}
print(myNumsSet)

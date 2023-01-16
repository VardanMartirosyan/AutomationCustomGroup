# Dict

# imutable
# int, str, float, bool, tuple

myDict = {"BMW": {1, 2, 3, 4, 5, 6, 7, 8, "x1", "x3"},
          "Audi": ["A4", "A5", "A6"],
          4: "Str"}
print(myDict)
print("myDict length is: ", len(myDict))
print(myDict["Audi"])
print(len(myDict["BMW"]))

print(myDict)
myDict.pop(4)
print(myDict)
print("_______")
print(myDict.get("bmw"))
# print(myDict["bmw"])
# myDict.popitem()
print(myDict)
print(myDict.items())
print(myDict.values())
print(myDict.keys())
print(myDict)
myDict["Mercedes"] = {"A", "B"}
print(myDict)
myDict.update({"Ferrari": ["Enzo", "f40"], "BMW": "x7"})
print(myDict)
print("________________")
print(myDict)
myDict.update({"Suzuki": ["SX4", "Grant Gitara"]})
print(myDict)
myDict.update({"Suzuki": "SX5"})
print(myDict)
myDict["Ford"] = ["Fusion", "GT"]
print(myDict)
myDict["Ford"].append("Mustang")
# print(myDict["Ford"])
print(myDict)

for key, value in myDict.items():
    print(key)
    print(value)
    print("____")

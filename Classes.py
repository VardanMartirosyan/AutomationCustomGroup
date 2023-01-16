class People():
    def __init__(self, name, age=None, height=None):
        self.set_name(name)
        self.set_age(age)
        self.height = height
        print("Called Constructor")

    def sing(self):
        print("lya lya")

    def set_name(self, someName):
        self.name = someName

    def set_age(self, age):
        self.age = age

    def set_height(self, height):
        self.height = height

    def info(self):
        print(f"Name is {self.name}\nAge is {self.age}\nHeight is: {self.height}")


teacher = People("Vardan", 24, 165)
print(teacher.name)
teacher.info()

student = People("Nelli", height=166)
student.info()

student1 = People("Anna")
student1.info()
student.sing()

# student = People()
# student.set_name("Rafo")
# student.set_age(31)
# student.set_height(170.9)
# student.info()
#
# student2 = People()
# student2.set_name("Garik")
# student2.set_age(35)
# student2.set_height(180)
# student2.info()
#
# myList = [teacher, student, student2]
#
# print(myList)

class Student:
    def __init__(self, name, ID, email):
        self.__name = name
        self.__ID = ID
        self.__email = email

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_email(self):
        return self.__email

    def set_name(self, n):
        self.__name = n

    def set_ID(self, ID):
        self.__ID = ID

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return self.__name+" with ID: "+self.__ID+" and email: "+self.__email

class UndergraduateStudent(Student):
    def __init__(self, name, ID, email, noRequiredCredits, major):
        super().__init__(name, ID, email)
        # Student.__init__(self, name, ID, email)
        self.__noRC = noRequiredCredits
        self.__major = major

    def printMajor(self):
        print(self.__major)

    def __str(self):
        return Student.__str__(self)+self.__name+" with major: "+self.__major
        

student1 = UndergraduateStudent("Taylor", "32432", "taylorblabla@stevens.edu", 15, "CS")
print(student1.get_name())
student1.printMajor()
student2 = Student("Kyle", "34325", "kyleblabla@stevens.edu")
#student2.printMajor() will give error because superclass does not have access to subclass actions
print(student1)
print(student2)

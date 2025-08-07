# Class is a blueprint or a template. Eg A blank Form for an Exam that contain name, age father's name , roll no etc
# object is a specific instance created from template (class) Eg Form which contain the data about Glenn Maxwell

class Employee:
    company = "SUPARCO"

    def get_salary(self):   # self is important b/c self is the way to reference the object
                                                             #  of the class which is being created
        return 70000

e = Employee()     # An object of class Employee created here
print(e.get_salary())   # Emloyee e  salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)
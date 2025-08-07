class Employee:
    company = "Hp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        print(f"The name of employee is {self.name} and its salary is {self.salary}")

    @staticmethod    # if dont want to write self in argument
    def sum(a, b):
        return a + b

    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    
e1 = Employee("Jack", 35200)
e2 = Employee("roman", 32800)
print(Employee.company)

# print(Employee.name)  # This will Throw an error to remove this error we define new function of print_info
e1.print_info()
e2.print_info()

print(e2.sum(5,23))

e1.new_company()

e1.change_company("lenovo")
e1.new_company()
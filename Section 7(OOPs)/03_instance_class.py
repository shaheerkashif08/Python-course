class Employee:
    company = "Apis"

    def __init__(self, name, salary, contract, company):
        self.name = name
        self.salary = salary
        self.contract = contract
        self.company = company

    def get_salary(self):   
        return self.salary

    def get_info(self):
        print(f"The name of employee is {self.name}. The salary of Employee is about {self.salary} and contarct will end at {self.contract} years")

e1 = Employee("Shah Rukh", 55000, 7, "Mobilin")
print(e1.company)   # will always instance attribute if it is present
print(Employee.company)  # This will always print the class attribute 

# Object Introspection
print(dir(e1))
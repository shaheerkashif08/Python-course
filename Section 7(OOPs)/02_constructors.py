class Employee:
    company = "SUPARCO"

    def __init__(self, name, salary, contract):
        self.name = name  # Create an instance attribute named name and assign it with name
        self.salary = salary  # Create an instance attribute named salary and assign it with salary
        self.contract = contract  # Create an instance attribute named contract and assign it with contract

    def get_salary(self):   
        return self.salary

    def get_info(self):
        print(f"The name of employee is {self.name}. The salary of Employee is about {self.salary} and contarct will end at {self.contract} years")

e1 = Employee("Asim Munir", 70000, 5)
Employee.get_info(e1)
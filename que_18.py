class Employee:
    def __init__(self):
        self.name = None
        self.employee_id = None
        self.phone_number = None
        self.designation = None
        self.address = None

    def get_data(self):
        self.name = input("Enter your name: ")
        self.employee_id = input("Enter your employee_id: ")
        self.phone_number = input("Enter your phone_number: ")
        self.address = input("Enter your Address: ")
        self.designation = input("Enter your Designation: ")
        
    def print_data(self):
        print("")
        print(f"Employee Name is: {self.name}\nEmployee id is: {self.employee_id}\nEmployee phone number is: {self.phone_number}\nEmployee Address is: {self.address}\nEmployee Designation is: {self.designation}")


class Salary(Employee):
    def __init__(self):
        super(Salary, self).__init__()
        self.basic_pay = 0
        self.da = self.calculate_da()
        self.hra = self.calculate_hra()
        self.pf = self.calculate_pf()
        self.net_pay = self.calculate_netpay()

    def get_basicpay(self):
        super().get_data()
        try:
            self.basic_pay = int(input("\nEnter your Basic Pay: ")) 
        except ValueError:
            print("Invalid Salary")

    def calculate_da(self):
        return self.basic_pay * 0.08

    def calculate_hra(self):
        return self.basic_pay * 0.15

    def calculate_pf(self):
        return self.basic_pay * 0.1

    def calculate_netpay(self):
        return self.basic_pay + self.calculate_da() + self.calculate_hra() + self.calculate_pf()  

    def display(self):
        print(f"\nYour DA is: {self.calculate_da()}\nYour HRA is {self.calculate_hra()}\nYour net pay is: {self.calculate_netpay()}")


sal = Salary()
sal.get_basicpay()
sal.display()
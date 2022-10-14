class Student:

    def __init__(self):
        self.name =""
        self.roll_number = ""

    def get_data(self):
        self.name = input("Enter your name: ")
        self.roll_number = input("Enter your Roll Number: ")
        return (self.name, self.roll_number)

    def print_data(self):
         print(f"Your Name is: {self.name}\nYour Roll Number is: {self.roll_number}")


class Mark(Student):
    def __init__(self):
        super(Mark, self).__init__()
        self.physics = ""
        self.chemistry = ""
        self.biology = ""
        self.maths = ""
        self.english = ""
        self.malayalam = ""

    def get_data(self):
        super().get_data()
        self.mark_list = input("Enter your marks for Physics, Chemistry, Biology, Maths, English, Malayalam in order: ")
        self.physics = self.mark_list.split()[0]
        self.chemistry = self.mark_list.split()[1]
        self.biology = self.mark_list.split()[2]
        self.maths = self.mark_list.split()[3]
        self.english = self.mark_list.split()[4]
        self.malayalam = self.mark_list.split()[5]

    def print_data(self):
        print(f"Your marks is :\nPhysics:{self.physics}")


marks = Mark()
marks.get_data()
marks.print_data()

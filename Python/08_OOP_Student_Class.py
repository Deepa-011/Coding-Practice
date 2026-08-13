class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Deepa", 101, 85)

student1.display()
student1.result()

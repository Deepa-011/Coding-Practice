students = {
    101: {"name": "Deepa", "marks": 85},
    102: {"name": "Anjali", "marks": 78},
    103: {"name": "Rahul", "marks": 91}
}

print("Student Records:\n")

for roll_no, details in students.items():
    print("Roll No:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print("-------------------")

roll = int(input("Enter Roll Number to search: "))

if roll in students:
    print("\nStudent Found!")
    print("Name:", students[roll]["name"])
    print("Marks:", students[roll]["marks"])
else:
    print("Student not found.")

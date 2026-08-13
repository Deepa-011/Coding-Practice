with open("student.txt", "w") as file:
    file.write("Name: Deepa\n")
    file.write("Course: B.Tech CSE AI\n")
    file.write("Semester: 4th\n")

print("Data written successfully.")

with open("student.txt", "r") as file:
    data = file.read()

print("\nFile Content:")
print(data)

with open("student.txt", "a") as file:
    file.write("Subject: Python Programming\n")

print("Data appended successfully.")

import json

class Student:
    total_students = 0

    def __init__(self, name, age, m1, m2, m3):
        self.name = name
        self.age = int(age)
        self.m1 = int(m1)
        self.m2 = int(m2)
        self.m3 = int(m3)

        type(self).total_students += 1

    def show_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Maths Marks:", self.m1)
        print("Science Marks:", self.m2)
        print("English Marks:", self.m3)

    def to_dict(self):
      return {
        "name": self.name,
        "age": self.age,
        "m1": self.m1,
        "m2": self.m2,
        "m3": self.m3
    }

students = []

def add_student():
    name = input("Type student name: ").strip()
    age = input("Type student age: ").strip()
    m1 = input("Type your Maths marks: ").strip()
    m2 = input("Type your Science marks: ").strip()
    m3 = input("Type your English Marks: ").strip()
    students.append(Student(name, age, m1, m2, m3))
    pass

def view_students():
    if not students:
        print("No students yet.")
        return
    else:
      for s in students:
        s.show_info()
        print("Percentage:", percentage(s))
    pass

def show_total():
    print("Total No of Students:", Student.total_students)

def remove_student():
    name = input("Enter student name to remove: ").strip()
    found = False

    for s in students:
        if s.name == name:              
            students.remove(s)         
            Student.total_students -= 1 
            found = True
            break
    if not found:
        print("Student not found")
    else:
        print("Successfully removed")


def percentage(self):
    total = self.m1 + self.m2 + self.m3
    return (total/300)*100

def search_student():
    name = input("Enter name to search: ").strip()
    found = False

    for s in students:
        if s.name == name:
            s.show_info()
            found = True
            break

    if not found:
        print("Student not found")

def average_age():
    if not students:
        print("No students yet.")
        return

    total_age = 0
    for i in students:
      total_age = total_age + i.age
    average = total_age / Student.total_students

    print("The average of age of all students is:", average)

def save_data():
    data = [s.to_dict() for s in students]
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Data Saved Successfully!")


def load_data():
    try:
        with open("students.json", "r") as f:
            data = json.load(f)
        for item in data:
            students.append(
                Student(item["name"], item["age"], item["m1"], item["m2"], item["m3"])
            )
        print("Data loaded successfully!")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")


def main_menu():
    while True:
        print("\nSelect the menu options:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Show Total Students")
        print("4. Remove a Student from list")
        print("5. Search for a student")
        print("6. Average age")
        print("7. Save the Data")
        print("8. Load the Data")
        print("9. Quit")
        choice = input("Type your choice of menu: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            show_total()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            average_age()
        elif choice == "7":
            save_data()
        elif choice == "8":
            load_data()

        elif choice == "9":
            print("Exiting the CLI application. Bye!")
            break
        else:
            print("Enter a valid menu number (1-4).")

if __name__ == "__main__":
    main_menu()


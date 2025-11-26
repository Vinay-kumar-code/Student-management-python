# Student Manager CLI

A simple Python command‑line application to manage student records.  
This project was built **module by module (function by function)** to demonstrate clean design, file handling, and basic data persistence.

---

## ✨ Features
- Add new students with name, age, and marks
- View all students in a formatted list
- Show the total number of students
- Remove a student by name
- Search for a student
- Calculate the average age of all students
- Save student data to a JSON file
- Load student data from a JSON file
- Quit the application gracefully

---

## 📂 Project Structure
- `student_manager.py` → main CLI script
- `students.json` → JSON file used for saving/loading data
- Functions are modular (e.g., `add_student()`, `remove_student()`, `save_data()`, `load_data()`)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation
Clone the repository:
```bash
git clone https://github.com/your-username/student-manager-cli.git
cd student-manager-cli
```
### Usage
Run this program:
```bash
python student_manager.py
```
You'll see a menu like this:
```bash
1. Add Student
2. View All Students
3. Show Total Students
4. Remove a Student from list
5. Search for a student
6. Average age
7. Save the Data
8. Load the Data
9. Quit
```



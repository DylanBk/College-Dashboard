import sqlite3

conn = sqlite3.connect("GoOnlinePt3.db")
cur = conn.cursor()

def viewAllStudents():
    res = cur.execute("SELECT * FROM Student;")
    print("\n", res.fetchall(), "\n")
    menu()

def viewStudentsInArea():
    location = input("\nPlease select a location:\n [1] Norwich\n [2] Birmingham\n [3] Bristol\n [4] Manchester\n [5] Lincoln\n [6] London\n [7] Plymouth\n> ")

    res = cur.execute(f"SELECT * FROM Student WHERE centre_id = {location};")
    print("\n", res.fetchall(), "\n")
    menu()

def search():
    name = input("\nEnter the student's name: ")
    location = input("Please select a location:\n [1] Norwich\n [2] Birmingham\n [3] Bristol\n [4] Manchester\n [5] Lincoln\n [6] London\n [7] Plymouth\n> ")

    res = cur.execute(f"SELECT * FROM Student WHERE student_name = '{name}' and centre_id = {location};")
    print(res.fetchall())
    menu()

def addStudent():
    student_id = input("\nEnter student ID: ")
    name = input("Enter student name: ")
    location = input("Enter centre id: ")

    res = cur.execute(f"INSERT INTO Student(student_id, centre_id, student_name) VALUES({student_id}, {location}, '{name}');")

    print("\nStudent added succesfully\n")
    menu()

def menu():
    choice = input("\n-- ACC Dashboard --\n[1] View all students\n[2] View students based on area\n[3] Search for a student\n[4] Add a student\n> ")

    if choice == "1":
        viewAllStudents()
    elif choice == "2":
        viewStudentsInArea()
    elif choice == "3":
        search()
    elif choice == "4":
        addStudent()
    else:
        print("\nError: Invalid input\n")
        menu()

menu()
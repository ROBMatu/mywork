# student.py
# Author: Robert O'Brien-Monk
# A program to create and view students using functions

# function definitions
# menu
def display_menu():
    print("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Enter letter choice(a/v/q): ").lower().strip()
    return choice

# add students functions
def do_add(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= read_modules()
    students.append(currentStudent)

def read_modules(): 
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter the grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules

# view students functions
def display_modules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{ module['grade']}")


def do_view(students):
    for currentStudent in students:
        print(currentStudent["name"])
        display_modules(currentStudent["modules"])


# main program 
students = []

choice = display_menu()
while (choice != "q"):
    if choice == 'a':
        do_add(students)
    elif choice == 'v':
        do_view(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice = display_menu()
# Initialize an empty list to store student names
students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("{name} has been added to the list.")



def remove_student():
    
        
        index = int(input("Enter the number of the student to remove: ")) - 1
        if 0 <= index < len(students):
                rem_student = students.pop(index)
                print("{rem_student} has been removed from the list.")
        else:
                print("Invalid number.")
def view_list():
    if not students:
        print("empty list")
    else:
        for i in range(len(students)):
            print(students[i])
        
       
def data():
    print("choose the option what do u like to perform in student list:(ADD,REMOVE,SHOW)")
    while True:
        print("Menu:")
        print("1. Add")
        print("2. Remove")
        print("3. view")
        print("4. exit")
        option=input("enter your option (1-4):")
        if option =="1":
            add_student()
        elif option=="2":
            remove_student()
        elif option=="3":
            view_list()
        else:
            break
data()  
    


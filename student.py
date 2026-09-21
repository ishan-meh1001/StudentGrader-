class Student:
    # The __init__ method is the constructor used to initialize attributes
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        grades=[]

    # "self" refers to the specific object instance calling the method
    def displayinfo(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Major:", self.major)

    def inputgrades():
        for i in range(5):
            grade = float(input("Enter grade {}: ".format(i + 1)))
            self.grades.append(grade)

        

def main():
    # Create a Student object
    student = Student("John Doe", 20, "Computer Science")
    
    # Call the display method
    student.displayinfo()

# This ensures main() runs when the script is executed
if __name__ == "__main__":
    main()



class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        self.marks = []       # Holds raw numeric marks (0-100)
        self.grades = []      # Holds letter grades (A, B+, etc.)

    def displayinfo(self):
        print("\n" + "="*30)
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Major:", self.major)
        print("="*30)

    def inputgrades(self):
        self.marks = []
        self.grades = []
        subjects = ["Mathematics", "Data Structures", "Operating Systems", "Software Engineering", "Web Technology"]
        
        print("\n--- Enter Marks for 5 Subjects ---")
        for sub in subjects:
            # Increment 3: Input Validation Loop
            while True:
                try:
                    mark = float(input(f"Enter marks for {sub} (0-100): "))
                    if 0 <= mark <= 100:
                        self.marks.append(mark)
                        # Allocate letter grade immediately based on mark boundaries
                        letter_grade = self.allocate_letter_grade(mark)
                        self.grades.append(letter_grade)
                        break
                    else:
                        print("Invalid input! Marks must be between 0 and 100.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

    # Increment 2: Mapping marks to Letter Grades (JIIT/Standard style)
    def allocate_letter_grade(self, mark):
        if mark >= 90: return "A"
        elif mark >= 80: return "B+"
        elif mark >= 70: return "B"
        elif mark >= 60: return "C+"
        elif mark >= 50: return "C"
        elif mark >= 40: return "D"
        else: return "F"

    # Increment 2: Mapping Letter Grades to GPA Value Scale (e.g., Out of 10 or 4)
    def letter_grade_to_gpa(self, grade):
        gpa_map = {
            "A": 10.0,
            "B+": 9.0,
            "B": 8.0,
            "C+": 7.0,
            "C": 6.0,
            "D": 5.0,
            "F": 0.0
        }
        return gpa_map.get(grade, 0.0)

    # Increment 2: Calculate overall performance metrics
    def calculate_metrics(self):
        if not self.marks:
            return None
        
        # Calculate percentage based on total marks
        total_marks = sum(self.marks)
        percentage = (total_marks / 500) * 100
        
        # Calculate GPA based on the allocated letter grades
        total_gpa_points = sum(self.letter_grade_to_gpa(g) for g in self.grades)
        final_gpa = total_gpa_points / len(self.grades)
        
        # Determine Pass/Fail status
        status = "Fail" if "F" in self.grades or percentage < 40 else "Pass"
        
        return percentage, final_gpa, status
    
    # Increment 3: Output Clean Summary Report
    def display_report(self):
        metrics = self.calculate_metrics()
        if metrics is None:
            print("No marks available to generate report.")
            return
            
        percentage, final_gpa, status = metrics
        
        print("\n" + "═"*15 + " PERFORMANCE REPORT " + "═"*15)
        subjects = ["Math", "DSA", "OS", "SE", "WebTech"]
        
        print(f"{'Subject':<15} | {'Marks':<8} | {'Grade':<5}")
        print("-" * 35)
        for i in range(5):
            print(f"{subjects[i]:<15} | {self.marks[i]:<8.1f} | {self.grades[i]:<5}")
            
        print("═" * 50)
        print(f"Aggregate Percentage : {percentage:.2f}%")
        print(f"Calculated SGPA      : {final_gpa:.2f} / 10.0")
        print(f"Final Status         : {status}")
        print("═" * 50)


def main():
    # User Input for Student Info
    print("--- Initializing Student Profile ---")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    major = input("Enter Student Major: ")
    
    student = Student(name, age, major)
    
    student.displayinfo()
    student.inputgrades()
    student.display_report()


if __name__ == "__main__":
    main()

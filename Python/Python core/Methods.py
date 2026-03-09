class Student:
    # Class variables (shared by all students)
    total_students = 0
    passing_mark = 40   # shared passing mark
    all_students = []   # keep track of all student objects

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
        Student.all_students.append(self)

    def has_passed(self):
        return self.marks >= Student.passing_mark

    @classmethod
    def curve_marks(cls, percentage):
        """Increase everyone's marks by given percentage."""
        for student in cls.all_students:
            increase = student.marks * (percentage / 100)
            student.marks = min(100, student.marks + increase)  # cap at 100

    @staticmethod
    def convert_to_grade(marks):
        """Convert numeric marks to letter grade."""
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        status = "Passed" if self.has_passed() else "Failed"
        grade = Student.convert_to_grade(self.marks)
        print(f"{self.name}: Marks={self.marks:.1f}, Grade={grade}, Status={status}")
# 1. Creating multiple students
s1 = Student("Alice", 35)
s2 = Student("Bob", 78)
s3 = Student("Charlie", 92)

print("Before Curving:")
s1.display()
s2.display()
s3.display()

# 2. Applying a grading curve (+10%)
Student.curve_marks(10)

print("\nAfter Curving:")
s1.display()
s2.display()
s3.display()

# 3. Show total students created
print(f"\nTotal Students: {Student.total_students}")
# Project Requirements
# 1️⃣ Functional Requirements
# The system should store school name as a static variable shared by all students.
# The system should store student name and marks as instance variables.
# The system should have a method to calculate the grade based on marks:
# Marks ≥ 90 → Grade A
# Marks ≥ 75 and < 90 → Grade B
# Marks ≥ 50 and < 75 → Grade C
# Marks < 50 → Fail
# The method should use a local variable to hold the grade before returning it.
# The program should display:
# School name (static variable)
# Student name (instance variable)
# Calculated grade (local variable result)

# student grade claculations
class school:
    school_name="Pentagon space"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def grade_cal(self):
        if self.marks>=90:
            print("grade A")
        elif self.marks>=75 and self.marks<90:
            print("grade B")
        elif self.marks>=50 and self.marks<75:
            print("grade C")
        else:
            print("fail")

s1=school('nandi',75)
s2=school('kali',90)
s3=school('kohli',49)


print(school.school_name)
print("student name is:",s1.name)
print("student marks is:",s1.marks)

s1.grade_cal()

print(school.school_name)
print("student name is:",s2.name)
print("student marks is:",s2.marks)

s2.grade_cal()

print(school.school_name)
print("student name is:",s3.name)
print("student marks is:",s3.marks)

s3.grade_cal()















#practice q1
try:
    with open("missing.txt","r") as f:
       f.read()
        
except FileNotFoundError:
        print("File doe not exist")
finally:
        print("Operation attempted")


#practice q2
class Student:
      def __init__(self,name,grade):
            self.name = name
            self.grade = grade
      def __str__(self):
            return f"{self.name}:{self.grade}"
      
def save_student(student):
    with open("students.txt", "a") as f:
         f.write(f"{student.name}: {student.grade}\n")
def load_students():
      try:
          with open("students.txt","r") as f:
              for line in f:
                print(line.strip())

               

      except FileNotFoundError:
                print("No students found yet")      


s1 = Student("Smarika", 85)
s2 = Student("Ram", 92)
s3 = Student("Priya", 78)

save_student(s1)
save_student(s2)
save_student(s3)

load_students()
            
            
      
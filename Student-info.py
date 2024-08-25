#This code takes the name, student id and the field of study of the student

class Student:

    def __init__(self, name, student_id, field_of_study):
        """
        Initializes the Student.
        
        """
        self.name = name
        self.student_id = student_id
        self.field_of_study = field_of_study

    def get_student_info(self):
        """
        Returns the student's information.
        
        """
        return f"Student Name: {self.name}\nStudent ID: {self.student_id}\nField of Study: {self.field_of_study}"

def main():
    """
    creating a Student object.
    """
    # Creating a sample student
    student = Student("Azin", 12345, "Computer Science")
    print(student.get_student_info())

if __name__ == "__main__":
    main()

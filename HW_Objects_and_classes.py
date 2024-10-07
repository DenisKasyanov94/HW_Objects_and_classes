class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
            super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self) -> str:
        return 'Имя: '  + self.name + '\nФамилия: ' + self.surname
        
                   
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def Compare_avrage(self,lecturer):
        avr_el_self = Get_Avr(self)
        avr_el_lecturer = Get_Avr(self)
        if avr_el_self > avr_el_lecturer:
            print(self)
        elif avr_el_self < avr_el_lecturer:
            print (lecturer)
        else:
            print ('Средний балл равен')
             

    def __str__(self) -> str:
        return 'Имя: '  + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(Get_Avr(self))
    
    def __eq__(self, other):
        return Get_Avr(self) == Get_Avr(other)

    def __ne__(self, other):
        return not Get_Avr(self)

    def __lt__(self, other):
        return Get_Avr(self) < Get_Avr(other)

    def __le__(self, other):
        return Get_Avr(self) <= Get_Avr(other)

    def __gt__(self, other):
        return Get_Avr(self) > Get_Avr(other)

    def __ge__(self, other):
        return Get_Avr(self) >= Get_Avr(other)
    

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    

        
    def __eq__(self, other):
        return Get_Avr(self) == Get_Avr(other)

    def __ne__(self, other):
        return not Get_Avr(self)

    def __lt__(self, other):
        return Get_Avr(self) < Get_Avr(other)

    def __le__(self, other):
        return Get_Avr(self) <= Get_Avr(other)

    def __gt__(self, other):
        return Get_Avr(self) > Get_Avr(other)

    def __ge__(self, other):
        return Get_Avr(self) >= Get_Avr(other)
            
        
    def Compare_avrage(self,student):
        avr_el_self = Get_Avr(self)
        avr_el_student = Get_Avr(student)
        if avr_el_self > avr_el_student:
            print(self)
        elif avr_el_self < avr_el_student:
            print (student)
        else:
            print ('Средний балл равен')
        
    
        
    def __str__(self) -> str:
        courses = ','.join(self.courses_in_progress)
        finished_courses = ','.join(self.finished_courses)
        return ('Имя: '  + self.name +'\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: ' + str(Get_Avr(self)) +
                '\nКурсы в процессе изучения: ' + courses + '\nЗавершенные курсы: ' + finished_courses)
        

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade >= 1 and grade <=10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценка должна быть от 1 до 10'
        else:
            return 'Ошибка'
        
def Get_Avr(source):
    grades = sum(source.grades.values(), [])
    quant_el = len(grades)
    sum_el = sum(grades)
    if quant_el == 0:
        return 0
    else:
        return sum_el / quant_el 
    

    
def Get_Avr_students(students, course):
    all_grades = []
    for student in students:
        if course in  student.grades:
            grades = [marks for marks in student.grades[course]]
            all_grades += grades
    if len(all_grades) != 0:
        return sum(all_grades) / len(all_grades)
    else:
        return 0
 



def Get_Avr_lecturer(lectors, course):
    all_grades = []
    for lector in lectors:
        if course in lector.grades:
            grades_list = [marks for marks in lector.grades[course]]
            all_grades += grades_list
    if len(all_grades) != 0:
        return sum(all_grades) / len(all_grades)
    else:
        return 0
    
   
           
        
lecturer1 = Lecturer("Stephen", "Hawking")
lecturer1.courses_attached = ["Python"]

lecturer2 = Lecturer("Bill", "Gates")
lecturer2.courses_attached = ["Python"]
        
student1 = Student("Jhnn", "Doe", "male")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]
student1.rate_hw(lecturer1, "Python", 9)
student1.rate_hw(lecturer2, "Python", 8)

student2 = Student("Jane", "Doe", "female")
student2.courses_in_progress = ["Python", "Git"]
student2.finished_courses = ["Введение в программирование"]
student2.rate_hw(lecturer1, "Python", 7)
student2.rate_hw(lecturer2, "Python", 9)

reviewer1 = Reviewer("Michael", "Stevens")
reviewer1.courses_attached = ["Python","Git"]
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Git", 8)
reviewer1.rate_hw(student2, "Python", 4)
reviewer1.rate_hw(student2, "Git", 9)

reviewer2 = Reviewer("Alan", "Turin")
reviewer2.courses_attached = ["Python","Git"]
reviewer2.rate_hw(student1, "Python", 6)
reviewer2.rate_hw(student1, "Git", 5)
reviewer2.rate_hw(student2, "Python", 3)
reviewer2.rate_hw(student2, "Git", 7)

students_list = [student1, student2]
course_name = 'Python'
lecturer_list = [lecturer1, lecturer2]
print(Get_Avr_students(students_list, course_name))
print(Get_Avr_lecturer(lecturer_list, course_name)) 

print(student1)
print(student2)

print(reviewer1)
print(reviewer2)

print(lecturer1)
print(lecturer2)

lecturer1.Compare_avrage(lecturer2)
student1.Compare_avrage(student2)

print(lecturer1 == lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)

print(student1 == student2)
print(student1 > student2)
print(student1 < student2)
from peewee import *

test_db = SqliteDatabase(':memory:') # test database

class BaseModel(Model): 
    class Meta:
        database = test_db

class Students(BaseModel):
    id = AutoField()
    name = CharField(max_length=15, null=False)
    surname = CharField(max_length=20, null=False)
    age = IntegerField(null=False)
    city = CharField(max_length=20, null=False)


class Courses(BaseModel):
    id = AutoField()
    name = CharField(max_length=10, null=False)
    time_start = DateField(null=False)
    time_end = DateField(null=False)


class StudentCourses(BaseModel):
    student_id = ForeignKeyField(Students, field=Students.id, backref='courses')
    course_id = ForeignKeyField(Courses, field=Courses.id, backref='students')
    primary_key = CompositeKey('student_id', 'course_id') 

'''
Create DB
'''
test_db.connect()
test_db.create_tables([Students, Courses, StudentCourses])


'''
Create StudentCources's objects, with student delete their courses/dependencies
'''
def add_student_course(student_id, course_id):
    StudentCourses.create(student_id=student_id, course_id=course_id)

def delete_student(student_id):
    StudentCourses.delete().where(StudentCourses.student_id == student_id).execute()
    student = Students.get(Students.id == student_id)
    student.delete_instance()


'''
Tests
'''
import unittest

class TestORM(unittest.TestCase):

    def setUp(self):
        '''
        Clean DB up before running tests
        '''
        test_db.drop_tables([Students, Courses, StudentCourses])
        test_db.create_tables([Students, Courses, StudentCourses])
    
    def test_add_student(self):
        student = Students.create(name='Max', surname='Brooks', age=24, city='Spb')
        self.assertIsNotNone(student.id)

        student_by_id = Students.get(Students.id == student.id)
        self.assertEqual(student_by_id.name, 'Max')
        self.assertEqual(student_by_id.surname, 'Brooks')
        self.assertEqual(student_by_id.age, 24)
        self.assertEqual(student_by_id.city, 'Spb')

    def test_add_course(self):
        course = Courses.create(name='python', time_start='2021-07-21', time_end='2021-08-21')
        self.assertIsNotNone(course.id)

        course_by_id = Courses.get(Courses.id == course.id)
        self.assertEqual(course_by_id.name, 'python')
        self.assertEqual(course_by_id.time_start, '2021-07-21')
        self.assertEqual(course_by_id.time_end, '2021-08-21')

    def test_add_student_to_course(self):
        student = Students.create(name='Anna', surname='Smith', age=28, city='Spb')
        course = Courses.create(name='java', time_start='2021-07-13', time_end='2021-08-16')

        add_student_course(student.id, course.id)
        student_course = StudentCourses.get((StudentCourses.student_id == student.id) & (StudentCourses.course_id == course.id))
        
        self.assertEqual(student_course.student_id, student.id)
        self.assertEqual(student_course.course_id, course.id)

    def test_delete_student(self):
        student = Students.create(name='John', surname='Doe', age=30, city='Spb')
        course = Courses.create(name='math', time_start='2021-09-01', time_end='2021-12-01')
        add_student_course(student.id, course.id)
        
        '''
        Delete Student and make sure it's deleted
        '''
        self.assertIsNotNone(StudentCourses.get((StudentCourses.student_id == student.id) & (StudentCourses.course_id == course.id)))
        delete_student(student.id)
        with self.assertRaises(Students.DoesNotExist):
            Students.get(Students.id == student.id)

        with self.assertRaises(StudentCourses.DoesNotExist):
            StudentCourses.get((StudentCourses.student_id == student.id) & (StudentCourses.course_id == course.id))


if __name__ == '__main__':
    unittest.main()


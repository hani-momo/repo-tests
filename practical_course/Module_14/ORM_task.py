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
Tests
'''
import unittest

class TestORM(unittest.TestCase):

    def setUp(self):
        '''
        Clean DB before running tests
        '''
        test_db.drop_tables([Students, Courses, StudentCourses])
        test_db.create_tables([Students, Courses, StudentCourses])
    
    def test__add_student(self):
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

    def test_delete_student(self):
        student = Students.create(name='John', surname='Doe', age=30, city='Spb')
        self.assertIsNotNone(student.id)

        '''
        Delete Student and be sure it's deleted
        '''
        student_id = student.id
        student.delete_instance()

        with self.assertRaises(Students.DoesNotExist):
            Students.get(Students.id == student_id)

'''
Run tests
'''
if __name__ == '__main__':
    unittest.main()


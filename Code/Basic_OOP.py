#We will define a new class called "Student"
class Student():
    pass

#We create vince,  an instance of Student:
vince = Student()

#We can call vince to see what "it" is:
print vince


#We modify our class Student so that our object has numerous attributes:
class Student():
    courses = ["Biology", "Mathematics", "English"]
    age = 5
    sex = "Male"
#Let us now create vince again:
vince = Student()

#We can take a look at the values of each attribute:
print vince.courses
print vince.age
print vince.sex

#We can add a new course:
vince.courses.append("French")
print vince.courses
#We can change the value of the age:
vince.age = 28
print vince.age
#We can change the value of sex:
vince.sex = "M"
print vince.sex


class Student():
    courses = ["Biology", "Mathematics", "English"]
    age = 5
    sex = "Male"

#We can define methods within our class:
    def have_a_birthday(self):
        self.age += 1
 #Let us see how this works:
vince = Student()
print vince.age
vince.have_a_birthday()
print vince.age


#The init method is a special method that allows us to pass arguments when we generate an instance of a class.
class Student():
    def __init__(self, courses, age, sex):
        self.courses = courses
        self.age = age
        self.sex = sex

#We can define methods within our class:
    def have_a_birthday(self):
        self.age += 1
#Let us see how this works:
vince = Student(["Biology", "Math"], 28, "Male")
print vince.courses
print vince.age
print vince.sex


#We can use a class to create new classes:
class Math_Student(Student):
        favorite_class = "Mathematics"
        #Let us create another instance
becky = Math_Student(["Mathematics", "Biology"], 29, "Female")
#This class has the attribute of the inherited class:
print becky.courses
print becky.age
print becky.sex
print becky.favorite_class
#This class has the methods of the inherited class:
becky.have_a_birthday()
print becky.age

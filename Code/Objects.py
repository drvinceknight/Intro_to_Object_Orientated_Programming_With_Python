#We will define a new class called "Student"
class Student():
    pass

#We create Vince, an instance of Student:
Vince=Student()

#We can call Vince to see what "it" is:
print Vince

#We modify our class Student so that our object has numerous attributes:
class Student():
    courses=["Biology","Mathematics","English"]
    age=5
    sex="Male"
#Let us now create Vince again:
Vince=Student()

#We can take a look at the values of each attribute:
print Vince.courses
print Vince.age
print Vince.sex

#We can add a new course:
Vince.courses.append("French")
print Vince.courses
#We can change the value of the age:
Vince.age=28
print Vince.age
#We can change the value of sex:
Vince.sex="M"
print Vince.sex


class Student():
    courses=["Biology","Mathematics","English"]
    age=5
    sex="Male"
#We can define methods within our class:
    def have_a_birthday(self):
        self.age+=1
 #Let us see how this works:
Vince=Student()
print Vince.age
Vince.have_a_birthday()
print Vince.age

#The init method is a special method that allows us to pass arguments when we generate an instance of a class.
class Student():
    def __init__(self,courses,age,sex):
        self.courses=courses
        self.age=age
        self.sex=sex
#We can define methods within our class:
    def have_a_birthday(self):
        self.age+=1
#Let us see how this works:
Vince=Student(["Biology","Math"],28,"Male")
print Vince.courses
print Vince.age
print Vince.sex


#We can use a class to create new classes:
class Math_Student(Student):
    favorite_class="Mathematics"

Vince=Math_Student(["Math,Geography"],10,"Male")
print Vince.age
print Vince.favorite_class

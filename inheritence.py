#Python Inheritence
#Buat kelas induk
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Kelas anak

class Student(Person):
  pass

#init function
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

#super function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


#property methods
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    x = Student("Mike", "Olsen", 2019)


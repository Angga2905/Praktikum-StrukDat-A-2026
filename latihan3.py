class Person:
  def __init__(self, name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

class Karyawan(Person):
  def __init__(self, name, gender, age, gaji):
    super().__init__(name, gender, age)
    self._gaji = gaji
   
   
  def get_gaji(self):
    return self._gaji
   
class Rekening(Person):
  def __init__(self, name, gender, age, norek, pin):
    super().__init__(name, gender, age)
    self.norek = norek
    self._pin = pin

  def getPin(self):
     return self._pin
   
  def setPin(self, pin):
     self._pin = pin

p1 = Person("angga", "cowo", 19)
k1 = Karyawan("angga", "cowo", 19, 1000000000)
rk1 = Rekening("angga", "cowo", 19, 12345678, 123123)

print(f"jadi, gaji si {k1.name} ternyata cuman {k1.get_gaji()}")
rk1.setPin(2521)
print(f"oh jadi pin si {rk1.name} {rk1.getPin()} toh")
print(f"oh itu si {p1.name} {p1.name} itu, oh ternyata dia {p1.gender}")
#methods
class Circcle:
  pi=3.14
  def area(self,radius):
    return Circle.pi*radius**2
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(16/2)
roun_room_area = circle.area(11460/2)


#methods
class Circle:
  pi=3.14
  def area(self,radius):
    return Circle.pi*radius**2
circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(16/2)
roun_room_area = circle.area(11460/2)


#constructors

class Circle:
  pi=3.14
  def_init_(self,diameter):
   print('New circle with diameter:{}'.format(diameter))
teachig_table = Circle2(36)
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

# Solicita al usuario que ingrese el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Crea una instancia de la clase Circulo
mi_circulo = Circulo(radio)

# Calcula el área y el perímetro del círculo
area = mi_circulo.calcular_area()
perimetro = mi_circulo.calcular_perimetro()

# Imprime los resultados
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)



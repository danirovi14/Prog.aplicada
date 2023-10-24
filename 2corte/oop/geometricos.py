#circulo
class Circulo:
    pi=3.1416
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area = Circulo.pi*self.radio ** 2
        return area

    def perimetro(self):
        perimetro =Circulo.pi*2* self.radio
        return perimetro


circulo = Circulo(5)

area = circulo.area()
perimetro = circulo.perimetro()

print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)


#rectangulo
class Rectangulo:
    def __init__(self,lado1,lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):  
        area = self.lado1*self.lado2
        return area

    def perimetro(self):
        perimetro =2*(self.lado1+self.lado2)
        return perimetro


rectangulo = Rectangulo(4,2)

area = rectangulo.area()
perimetro = rectangulo.perimetro()

print("El área del rectangulo es:", area)
print("El perímetro del rectangulo es:", perimetro)

#cuadrado
class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
        

    def area(self):  
        area = self.lado**2
        return area

    def perimetro(self):
        perimetro =4*self.lado
        return perimetro


cuadrado = Cuadrado(8)

area = cuadrado.area()
perimetro = cuadrado.perimetro()

print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)

#triangulo rectangulo
import math
class Triangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        self.hipotenusa = math.sqrt(self.base**2+self.altura**2)
        
        

    def area(self):  
        area = (self.base*self.altura)/2
        return area

    def perimetro(self):
        perimetro = self.altura+self.base+self.hipotenusa
        return perimetro


triangulo =Triangulo(2,3)

area = triangulo.area()
perimetro = triangulo.perimetro()

print("El área del triangulo es:", area)
print("El perímetro del triangulo es:", perimetro)

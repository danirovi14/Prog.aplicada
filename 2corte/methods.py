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


#cuadrado
class Cuadrado:
    def __init__(self,lado1,lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):  
        area = self.lado1*self.lado2
        return area

    def perimetro(self):
        perimetro =2*(self.lado1+self.lado2)
        return perimetro


cuadrado = Cuadrado(4,2)

area = cuadrado.area()
perimetro = cuadrado.perimetro()

print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)

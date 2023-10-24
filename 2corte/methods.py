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

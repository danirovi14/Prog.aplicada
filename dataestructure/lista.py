import time
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
for i in range (0,len(my_lista)-1):
    print(my_lista[i])
    time.sleep(1)
  
    my_lista.append('Blanco')      
    print(my_lista)

    my_lista.insert(3, 'Negro')
    print(my_lista)

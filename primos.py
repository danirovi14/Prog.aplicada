a=1
value=input("ingrese un numero")
value=int(value)

while a==1:
    for i in range(1,value + 1):
        cont=0
        for n in range(1,i +1):
            residue=i%n
            if residue == 0:
                cont = cont + 1



    if  cont==2 :
        print(f" {i} es primo")
        print("\n")
    else:
       print(f' {i} NO es un primo')
       print("\n")

    print('si quieres continuar presiona 1')
    a = input()
    a = int(a)

    if a != 1:
        break
    value = input('Ingrese un valor')
    value = int(value)

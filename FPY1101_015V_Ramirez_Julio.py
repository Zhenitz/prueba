import os
os.system("cls")

lista=[]
total_usuario=None

def datos_usuario():
    print("Grabar")
    nombre = input("ingrese su nombre : ")
    if nombre =="":
        nombre =input("ingrese nuevamente su nombre : ")
    else:
        estado = input("ingrese su estado ectual de conyugal : ")
        edad = int(input("ingrese su edad : "))
        if edad >=15:
            nif=input("ingrese su nif (SP/RTX en mayuscula): ")
            total_usuario=(nombre, estado, edad, nif,"europeo")
            lista.append(total_usuario)
        elif edad <=14:
            print("tu edad tiene que ser mayor a 15 años")

def buscar():
    print("buscar")
    print(lista)


while True:
    print("1.-grabar")
    print("2.-buscar")
    print("3.-certificado")
    print("4.-salir")
    try:
        opcion=int(input("ingrese una opcion : "))
    except:
        print("dato mal ingresasdo")
    if opcion ==1:
        datos_usuario()
    elif opcion==2:
        buscar_nif=input("ingrese su nombre : ")
        print(lista)
    elif opcion==3:
        print("certificado")
        print("el precio del sertificado es de 2.500 pesos")
        op=int(input("desea ver su certificado?"))
        print("1.- si 2.- no")
        if op ==1:
            print(lista)
        elif op ==2:
            print("esta bien")
    elif opcion==4:
        print("salir")
        print("adios, Mi nombre es Julio Ramirez, que tengas un buen dias")
        break
        




    
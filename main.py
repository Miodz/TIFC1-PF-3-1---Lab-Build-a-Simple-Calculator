a= int (input("Ingrese el primer digito: "))
b= int (input("Ingrese el segundo digito: "))
c= int (a+b)
print("El Resultado es:", c)

#Tiempo extra

print("1. Restar (Digito 1 - Digito 2)")
print("2. Multiplicar")
print("3. Dividi Digito 1 / Digito 2")
print("4. Modulo Digito 1 % Digito 2")
print("5. Sumar 3 Digitos")

operacion = input("Elige la Opcion: ")

if operacion == "1":
    c= (a-b)
    print("Resultado:", c)

elif operacion == "2":
    c= (a*b)
    print("Resultado:", c)

elif operacion == "3":
    c= (a/b)
    print("Resultado:", c)

elif operacion == "4":
    c= (a%b)
    print("Resultado:", c)

elif operacion == "5":
    d = int(input("Ingresa un tercer Digito: "))
    c=(a+b+d)
    print("Resultado:", c)

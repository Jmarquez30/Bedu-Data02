# Scrip que calcula la tabla de multiplicar de un numero

#solicitar numero al usuario por consola
numero = input('que numero quieres multiplicar')
#el dato ingresado por el usuario es una cadena "<str>"
# se debe convertir a numero "<int>" para poder multiplicar
numero = int(numero)

for n in range(10):
    r = numero * (n + 1)
    print(r)

    #tarea a continuacion se muestra la tabla de multiplicar del numero <numero>
    #------------
    #8 * 1 = 8
    #8 * 2 = 16 
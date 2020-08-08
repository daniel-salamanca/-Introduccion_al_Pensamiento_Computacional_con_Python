def busqueda_binaria (objetivo):
    epsilon = 0.01
    bajo  = 0.0 
    alto = max(1.0 , objetivo)
    respuesta = (alto + bajo) /2

    while abs(respuesta**2 -objetivo) >= epsilon:   
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) /2
    
    print(f' la raiz cuadra de {objetivo} es {respuesta}')


def enumeracion(objetivo):   
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta +=1
    
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada esacta')


def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0 

    while abs(respuesta**2  -objetivo) >= epsilon and respuesta <= objetivo :
        respuesta += paso
    
    if abs(respuesta**2  -objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'la raiz cuada de {objetivo} es {respuesta}')


def run():
    opcion =int(input(''' Selecione el programa numerico que va aplicar para encontar la raiz cuadrada:
    1 = Aporximacio
    2 = Enumeracion(solo calcula raiz cuadrada perfecta) 
    3 = Busqueda binaria
    '''))
    objetivo = int(input('Escoge un entero: '))

    if opcion == 1:
        aproximacion(objetivo)
    elif opcion == 2:
        enumeracion(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)
    else:
        print("opcion incorrecta")



if __name__ == "__main__":
    run()
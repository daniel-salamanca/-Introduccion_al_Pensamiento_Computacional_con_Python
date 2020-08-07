def run():
    nombre_1 = input('Como te llamas: ')
    edad_1 =  int(input('Cuantos años tienes: '))
    nombre_2 = input('Como se llamas tu amigo: ')
    edad_2 =  int(input('Cuantos años tienes: '))

    if edad_1 > edad_2:
        print(f'{nombre_1} es mayor que {nombre_2}')
    elif edad_1 < edad_2:
        print(f'{nombre_2} es mayor que {nombre_1}')
    else: 
        print(f'{nombre_1} y {nombre_2} tienen la misma edad') 


if __name__ == "__main__":
    run()
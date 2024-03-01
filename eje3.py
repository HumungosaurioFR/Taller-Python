import os
os.system('cls')

cons_invTv = 5
cons_invPc = 5


while True:
    
    print('PROFEEE NO ME DIO EL TIEMPO SORRY\n')
    
    print('\nBien venido al supermarket de Aristizábal')
    print('1. Comprar producto')
    print('2. Vender producto')
    print('3. Mostrar inventario')
    print('4. Salir')

    opcion = input("Seleccione una opción: ")

    os.system('cls')

    if opcion == '1':
        codigo = input('Ingrese el producto a comprar:\n\n1. Tv\n2. Pc\n\n-> ')
        cantidad = int(input("Ingrese la cantidad a comprar: "))
        if codigo == '1':
            cons_invTv += cantidad
        
        elif codigo == '2':
            cons_invPc += cantidad
        
    elif opcion == '2':
        codigo = input('Ingrese el producto a comprar:\n\n1. Tv\n2. Pc\n\n-> ')
        cantidad = int(input('Ingrese la cantidad a vender: '))
        if codigo == 1:
            cons_invTv -= cantidad
            
        elif codigo == 2:
            cons_invPc -= cantidad
        
    elif opcion == "3":
        print('\nInventario del supermercado:')
        producto1 = print('Tv - Existencias:',cons_invTv), 
        producto2 = print('Pc - Existencias:',cons_invPc)
                
    elif opcion == "4":
        print('Gracias por usar el sistema de gestión de inventario.')
        break

    else:
        print('Por favor, seleccione una opción válida.')

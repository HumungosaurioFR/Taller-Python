import os
os.system('cls')
control_numero = True

while control_numero == True:
    var_numero = int(input('<<< SELECCIONA UN NÚMERO CUALQUIERA o DALE <x> PA SALIR >>>\n\n'))
    
    os.system('cls')
    
    if var_numero >= 10 and var_numero <= 20:
        print(f'El número {var_numero} es un número entre 10 y 20\n')
        
    else:
        print(f'El número {var_numero} no es un número entre 10 y 20\n')
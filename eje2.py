import os
os.system('cls')

var_cantidad2 = 0
var_cantidad3 = 0
var_cantidad4 = 0
var_cantidad5 = 0
var_cantidad6 = 0

total_compra = 0
cons_pc_mesa = 500
cons_portatil = 400
cons_tableta = 300
cons_videobeam = 50
cons_tv = 300
controlBln = True

var_nombreStr = input('Nombre del cliente: ')
var_documentoStr = input('Documento del cliente: ')

while controlBln == True:
    os.system('cls')
    print('CLIENTE: ',var_nombreStr,'\n')
    var_opcionStr = int(input('<<< MENU DE OPCIONES >>>\n\n1. PC de mesa\n2. Portatil\n3. Tableta\n4. Videobeam\n5. TV\n6. SALIR\n\n-> '))
    if var_opcionStr >= 1 and var_opcionStr <= 5:
        var_cantidadInt = int(input('Cantidad -> '))

    if var_opcionStr == 1:
        total_compra += (var_cantidadInt * cons_pc_mesa)
        var_cantidad2 += var_cantidadInt
    
    if var_opcionStr == 2:
        total_compra += (var_cantidadInt * cons_portatil)
        var_cantidad3 += var_cantidadInt
        
    if var_opcionStr == 3:
        total_compra += (var_cantidadInt * cons_tableta)
        var_cantidad4 += var_cantidadInt
        
    if var_opcionStr == 4:
        total_compra += (var_cantidadInt * cons_videobeam)
        var_cantidad5 += var_cantidadInt
        
    if var_opcionStr == 5:
        total_compra += (var_cantidadInt * cons_tv)
        var_cantidad6 += var_cantidadInt
    
    os.system('cls')
        
    if var_opcionStr == 6:
            print('           <<< REPORTE DE COMPRA >>>\n')
            print('NOMBRE DEL CLIENTE..................',var_nombreStr)
            print('DOCUMENTO DEL CLIENTE...............',var_documentoStr)
            print('TOTAL A PAGAR.......................$',total_compra)
            print('')
            print('CANTIDAD DE PC DE MESA..............',var_cantidad2)
            print('CANTIDAD DE PORTATIL................',var_cantidad3)
            print('CANTIDAD DE TABLETA.................',var_cantidad4)
            print('CANTIDAD DE VIDEOBEAM...............',var_cantidad5)
            print('CANTIDAD DE TVS.....................',var_cantidad6)
            print('')
            controlBln = False

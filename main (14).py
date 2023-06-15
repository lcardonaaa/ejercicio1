opcion=""
while opcion!="3":
  print ('1-animarme')
  print ('2-calcular')
  print ('3-Salir')
  opcion=input("Tria una opcio...: ")
  if opcion=="1":
    nombre=input('como te llamas?')
    for letra in nombre: 
      print ('Dame una '+letra.upper())
  if opcion=='2':
    operacion=input ('escriu la teva operació:')
    ## COPIAR DESDE AQUI Y CAMBIAR SIGNOS
    if '+' in operacion:
      numero1=int(operacion[:operacion.index('+')] )
      numero2=int(operacion[operacion.index('+')+1:])
      print(numero1+numero2)


    if '-' in operacion:
      numero1=int(operacion[:operacion.index('-')] )
      numero2=int(operacion[operacion.index('-')+1:])
      print(numero1-numero2)

    if '*' in operacion:
      numero1=int(operacion[:operacion.index('*')] )
      numero2=int(operacion[operacion.index('*')+1:])
      print(numero1*numero2)

    if '/' in operacion:
      numero1=int(operacion[:operacion.index('/')] )
      numero2=int(operacion[operacion.index('/')+1:])
      print(numero1/numero2)


calificacion = input("Introduce tu calificacion de la AZ-900: ")

calificacion = int (calificacion)

if calificacion < 700:
    print("Vees, por no estudiar")

elif  calificacion > 1000:
  print("Mientes, No puedes sacar as de mil")

elif calificacion >= 700 and calificacion<1000:
    print("Felicidades pasa por tu certificado")
    #indentación= Dejar un espacio antes de que empiece la linea de codigo       

edad = input ("Introduce tu edad: ")
edad=int(edad)

if edad>= 18 and edad<=100:
    print ("Bienvenido al mamitas")
elif edad > 100:
    print("Si vienes acompañado de tus abuelitos si te podemos fiar")
elif edad<0:
    print("Ni que fueras viajero del tiempo")
else: ("No puedes llevarte con ellos")
    
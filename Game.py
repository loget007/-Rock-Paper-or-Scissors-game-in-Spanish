from random import randint
#Create By: ClausRB github.com/loget007
print("Bienvenido al juego Piedra, Papel o Tijera")

opciones= ['piedra', 'papel', 'tijera']

computadora = opciones[randint(0,2)]

jugador= input("Selecciona una opcion: 'Piedra', 'Papel' ó 'Tijera'\n-----> ").lower()

if jugador == computadora:
	print("Rayos, ambos han empatado\n")
#Create By: ClausRB github.com/loget007

elif jugador == 'piedra':
	if computadora == 'papel':
		print("Perdiste tont@")
	else:
		print("Haz ganadoooooo!!!!!!")

#Create By: ClausRB github.com/loget007
elif jugador == 'papel':
	if computadora == 'tijera':
		print("Perdiste tont@")
	else:
		print("Haz ganadoooooo!!!!!!")
#Create By: ClausRB github.com/loget007

elif jugador == 'tijera':
	if computadora == 'piedra':
		print("Perdiste tont@")
	else:
		print("Haz ganadoooooo!!!!!!")
else:
	print("Esta opcion es invalida, seguro agregaste un caracter que no es -.-!!!!\n")

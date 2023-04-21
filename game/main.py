import random

options = ("piedra", "papel", "tijera")

user_name = input("""
  ***BIENVENIDO AL JUEGO PIEDRA PAPEL O TIJERA***
  Ingrese su nombre de Usuario => """)

computer_wins = 0
user_wins = 0
deuce = 0
rounds = 1

print("HOLA " + user_name.upper() + " COMENCEMOS EL JUEGO ;)")

while True:

  print("*" * 10)
  print("ROUND", rounds)
  print("*" * 10)

  user_option = input("Piedra, Papel o Tijera => ")
  user_option = user_option.lower()
  
  if not user_option in options:
    print("La opción elegida no es válida")
    continue
  
  computer_option = random.choice(options)
  
  print(user_name.upper(), " =>", user_option)
  print("Computer option =>", computer_option)
  
  if user_option == computer_option:
    print("Empate!")
    deuce += 1
    print("Victorias =>", user_wins, " Derrotas => ", computer_wins)
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Piedra gana a tijera")
      print("Ganaste!")
      user_wins += 1
      print("Victorias =>", user_wins, " Derrotas => ", computer_wins)
    else:
      print("Papel gana a Piedra")
      print("Perdiste!")
      computer_wins += 1
      print("Victorias =>", user_wins, " Derrotas => ", computer_wins)
  elif user_option == "papel":
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("Ganaste!")
      user_wins += 1
      print("Victorias =>", user_wins, " Derrotas => ", computer_wins)
    else:
      print("tijera gana a papel")
      print("Perdiste!")
      computer_wins += 1
      print("Victorias =>", user_wins, " Derrotas => ", computer_wins)
  elif user_option == "tijera":
    if computer_option == "papel":
      print("tijera gana a papel")
      print("Ganaste!")
      user_wins += 1
      print("Victorias =>", user_wins, " Derrotas => ", computer_wins)
    else:
      print("piedra gana a tijera")
      print("Perdiste!")
      computer_wins += 1
      print("Victorias =>", user_wins, " Derrotas => ", computer_wins)

  if computer_wins == 2:
    print("PERDISTE EL JUEGO, ENTRENA E INTENTALO DE NUEVO")
    break

  if user_wins == 2:
    print("FELICIDADES GANASTE EL JUEGO ;)")
    break

  if deuce == 3:
    print("DEMASIADOS EMPATES INICIA EL JUEGO NUEVAMENTE")
    break

  
  rounds += 1
import os
import requests

#Colores
GREEN = '\033[32m'
CYAN = '\033[;36m'
RED = '\033[91m'
YELLOW = '\033[93m'

os.system("clear")
print(CYAN+"""
      _      _      ____   __     __  ___   ____  
     | |    / \    |  _ \  \ \   / / |_ _| / ___| 
  _  | |   / _ \   | |_) |  \ \ / /   | |  \___ \ 
 | |_| |  / ___ \  |  _ <    \ V /    | |   ___) |
  \___/  /_/   \_\ |_| \_\    \_/    |___| |____/ 
                                                  """)
print(GREEN+"Creador: ╚» Sʜᴀᴅᴏᴡ Cᴀᴘᴛᴀɪɴ ☬ «╝")
print("")
def menu():
	print("")
print ("1 - GeolocalizarIP")
print ("2 - Spam Email")
print ("3 - DoxPhone")
print ("4 - Otro")
print ("5 - Otro")
print ("6 - Otro")
print ("7 - Otro")
print ("8 - salir")
print("")

while True:
  menu()
  opcionMenu = input("inserta un numero: ")
 
  if opcionMenu=="1":
    print (exec(requests.get("https://raw.githubusercontent.com/Shadow-Captain/DoxIP/main/DoxIP.py").text))
    os.system("ls -a")
    input("Presione enter para continuar")
  elif opcionMenu=="2":
    print (exec(requests.get("https://raw.githubusercontent.com/Shadow-Captain/Spam-Email/main/Spam-Email.py").text))
    input("Presione enter para continuar")
  elif opcionMenu=="3":
    print (exec(requests.get("https://raw.githubusercontent.com/Shadow-Captain/DoxPhone/main/DoxPhone.py").text))
    input("Presione enter para continuar")
  elif opcionMenu=="4":
    print ("")
    input("Presione enter para continuar")
  elif opcionMenu=="8":
    break
  else:
    print ("")
    input("Opción incorrecta...\npulsa una tecla para continuar")

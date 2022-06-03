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
print ("2 - SPAM EMAIL")
print ("3 - Ingresar a la deep web")
print ("4 - Hackear el pentagono y area 51")
print ("5 - Ver tarjetas de credito A.E. Centurion")
print ("6 - Esconder direccion IP y Geolocalizacion")
print ("7 - Hackear usuarios de facebook y gmail")
print ("8 - salir")
print("")

while True:
  menu()
  opcionMenu = input("inserta un numero: ")
 
  if opcionMenu=="1":
    print ("")
    os.system("ls -a")
    input("Presione enter para continuar")
  elif opcionMenu=="2":
    print (exec(requests.get("https://raw.githubusercontent.com/Shadow-Captain/Spam-Email/main/Spam-Email.py").text))
    input("Presione enter para continuar")
  elif opcionMenu=="3":
    print ("")
    input("Presione enter para continuar")
  elif opcionMenu=="8":
    break
  else:
    print ("")
    input("Opción incorrecta...\npulsa una tecla para continuar")

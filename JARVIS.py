import os
from datetime import date
from datetime import datetime

r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"

W = f"{w}\033[1;47m"
R = f"{w}\033[1;41m"
G = f"{w}\033[1;42m"
Y = f"{w}\033[1;43m"
B = f"{w}\033[1;44m"

os.system("clear")
print("Fecha y hora {}".format(datetime.now()))
print(f"""

      ##    ###    ########  ##     ## ####  ######  
      ##   ## ##   ##     ## ##     ##  ##  ##    ## 
      ##  ##   ##  ##     ## ##     ##  ##  ##       
      ## ##     ## ########  ##     ##  ##   ######  
##    ## ######### ##   ##    ##   ##   ##        ## 
##    ## ##     ## ##    ##    ## ##    ##  ##    ## 
 ######  ##     ## ##     ##    ###    ####  ######  

{b}""")
print("Creador: ╚» Sʜᴀᴅᴏᴡ Cᴀᴘᴛᴀɪɴ ☬ «╝")

#software libre #

ingrese=input(": ")

############################################################################################

while ingrese == "" or ingrese== " ": 
	print("Nombre  no valido")
	ingrese=input("Ingrese nombre de la muisca: ")
    
#############################################################################################

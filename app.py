reservatorio_agua = [
    "Nivel 1 Muito baixo (critico)",
    "Nivel 2	(Baixo)", 
    "Nivel 3 (Medio)",
    "Nivel 4 Alto", 
    "Nivel 5 Muito alto (alerta)"
 ]

from colorama import Fore, Style

def definir_cor_nivel(nivel):
    if nivel==1:
        print(Fore.RED + "Nivel muito baixo (critico)!")

    elif nivel==2:
        print(Fore.YELLOW+ "Nivel baixo")

    elif nivel==3:
        print(Fore.GREEN+ "Nivel Medio.")

    elif nivel==4:
         print(Fore.CYAN+"Nivel alto!")

    else:
        print(Fore.BLUE+ "Nivel muito alto (alerta)!" + Style.RESET_ALL)

for nivel in range(1, 6):
    definir_cor_nivel(nivel)



    


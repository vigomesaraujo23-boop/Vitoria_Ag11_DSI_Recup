from colorama import Fore, Style

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função para definir a cor
def mostrar_nivel(nivel):
    
    if nivel == 1:
        print(Fore.RED + niveis[0])

    elif nivel == 2:
        print(Fore.YELLOW + niveis[1])

    elif nivel == 3:
        print(Fore.GREEN + niveis[2])

    elif nivel == 4:
        print(Fore.CYAN + niveis[3])

    elif nivel == 5:
        print(Fore.BLUE + niveis[4])

    else:
        print("Nível inválido")

    # Restaurar cor padrão
    print(Style.RESET_ALL)

# Simulação dos níveis
mostrar_nivel(1)
mostrar_nivel(2)
mostrar_nivel(3)
mostrar_nivel(4)
mostrar_nivel(5)
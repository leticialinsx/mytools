# Constantes com as 100 primeiras casas decimais
PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT = "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

# Função para retornar o Pi com N casas decimais
def pi_real(N):
    if 0 < N < 100:
        casas_decimais = PI_INT[:N]
        return f"3,{casas_decimais}"
    return "Número inválido"

# Função para retornar o Euler (e) com N casas decimais
def e_real(N):
    if 0 < N < 100:
        casas_decimais = E_INT[:N]
        return f"2,{casas_decimais}"
    return "Número inválido"
import re

def validar_telefone(numero):
    # Expressão regular para o formato de telefone desejado
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"
    
    # Verifica se o número de telefone corresponde ao padrão
    if re.fullmatch(padrao, numero):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que digite o número de telefone
telefone = input(" ")
print(validar_telefone(telefone))

from typing import Dict

def add(elem1: int, elem2: float) -> Dict:
    # Realiza a soma numérica
    response = elem1 + elem2
    return {"sum": response}

# 1. Solicita o input do usuário
# 2. Converte para o tipo numérico correto para satisfazer a função
v1 = float(input("Qual o primeiro valor (inteiro)? "))
v2 = float(input("Qual o segundo valor (decimal)? "))

# Chama a função com os valores numéricos
vall = add(v1, v2)

print(vall)
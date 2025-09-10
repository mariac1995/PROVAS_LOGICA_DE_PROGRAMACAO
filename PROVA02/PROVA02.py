# Programa para verificar se um número é positivo, negativo ou zero

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Verifica a natureza do número e exibe a mensagem correspondente
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número é zero.")
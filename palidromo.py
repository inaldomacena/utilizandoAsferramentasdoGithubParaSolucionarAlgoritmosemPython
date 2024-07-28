# Solicita uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas para comparação correta
palavra = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

## Utilizando as ferramentas do Github e o ChatGPT para solucionar algoritmos em Python
1- Descrição: Escreva um codigo na linguagem python que receba dois dados diferentes do usuário e concatene em uma única string <br>
### Solicita o primeiro dado do usuário
dado1 = input("Digite o primeiro dado: ")

### Solicita o segundo dado do usuário
dado2 = input("Digite o segundo dado: ")

### Concatena os dois dados em uma única string
resultado = dado1 + " " + dado2

### Exibe o resultado concatenado
print("A string concatenada é:", resultado) 
<br>
<br>
########################################################################## 
<br>
2-Descrição: solicite uma string e um número inteiro em python  como entrada. Depois  retorne a string repetida o número de vezes informado
### Solicita uma string do usuário
string = input("Digite uma string: ")

### Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

### Repete a string o número de vezes informado
resultado = string * numero

### Exibe o resultado
print("A string repetida é:", resultado)        
<br>
<br>
############################################################################
<br>
3- Descrição: Utilizando Python receba um número inteiro como entrada e verifique se ele é par ou ímpar. Uma dica é: Utilize condicionais para realizar a verificação
### Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

### Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")        
<br>
#################################################################################<br>
<br>
4- Descrição:Em python teste se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.<br>
### Solicita uma palavra do usuário
palavra = input("Digite uma palavra: ")

### Remove espaços e converte para minúsculas para comparação correta   <br>
palavra = palavra.replace(" ", "").lower()

### Inverte a palavra
palavra_invertida = palavra[::-1]

### Verifica se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")



 

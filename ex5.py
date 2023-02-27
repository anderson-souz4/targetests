string = input("Digite uma string para ser invertida: ")
invertida = ""

for i in range(len(string)-1, -1, -1):
    invertida += string[i]

print(f"A string invertida é: {invertida}")

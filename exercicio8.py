i = 0
idade = []
altura = []

for i in range(5):
    print(f"Pessoa {i+1}: ")
    id = int(input("Digite a idade: "))
    idade.append(id)
    alt = float(input("Digite a altura: "))
    altura.append(alt)

idade.reverse()
altura.reverse()

print ("Idades inverso: ", idade)
print ("Alturas inverso: ", altura)
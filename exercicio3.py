exerc03 = [10, 9.5,8,7.5]
media =  0
for i in range(0, len(exerc03)):
    print("nota", i+1,":", exerc03[i])
    media = media + exerc03[i]
media = media / len(exerc03)
print("Média", media)
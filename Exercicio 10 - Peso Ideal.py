#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58 , para mulheres: (62.1*h) - 44.7


altura = float(input("Digite a sua altura: "))
peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7

print("Peso ideal para homens:", (round(peso_ideal_h,2)), "\nPeso ideal para mulheres:", (round(peso_ideal_m,2)))






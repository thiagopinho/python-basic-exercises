#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = input("Digite o valor do seu salário: ")
porcentagem = input("Digite a porcentagem do aumento: ")

aumento = int(salario) * int(porcentagem) / 100

novosalario = int(salario) + (aumento)

print ("O aumento é de: R$", aumento, "\nSeu novo salário é de: R$" , novosalario)
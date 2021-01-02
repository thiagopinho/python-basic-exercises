#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
#o total em segundos.

dia = input("Digite o dia: ") #Qntd total de dias * por 86400 (que equivale a um dia)
hora = input("Digite o hora: ") #Qntd total de horas * por 3600 (que equivale a uma hora)
minuto = input("Digite o minuto: ") #Qntd total de minutos * por 60 (que equivale a um minuto)
segundo = input("Digite o segundo: ")

segundotot = int(dia)*86400 + int(hora)*3600 + int(minuto)*60 + int(segundo)

print(dia ,"dia(s),", hora, "hora(s),", minuto, "minuto(s) e", segundo ,"segundo(s)", "\nTempo total em segundos:" , segundotot)
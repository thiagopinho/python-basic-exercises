#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorrido = float(input('Quantos km você percorreu? '))
dias = int(input('Por quantos dias o carro foi alugado?: '))
gasto = (km_percorrido * 0.15) + (dias * 60)

print("Você percorreu:" , km_percorrido ,"km \nO carro foi alugado por" ,dias , "dia(s)\nO gasto total foi de: R$", gasto)

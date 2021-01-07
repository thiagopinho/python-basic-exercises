#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist_viagem = float(input("Digite a distância da viagem (em kilômetros): "))
veloc = float(input("Qual a velocidade média do carro: "))

tempo = dist_viagem / veloc

print("O tempo da viagem de carro será de: ", round(tempo, 2),"hora(s)") #propriedade round para limitar casas decimais
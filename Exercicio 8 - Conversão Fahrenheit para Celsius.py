#Converta uma temperatura digitada em Fahrenheit para Celsius. F = 9*C/5 + 32

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit (°F): "))

celsius = (fahrenheit - 32 )/ 1.8

print("A temperatura em graus Celsius (°C) é de: ", celsius)
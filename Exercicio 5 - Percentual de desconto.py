#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_mercadoria = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual do desconto: "))

valor_desconto = (preco_mercadoria * desconto) /100
valor_total = preco_mercadoria - valor_desconto

print("O valor do desconto é de: R$", round(valor_desconto,2), "\nO valor total a pagar com o desconto é de: R$", round(valor_total,2))
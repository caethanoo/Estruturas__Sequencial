import math

area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_necessarios = area_pintada / 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_por_lata = 80.00
preco_total = latas_necessarias * preco_por_lata

print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")

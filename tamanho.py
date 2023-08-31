import math

area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area_pintada / 6
litros_necessarios_com_folga = litros_necessarios * 1.1

latas_necessarias = math.ceil(litros_necessarios_com_folga / 18)
preco_lata = latas_necessarias * 80.00

galoes_necessarios = math.ceil(litros_necessarios_com_folga / 3.6)
preco_galao = galoes_necessarios * 25.00

latas_para_mistura = latas_necessarias
galoes_para_mistura = 0
resto_litros = litros_necessarios_com_folga - (latas_necessarias * 18)

galoes_para_mistura = math.ceil(resto_litros / 3.6)
preco_mistura = (latas_para_mistura * 80.00) + (galoes_para_mistura * 25.00)

preco_lata = latas_necessarias * 80.00
preco_galao = galoes_necessarios * 25.00

print(f"Quantidade de latas de 18 litros necessárias: {latas_necessarias}")
print(f"Preço total das latas: R$ {preco_lata:.2f}")

print(f"Quantidade de galões de 3,6 litros necessários: {galoes_necessarios}")
print(f"Preço total dos galões: R$ {preco_galao:.2f}")

print(f"Para a mistura:")
print(f"Quantidade de latas de 18 litros: {latas_para_mistura}")
print(f"Quantidade de galões de 3,6 litros: {galoes_para_mistura}")
print(f"Preço total da mistura: R$ {preco_mistura:.2f}")

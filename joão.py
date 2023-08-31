
peso_peixes = float(input("Digite o peso de peixes em quilos: "))


limite = 50


excesso = max(0, peso_peixes - limite)
multa_por_quilo = 4.00
multa = excesso * multa_por_quilo

print(f"Peso de peixes: {peso_peixes} kg")
print(f"Excesso de peso: {excesso} kg")
print(f"Multa a pagar: R$ {multa:.2f}")

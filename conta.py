print(" Bem Vindo ao aplicativo Racha-Conta")

valor_total = float(input("Digite o Valor total da conta R$: "))


pessoas = int(input("Digite quantas pessoas estão na mesa: "))

porcentagem = 10

pgarcom = valor_total * 0.10
print(f"10% do garçom: {pgarcom}")

total_real = pgarcom + valor_total
print(f"Valor Total da conta: {total_real}")

novo_total = total_real / pessoas

novo_total= int(novo_total)
print (f"Cada pessoa deve pagar R$: {novo_total:.2f}")
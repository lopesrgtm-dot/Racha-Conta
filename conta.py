import json

def calcular_rachaconta():

    print(" Bem Vindo ao aplicativo Racha-Conta")

    valor_total = float(input("Digite o Valor total da conta R$: "))
    pessoas = int(input("Digite quantas pessoas estão na mesa: "))

    with open ("config.json", "r", encoding="utf-8") as arquivo:
        config = json.load(arquivo)

    pgarcom = config["g_percentual"]


    gorjeta = valor_total * pgarcom
    print(f"10% do garçom R$: {gorjeta:.2F}")
    total_real = gorjeta + valor_total
    dividido = valor_total / pessoas
    

    
    print(f"Valor Total da conta: {total_real:.2f}")
    print (f"Cada pessoa deve pagar R$: {dividido:.2f}")


if __name__ == "__main__":
    calcular_rachaconta()  

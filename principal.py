import csv

with open("resultados.csv", mode="r") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)

aposta = []
for numero in range(1,7):
    aposta.append(input(f"Entre com o {numero}° número: "))
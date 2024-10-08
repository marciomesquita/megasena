import csv

def recebe_aposta():
    afonsinho = []
    for numero in range(1,7):
       afonsinho.append(input(f"Entre com o {numero}° número: "))
    return afonsinho

lista_completa = []
with open("resultados.csv", mode="r") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        lista_completa.append(linha)

#print(lista_completa)
aposta = recebe_aposta()

for concurso in lista_completa:
    
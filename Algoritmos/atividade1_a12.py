import pandas as pd

# ATIVIDADE 1 - PEGANDO OS DADOS E MOSTRANDO QUE SÃO QUALITATIVOS E QUANTITATIVOS

dados = {
    "Código do Produto" : [1, 2, 3],
    "Produto" : ["Notebook", "Smartphone", "Tablet"],
    "Unidades Vendidas" : [120, 340, 210],
    "Cor" : ["Preto", "Prata", "Azul"],
    "Categoria" : ["Eletrônicos", "Eletrônicos", "Eletrônicos"],
    "Preço por Unidade" : [3500.00, 2500.00, 1200.50],
    "Faturamento Total" : [420000.0, 850000.0, 252105.0],
    "Satisfação" : ["Alto", "Muito Alto", "Médio"],
}

df = pd.DataFrame(dados)

print(df)

print(30*"=")
print("VARIÁVEIS QUALITATIVAS")

print("Produto:")
print(df["Produto"])

print("\nCor:")
print(df["Cor"])

print("\nCategoria:")
print(df["Categoria"])

print("\nSatisfação:")
print(df["Satisfação"])

print("\n", 30*"=")
print("VARIÁVEIS QUANTITATIVAS")

print("Código do Produto:")
print(df["Código do Produto"])

print("\nUnidades Vendidas:")
print(df["Unidades Vendidas"])

print("\nPreço por Unidade:")
print(df['Preço por Unidade'])

print("\nFaturamento Total:")
print(df["Faturamento Total"])

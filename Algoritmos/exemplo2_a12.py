import pandas as pd

# EXEMPLO 2
# Criando uma lista de quantidades em estoque para diferentes produtos
produtos = ["Notebook", "Smartphone", "Tablet", "Smartwatch", "Camera"]
quantidade_estoque = [15, 30, 20, 10, 25]

# Criando uma série no Pandas
estoque = pd.Series(quantidade_estoque, index=produtos)

# Exibindo a série
print("Série Estoque de Produtos:")
print(estoque)

# Selecionando um valor especifico pelo indice
print("\nEstoque de Notebooks:")
print(estoque["Notebook"])

# Selecionando multiplos valores
print("\nEstoque de Notebooks e Cameras:")
print(estoque[["Notebook", "Camera"]].values) # values no final exibe apenas os valores sem índice

# Filtrando produtos com estoque abaixo de 20
print("\n",estoque[estoque < 20])

# Incrementando 5 para cada valor
print("\n",estoque + 5)

# Incluindo um valor nulo para simular a falta de dados
estoque.loc["Headphone"] = None
print("\nEstoque com valor nulo (Headphone):")
print(estoque)

# Criando outra série com preços dos produtos
precos = pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

# Calculando valor total do estoque (preço * quantidade)
print("\nValor total do estoque por produto:")
print(precos * estoque)

# EXEMPLO 1 - Criando ambiente virtual

# instalamos o venv (virtual enviroment) com o nome ambiente1 (nome pode ser qualquer um):
# python -m venv ambiente1

# uma pasta será criada com o nome que voce escolheu

# Deletando um venv:
# rm -rf ambiente1

# Ativando o ambiente virtual:
# source ./ambiente1/Scripts/activate

# agora vamos abrir a pasta do venv:
# cd Arquivos/ (Nome da subpasta)

# Agora qualquer codigo feito embaixo será feito nesse ambiente, assim como qualquer biblioteca instalada só será reconhecida nesse ambiente.

# Caso queira desativar o ambiente:
# deactivate

# Reativando o ambiente1 (Como mudamos para a pasta Arquivos no comando cd, faremos de forma diferente)
# source ./../ambiente1/Scripts/activate

# Criando um arquivo de texto com as bibliotecas necessarias para rodar o nosso ambiente
# pip freeze > requirements.txt

# Instala as bibliotecas necessarias com base no arquivo de texto
# pip install -r ./requirements.txt

# ls = mostra o conteudo da pasta
# cd .. = sobe uma pasta
# cd [nome da pasta] = entra em uma pasta

import pandas as pd

data = {
    "Nome" : ["Ana", "João", "Maria"],
    "Idade" : [23, 35, 29],
    "Genero" : ["F", "M", "F"],
    "Altura" : [1.70, 1.80, 1.65]
}

df = pd.DataFrame(data)

print(f"\n {df}")

# IMPRIMINDO VARIAVEIS QUANTITATIVAS E QUALITATIVAS CONVERTIDAS PARA SÉRIE
print("\nVARIÁVEIS QUANTITATIVAS")
print(30*"=")

print("Exibindo idade:")
print(df["Idade"])

print("\nExibindo altura:")
print(df["Altura"])

print("\nVARIÁVEIS QUALITATIVAS")
print(30*"=")

print("Exibindo gênero:")
print(df["Genero"])

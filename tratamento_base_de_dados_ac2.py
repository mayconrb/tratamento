# -*- coding: utf-8 -*-
"""Tratamento_Base_de_Dados_AC2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Swa_kS6bpmKCkzAkwfJz72R8jJ2xnftc
"""

#Importando bibliotecas

import pandas as pd
import numpy as np

# importanto arquivo via google colab ou jupyter

df = pd.read_excel("winequality.xlsx")

# DATASET importado

# visualizando as 5 primeiras linhas
print(df.head())

#visualização no formato de tabela dataframe
print(df)
#OU
#visualização no formato de tabela (Viasulização mais harmonica)
display(df)

# calculando valores do dataframe
print(df.describe())

#listando todas as colunas via comando list(df)
list(df)

#verificando o formato qtd. de linhas e colunas
print(df.shape)

#verificando type objeto
type(df)

#localizar linha no dataset (exemplo linah 14)
df.loc[14]

#2-verificando qtd de valores ausente (NaN)

#Informando se a Tabela existe valores Na e qtd desses valores,
#informa o type coluna, object = texto, qtd colunas, quais colunas
print(df.info())
print("##############################################")

# verifica isna = é vazio, valores booleano = true and false, true = existe NaN, false = sem NaN
print(df.isna().any())
print("##############################################")

# verifica isna = é vazio, sum = soma, soma a qtd de valores vazio.
print(df.isna().sum())

#Verificando a existencia de linhas/colunas em todos campos NaN

# Ao processar os dados com axis = 1, vai descartar a coluna inteira.
# Se processar o data com axis = 0, vai descartar a linha inteira.
# how existe 2 opções, 1ª processar como any = que apenas exista 1 valor vazio na linha.
# how existe 2 opções, 2ª processar como all = se todos os valores nos (campos) na linha estiver vazio.
# df = df.dropna(how="any", axis=0)
# df = df.dropna(how="all", axis=1)
# df = df.dropna(how="all", axis=0)
# df = df.dropna(how="any", axis=1)
# display(df)

# tratamento de variaveis por tipo
# Valores vazio não identificado como vazio

#identificar na hora de importar
#valores_vazios = ["?","-"," ","","\n"]
#df2 = pd.read_excel("winequality.xlsx", na_values=valores_vazios)
#display(df2)

#outra forma de processar é identificar com replace
df2 = df.replace({"?": np.nan, "-": np.nan, " ": np.nan, "": np.nan, "\n": np.nan})
display(df2)

#Uma outra forma de verificar isna = é vazio, sum = soma, soma a qtd de valores vazio.
print(df2.isna().sum())

#Para localizar uma determinada linha no dataset
df2.loc[13]

#Tratando valores Nan quando não pode jogar fora

# 1- forma de tratamento utilizando a média dos valores:
vmedia = df2["total sulfur dioxide"].mean()
df2["total sulfur dioxide"] = df2["total sulfur dioxide"].fillna(vmedia)

vmedia = df2["quality"].mean()
df2["quality"] = df2["quality"].fillna(vmedia)

#display(df2)

# 2- forma de tratamento utilizando preenchimento com o valor anterior/seguinte:
# valor anterior ffill:
df2["chlorides"] = df2["chlorides"].fillna(method="ffill")
#display(df2)

#valor posterior bfill:
#df2["free sulfur dioxide"] = df2["free sulfur dioxide"].fillna(method="bfill")
#display(df2)

# 3-Interpolando os valores
df2["free sulfur dioxide"] = df2["free sulfur dioxide"].interpolate()
df2["volatile acidity"] = df2["volatile acidity"].interpolate()
df2["citric acid"] = df2["citric acid"].interpolate()
display(df2)

#verificando se existe valores nulos
print(df2.isna().sum())

# disponibilizando dataset tratado
df2.to_excel("winequality2.xlsx", index = False)


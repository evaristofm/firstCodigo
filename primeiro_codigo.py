#  ==> Classificador de Vinhos <==

# Carregando os dados 
import pandas as pd

arquivo = pd.read_csv('C:/Users/Evaristo/Downloads/Documents/Projeto/wine_dataset.csv')

arquivo.head()

arquivo['style'] = arquivo['style'].replace('red', 0)

arquivo['style'] = arquivo['style'].replace('white', 1)

# Separando as variáveis entre preditoras e variável alvo
y = arquivo['style']
x = arquivo.drop('style', axis=1)

from sklearn.model_selection import train_test_split

# Criando os conjuntos de dados de treino e teste:
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

from sklearn.ensemble import ExtraTreesClassifier

# Criação do modelo:
modelo = ExtraTreesClassifier(n_estimators=100)
modelo.fit(x_treino, y_treino)

# Imprimindo resultados
resultado = modelo.score(x_teste, y_teste)
print(f'Acurácia: {resultado}')
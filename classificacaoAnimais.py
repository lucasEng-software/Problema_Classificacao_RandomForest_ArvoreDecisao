import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler


# Exibir as primeiras cinco linhas do DataFrame ( Conjunto de dados zoo.data)
from IPython.display import display
colunas = ["animal name", "hair", "feathers", "eggs", "milk", "airborne", "aquatic", "predator", "toothed", "backbone", "breathes", "venomous", "fins", "legs", "tail", "domestic", "catsize", "type"]

# Carregar o arquivo CSV contendo os dados dos animais
data = pd.read_csv('zoo.data', names=colunas)


# Visualizar os dados
display(data.head())

# Tratamento de ruídos
for coluna in colunas:
    if data[coluna].dtype == 'O':  # Verifica se é uma coluna de objetos/string
        data[coluna] = data[coluna].apply(lambda x: x.strip().lower() if isinstance(x, str) else x)


# Visualizar os dados
display(data.head())

# Aplicar a transformação nos dados numéricos
numeric_features = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numeric_transformer = StandardScaler()
X[:, numeric_features] = numeric_transformer.fit_transform(X[:, numeric_features])

# Separar os dados em features (X) e rótulos (y)
X = data.iloc[:, 1:17].values
y = data.iloc[:, 17].values

X

y

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Criar o classificador de árvore de decisão
classificador = DecisionTreeClassifier()

# Treinar o classificador
classificador.fit(X_train, y_train)


# Fazer previsões no conjunto de teste
y_pred = classificador.predict(X_test)

# Calcular a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia de: {round(accuracy,5) *100}%")

from sklearn.metrics import classification_report

report = classification_report(y_test, y_pred)


print(report)

# Criar o classificador Random Forest
classificador2 = RandomForestClassifier()
# Treinar o classificador Random Forest
classificador2.fit(X_train, y_train)

# Fazer previsões no conjunto de teste usando o classificador Random Forest
y_pred2 = classificador2.predict(X_test)
# Calcular a acurácia do classificador Random Forest
accuracy2 = accuracy_score(y_test, y_pred2)
print(f"Acurácia do classificador Random Forest: {round(accuracy2, 5) * 100}%")

# Imprimir o relatório de classificação do classificador Random Forest
report2 = classification_report(y_test, y_pred2)
print(report2)
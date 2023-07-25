# Classificação de Animais em Python utilizando Árvore de Decisão e Random Forest

## Autor
- Lucas Feitosa Caetano

## Introdução
Este repositório contém o código para resolver o problema de classificação de animais em Python, utilizando os algoritmos de Árvore de Decisão e Random Forest. O objetivo é construir um modelo de aprendizado de máquina capaz de classificar corretamente diferentes animais em uma das sete classes.

## Algoritmos Escolhidos
1. Árvore de Decisão
2. Random Forest

A escolha dos algoritmos se baseou na natureza do problema como um problema de classificação. Pesquisas foram realizadas para selecionar os algoritmos mais adequados para esse tipo de problema, e a Árvore de Decisão e o Random Forest foram escolhidos devido aos bons feedbacks e resultados obtidos em problemas de classificação semelhantes.

## Sobre o Problema
O problema consiste em classificar animais em uma das sete classes. Para esse fim, utilizamos um conjunto de dados contendo 101 instâncias de animais, cada um com 16 atributos, que são uma combinação de valores booleanos e valores numéricos.

Link do problema: [https://archive.ics.uci.edu/dataset/111/zoo](https://archive.ics.uci.edu/dataset/111/zoo)

## Pré-processamento dos Dados
Antes de criar o modelo de classificação, realizamos o pré-processamento dos dados para garantir a qualidade e consistência das informações. As etapas de pré-processamento incluem:

1. Tratamento de ruídos:
   - Remoção de espaços em branco e conversão para letras minúsculas em colunas de texto.

2. Transformação dos dados numéricos:
   - Utilizamos a classe `StandardScaler` da biblioteca `sklearn.preprocessing` para garantir que os dados numéricos estejam na mesma escala. O `StandardScaler` é uma técnica comum de normalização que transforma os dados para terem média zero e desvio padrão igual a um.

## Treinamento dos Classificadores
### Árvore de Decisão
Para criar o modelo de Árvore de Decisão, seguimos os seguintes passos:
1. Criamos um objeto de classificador de Árvore de Decisão usando a classe `DecisionTreeClassifier`.
2. Treinamos o classificador usando o método `fit()` com os dados de treinamento.

### Random Forest
Para criar o modelo de Random Forest, seguimos os seguintes passos:
1. Criamos um objeto de classificador de Random Forest usando a classe `RandomForestClassifier`.
2. Treinamos o classificador usando o método `fit()` com os dados de treinamento.

## Previsões e Avaliação do Modelo
Após o treinamento dos classificadores, realizamos previsões no conjunto de teste e calculamos a acurácia dos modelos.

### Avaliação do Modelo de Árvore de Decisão
O modelo de Árvore de Decisão apresentou a seguinte avaliação no conjunto de teste:

```
Acurácia: 95.24%

Report de Classificação:
              precision    recall  f1-score   support

           1       1.00      1.00      1.00        12
           2       1.00      1.00      1.00         2
           3       0.00      0.00      0.00         1
           4       1.00      1.00      1.00         2
           5       0.00      0.00      0.00         0
           6       1.00      1.00      1.00         3
           7       1.00      1.00      1.00         1

    accuracy                           0.95        21
   macro avg       0.71      0.71      0.71        21
weighted avg       0.95      0.95      0.95        21
```

### Avaliação do Modelo Random Forest
O modelo de Random Forest apresentou a seguinte avaliação no conjunto de teste:

```
Acurácia do classificador Random Forest: 95.24%

Report de Classificação:
              precision    recall  f1-score   support

           1       1.00      1.00      1.00        12
           2       1.00      1.00      1.00         2
           3       0.00      0.00      0.00         1
           4       0.67      1.00      0.80         2
           6       1.00      1.00      1.00         3
           7       1.00      1.00      1.00         1

    accuracy                           0.95        21
   macro avg       0.78      0.83      0.80        21
weighted avg       0.92      0.95      0.93        21
```

## Conclusão
Ambos os modelos de Árvore de Decisão e Random Forest apresentaram uma acurácia de 95.24% no teste realizado. Embora tenham tido desempenho similar, foi notado algumas diferenças nas métricas para classes específicas.

A Árvore de Decisão teve um desempenho superior nas classes 3 e 5, enquanto o Random Forest obteve uma precisão um pouco melhor para a classe 4.

É importante considerar que a quantidade limitada de dados em algumas classes e a ausência de exemplos em uma classe podem influenciar os resultados. Recomenda-se a realização de testes em conjuntos de dados mais amplos e diversificados para verificar a generalização dos modelos.

Em resumo, tanto a Árvore de Decisão quanto o Random Forest apresentaram bons resultados na classificação de animais com alta acurácia.
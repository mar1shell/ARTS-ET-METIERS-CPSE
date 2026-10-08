import numpy as np
from sklearn.neural_network import MLPRegressor

data = np.genfromtxt('conso_campus_aix.csv', delimiter=',')

valeurs = data[:, 0:8]   # Columns 1 to 7
conso = data[:, 8]  # Conso

mlp = MLPRegressor(hidden_layer_sizes=(10, ), solver='lbfgs', max_iter=10000)
mlp.fit(valeurs, conso)

# Training score
print("Score train :", mlp.score(valeurs, conso))

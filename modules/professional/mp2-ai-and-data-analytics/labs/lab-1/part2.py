import numpy as np
from sklearn.neural_network import MLPClassifier

data = np.genfromtxt('glass_data.csv', delimiter=',')

values = data[:, 0:9]  # Columns 1 to 8
classes = data[:, 9]  # Glass type

mlp = MLPClassifier(hidden_layer_sizes=(1,), solver='lbfgs', max_iter=10000)
mlp.fit(values, classes)  # Training

# Training score
print("Score train :", mlp.score(values, classes))

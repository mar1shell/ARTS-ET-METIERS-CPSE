import numpy as np
from sklearn.neural_network import MLPClassifier

# Loading the data: CSV file with 3 columns and 1200 rows
data = np.genfromtxt('data.csv', delimiter=',')
values = data[:, 0:2]  # Columns 1 et 2
classes = data[:, 2]  # Column 3

# Creating the network
mlp = MLPClassifier(hidden_layer_sizes=(1,), solver='adam', activation='relu', max_iter=10000)

# Training
mlp.fit(values[0:10], classes[0:10])

# Training score
print("Score train :", mlp.score(values[0:10], classes[0:10]))
# Test set score
print("Score test :", mlp.score(values[10:20], classes[10:20]))
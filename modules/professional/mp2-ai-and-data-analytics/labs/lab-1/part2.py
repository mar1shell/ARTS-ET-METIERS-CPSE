import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 1. Chargement des données
data = np.genfromtxt('glass_data.csv', delimiter=',')
valeurs = data[:, 0:9]
classe = data[:, 9]

# 2. Recherche des meilleurs hyperparamètres avec GridSearch
valeurs_train_init, valeurs_test_init, classe_train_init, classe_test_init = train_test_split(
    valeurs, classe, test_size=0.33, random_state=42
)

scaler = StandardScaler()
valeurs_train_scaled_init = scaler.fit_transform(valeurs_train_init)

param_grid = {
    'hidden_layer_sizes': [(32,), (64, 32), (100,), (50, 25)],
    'activation': ['relu',],
    'solver': ['adam', 'lbfgs'],
    'max_iter': [2500]
}

base_mlp = MLPClassifier(random_state=42)

grid_search = GridSearchCV(
    estimator=base_mlp,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(valeurs_train_scaled_init, classe_train_init)

best_params = grid_search.best_params_
print("--- 1. Hyperparamètres optimaux (GridSearch) ---")
print(f"Meilleurs paramètres : {best_params}\n")

# 3. Question 4 : Évaluation sur plusieurs tirages aléatoires
N_iterations = 50
scores_train = []
scores_test = []

classes_uniques = np.unique(classe)
cm_cumulee = np.zeros((len(classes_uniques), len(classes_uniques)))

print(f"--- 2. Exécution de {N_iterations} tirages aléatoires ---")

for i in range(N_iterations):
    # Nouveau tirage aléatoire du jeu d'apprentissage
    X_tr, X_te, y_tr, y_te = train_test_split(valeurs, classe, test_size=0.33)

    # Standardisation des données
    X_tr_sc = scaler.fit_transform(X_tr)
    X_te_sc = scaler.transform(X_te)

    # Entraînement avec les meilleurs hyperparamètres
    model = MLPClassifier(**best_params)
    model.fit(X_tr_sc, y_tr)

    # Enregistrement des scores
    scores_train.append(model.score(X_tr_sc, y_tr))
    scores_test.append(model.score(X_te_sc, y_te))

    # Cumul de la matrice de confusion
    y_pred = model.predict(X_te_sc)
    cm_cumulee += confusion_matrix(y_te, y_pred, labels=classes_uniques)

# 4. Affichage des scores moyens
print(f"Score moyen Train : {np.mean(scores_train):.3f}")
print(f"Score moyen Test  : {np.mean(scores_test):.3f}\n")

# 5. Calcul de la classe la plus difficile à reconnaître
lignes_somme = cm_cumulee.sum(axis=1)
taux_reussite_par_classe = np.divide(
    np.diag(cm_cumulee),
    lignes_somme,
    out=np.zeros_like(np.diag(cm_cumulee)),
    where=lignes_somme != 0
)

print("--- Taux de bonne détection moyen par classe ---")
for idx, cl in enumerate(classes_uniques):
    print(f"Classe {int(cl)} : {taux_reussite_par_classe[idx]*100:.1f}%")

classe_difficile = classes_uniques[np.argmin(taux_reussite_par_classe)]
print(f"\n=> La classe la plus difficile à reconnaître en moyenne est la classe : {int(classe_difficile)}")

# 6. Affichage de la matrice de confusion cumulée
cm_display = ConfusionMatrixDisplay(
    cm_cumulee.astype(int),
    display_labels=classes_uniques.astype(int)
)
cm_display.plot(cmap=plt.cm.Blues)
plt.title(f"Matrice de confusion cumulée sur {N_iterations} tirages")
plt.show()

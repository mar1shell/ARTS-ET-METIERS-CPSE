import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

# -------------------------------------------------------------------
# 1. Visualisation des données (Question 1)
# -------------------------------------------------------------------
data = np.genfromtxt('conso_campus_aix.csv', delimiter=',')
valeurs = data[:, 0:8]  # 8 caractéristiques d'entrée
conso = data[:, 8]      # Consommation

# Affichage avec repères mensuels en abscisse
mois = np.asarray(["jan", "fév", "mars", "avr", "mai", "juin", "juil", "août", "sept", "oct", "nov", "déc"])
index_debut_de_mois = np.where((valeurs[:, 0] == 1) & (valeurs[:, 3] == 0))[0]

plt.figure(figsize=(12, 5))
ax = plt.gca()
ax.set_xticks(index_debut_de_mois)
ax.set_xticklabels(mois[valeurs[:, 1][index_debut_de_mois].astype(int) - 1], rotation=45)
ax.plot(conso, color='tab:blue', alpha=0.8)
plt.title("Consommation d'énergie du campus d'Aix sur un an")
plt.xlabel("Mois")
plt.ylabel("Consommation (kW)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# -------------------------------------------------------------------
# 2. Normalisation et modèle de régression (Question 2)
# -------------------------------------------------------------------
valeurs_norm = np.copy(valeurs)
for i in range(8):
    valeurs_norm[:, i] = valeurs_norm[:, i] / np.max(valeurs_norm[:, i])

# Séparation train / test
X_train, X_test, y_train, y_test = train_test_split(valeurs_norm, conso, test_size=0.33, random_state=42)

# Entraînement du MLPRegressor
mlp = MLPRegressor(
    hidden_layer_sizes=(64, 32),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)
mlp.fit(X_train, y_train)

base_score = mlp.score(X_test, y_test) # Score R²
print("--- 2. Modèle de régression de base ---")
print(f"Score R² sur le jeu de test : {base_score:.3f}\n")

# -------------------------------------------------------------------
# 3. Étude de l'impact des entrées par permutation (Question 3)
# -------------------------------------------------------------------
feature_names = ['Jour', 'Mois', 'Année', 'Heure', 'Vitesse vent', 'Orientation vent', 'Température', 'Humidité']

print("--- 3. Impact de la permutation de chaque entrée ---")
for i in range(8):
    valeurs_perm = np.copy(valeurs_norm)
    # Permutation aléatoire de la colonne i
    valeurs_perm[:, i] = np.random.permutation(valeurs_perm[:, i])

    # Évaluation sur le jeu de test perturbé
    _, X_test_perm, _, _ = train_test_split(valeurs_perm, conso, test_size=0.33, random_state=42)
    score_perm = mlp.score(X_test_perm, y_test)
    drop = base_score - score_perm
    print(f"Perturbation de '{feature_names[i]:<16}' -> Score R² = {score_perm:.3f} (Baisse: {drop:+.3f})")

# -------------------------------------------------------------------
# 4. Test avec un sous-ensemble minimal d'entrées (Question 4)
# -------------------------------------------------------------------
print("\n--- 4. Test d'apprentissage avec le sous-ensemble minimal ---")
# Sélection minimale : Heure (idx 3), Température (idx 6), Mois (idx 1)
indices_minimaux = [1, 3, 6]

X_min = valeurs_norm[:, indices_minimaux]
X_tr_min, X_te_min, y_tr_min, y_te_min = train_test_split(X_min, conso, test_size=0.33, random_state=42)

mlp_min = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=1000, random_state=42)
mlp_min.fit(X_tr_min, y_tr_min)

score_min = mlp_min.score(X_te_min, y_te_min)
print(f"Entrées utilisées : {[feature_names[i] for i in indices_minimaux]}")
print(f"Score R² avec le sous-ensemble minimal : {score_min:.3f}")

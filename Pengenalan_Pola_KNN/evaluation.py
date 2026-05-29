# ==========================================
# IMPORT LIBRARY
# ==========================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATASET
# ==========================================
iris = load_iris()

X = iris.data
y = iris.target


# ==========================================
# SPLIT DATA
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# LIST NILAI K
# ==========================================
k_values = [1, 3, 5, 7, 9]
accuracies = []


# ==========================================
# UJI SETIAP NILAI K
# ==========================================
for k in k_values:

    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    accuracies.append(accuracy)

    print(f"K = {k} | Akurasi = {accuracy}")
    # ==========================================
# CROSS VALIDATION 5-FOLD
# ==========================================
print("\nCross Validation 5-Fold")

for k in k_values:

    model = KNeighborsClassifier(n_neighbors=k)

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5
    )

    print(f"K = {k}")
    print("Score tiap fold :", scores)
    print("Rata-rata akurasi :", scores.mean())
    print()
    # ==========================================
# VISUALISASI GRAFIK
# ==========================================
plt.figure(figsize=(8,5))

plt.plot(
    k_values,
    accuracies,
    marker='o'
)

plt.title("Akurasi KNN Berdasarkan Nilai K")
plt.xlabel("Nilai K")
plt.ylabel("Akurasi")

plt.grid(True)

plt.show()
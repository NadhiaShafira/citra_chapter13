# ==========================================
# IMPORT LIBRARY
# ==========================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


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
# MODEL KNN SKLEARN
# ==========================================
model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)


# ==========================================
# PREDIKSI
# ==========================================
predictions = model.predict(X_test)


# ==========================================
# HITUNG AKURASI
# ==========================================
accuracy = accuracy_score(y_test, predictions)

print("Akurasi KNN Sklearn :", accuracy)
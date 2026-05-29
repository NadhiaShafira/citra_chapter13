# ==========================================
# IMPORT LIBRARY
# ==========================================
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# ==========================================
# LOAD DATASET IRIS
# ==========================================
iris = load_iris()

X = iris.data
y = iris.target


# ==========================================
# SPLIT DATA TRAINING DAN TESTING
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# CEK BENTUK DATA
# ==========================================
print("Jumlah data training :", len(X_train))
print("Jumlah data testing  :", len(X_test))
# ==========================================
# FUNGSI EUCLIDEAN DISTANCE
# ==========================================
def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum((x1 - x2) ** 2))
    return distance


# ==========================================
# TEST PERHITUNGAN JARAK
# ==========================================
jarak = euclidean_distance(X_train[0], X_test[0])

print("Jarak Euclidean :", jarak)
# ==========================================
# FUNGSI KNN MANUAL
# ==========================================
def knn_predict(X_train, y_train, X_test, k=3):

    predictions = []

    # LOOP SEMUA DATA TEST
    for test_point in X_test:

        distances = []

        # HITUNG JARAK KE SEMUA DATA TRAINING
        for i in range(len(X_train)):

            distance = euclidean_distance(test_point, X_train[i])

            distances.append((distance, y_train[i]))

        # URUTKAN BERDASARKAN JARAK TERKECIL
        distances.sort(key=lambda x: x[0])

        # AMBIL K TETANGGA TERDEKAT
        neighbors = distances[:k]

        # AMBIL LABEL TETANGGA
        labels = [label for _, label in neighbors]

        # VOTING LABEL TERBANYAK
        prediction = max(set(labels), key=labels.count)

        predictions.append(prediction)

    return predictions
# ==========================================
# TEST KNN MANUAL
# ==========================================
predictions = knn_predict(X_train, y_train, X_test, k=3)

print("Hasil Prediksi :")
print(predictions[:10])

print("Label Asli :")
print(y_test[:10])
# ==========================================
# HITUNG AKURASI
# ==========================================
accuracy = accuracy_score(y_test, predictions)

print("Akurasi KNN Manual :", accuracy)
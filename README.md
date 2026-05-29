# 🌸 IMPLEMENTASI K-NEAREST NEIGHBOR (KNN) DARI NOL 🌸

<div align="center">

✨ *Project Tugas Pengolahan Citra* ✨

<img src="https://img.shields.io/badge/Python-Programming-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/KNN-Machine%20Learning-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Scikit--Learn-AI-yellow?style=for-the-badge&logo=scikitlearn">
<img src="https://img.shields.io/badge/VSCode-Editor-blue?style=for-the-badge&logo=visualstudiocode">

</div>

---

# 👩‍🎓 IDENTITAS MAHASISWA

| 📌 Keterangan        | 📖 Isi                                  |
| -------------------- | --------------------------------------- |
| 👤 Nama              | **Nadhia Shafira**                      |
| 🆔 NIM               | **312410498**                           |
| 🏫 Kelas             | **I241E**                               |
| 📚 Mata Kuliah       | **Pengolahan Citra**                    |
| 👨‍🏫 Dosen Pengampu | **Dr. Muhamad Fatchan, S.Kom., M.Kom.** |

---

# 📖 DESKRIPSI PROJECT

Project ini merupakan implementasi algoritma **K-Nearest Neighbor (KNN)** dari nol menggunakan bahasa pemrograman Python 🐍 tanpa menggunakan classifier bawaan sklearn pada proses utama.

Pada project ini dilakukan beberapa tahapan penting, yaitu:

✨ Implementasi manual algoritma KNN
✨ Perhitungan Euclidean Distance
✨ Prediksi klasifikasi data
✨ Pengujian beberapa nilai K
✨ Evaluasi akurasi model
✨ Perbandingan dengan KNN bawaan sklearn
✨ Cross Validation 5-Fold
✨ Visualisasi grafik akurasi

Dataset yang digunakan adalah **Iris Dataset** dari sklearn 🌸

---

# 🛠️ TOOLS & LIBRARY

| 💻 Tools     | 📌 Fungsi                   |
| ------------ | --------------------------- |
| Python       | Bahasa pemrograman utama    |
| NumPy        | Operasi perhitungan numerik |
| Matplotlib   | Visualisasi grafik          |
| Scikit-Learn | Dataset & evaluasi model    |
| VSCode       | Code editor                 |

---

# 📂 STRUKTUR PROJECT

```plaintext
Pengenalan_Pola_KNN
│
├── dataset
│
├── knn_manual.py
├── knn_sklearn.py
├── evaluation.py
│
├── README.md
│
├── ss1_struktur_folder.png
├── ss2_install_library.png
├── ss3_python_running.png
├── ss4_load_dataset.png
├── ss5_euclidean_distance.png
├── ss6_knn_manual_prediction.png
├── ss7_knn_accuracy.png
├── ss8_knn_sklearn.png
├── ss9_perbandingan_nilai_k.png
├── ss10_cross_validation.png
└── ss11_grafik_akurasi.png
```

---

# 🚀 LANGKAH-LANGKAH PENGERJAAN

# 📌 1. Persiapan Project

Pada tahap awal dilakukan pembuatan folder project serta instalasi library yang dibutuhkan.

Library yang digunakan:

* NumPy
* Matplotlib
* Scikit-Learn

📷 **Dokumentasi Persiapan Project**

Letakkan gambar di bawah ini:

```markdown
![Struktur Folder](ss1_struktur_folder.png)

![Install Library](ss2_install_library.png)

![Python Running](ss3_python_running.png)
```

Hasil tampilannya nanti:

![Struktur Folder](https://github.com/NadhiaShafira/citra_chapter13/blob/e6e0802f2c659a0683d96918eab017ebca0bf7f3/docs/ss1_struktur_folder.png)

![Install Library](ss2_install_library.png)

![Python Running](ss3_python_running.png)

---

# 📌 2. Load Dataset Iris 🌸

Dataset Iris digunakan sebagai dataset klasifikasi karena:
✨ ringan
✨ mudah digunakan
✨ cocok untuk implementasi KNN

Dataset memiliki:

* 150 data
* 4 fitur
* 3 kelas

📷 **Dokumentasi Load Dataset**

```markdown
![Load Dataset](ss4_load_dataset.png)
```

![Load Dataset](ss4_load_dataset.png)

---

# 📌 3. Perhitungan Euclidean Distance 📏

Euclidean Distance digunakan untuk menghitung jarak antar data.

Rumus Euclidean Distance:

```math
d = \sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
```

Tahapan:
✨ menghitung selisih fitur
✨ mengkuadratkan nilai
✨ menjumlahkan seluruh hasil
✨ melakukan akar kuadrat

📷 **Dokumentasi Euclidean Distance**

```markdown
![Euclidean Distance](ss5_euclidean_distance.png)
```

![Euclidean Distance](ss5_euclidean_distance.png)

---

# 📌 4. Implementasi KNN Manual 🤖

Pada tahap ini algoritma KNN dibuat secara manual tanpa classifier sklearn.

Tahapan algoritma:
✅ menghitung jarak seluruh data training
✅ mengurutkan jarak terkecil
✅ mengambil K tetangga terdekat
✅ melakukan voting kelas terbanyak
✅ menghasilkan prediksi

📷 **Dokumentasi KNN Manual**

```markdown
![KNN Manual](ss6_knn_manual_prediction.png)
```

![KNN Manual](ss6_knn_manual_prediction.png)

---

# 📌 5. Evaluasi Akurasi 📊

Evaluasi dilakukan menggunakan:

```python
accuracy_score()
```

Tujuan evaluasi:
✨ mengetahui performa model
✨ menghitung jumlah prediksi benar
✨ melihat efektivitas algoritma

📷 **Dokumentasi Akurasi**

```markdown
![Akurasi](ss7_knn_accuracy.png)
```

![Akurasi](ss7_knn_accuracy.png)

---

# 📌 6. Perbandingan dengan Sklearn ⚖️

Pada tahap ini dilakukan perbandingan antara:

* KNN manual
* KNN bawaan sklearn

Tujuan:
✨ memastikan implementasi manual sudah benar
✨ membandingkan performa model

📷 **Dokumentasi KNN Sklearn**

```markdown
![KNN Sklearn](ss8_knn_sklearn.png)
```

![KNN Sklearn](ss8_knn_sklearn.png)

---

# 📌 7. Pengujian Beberapa Nilai K 🔍

Pengujian dilakukan menggunakan:

* K = 1
* K = 3
* K = 5
* K = 7
* K = 9

Tujuan:
✨ mengetahui pengaruh nilai K
✨ mencari akurasi terbaik
✨ membandingkan performa model

📷 **Dokumentasi Pengujian Nilai K**

```markdown
![Perbandingan Nilai K](ss9_perbandingan_nilai_k.png)
```

![Perbandingan Nilai K](ss9_perbandingan_nilai_k.png)

---

# 📌 8. Cross Validation 5-Fold 🔄

Cross Validation digunakan agar evaluasi model lebih stabil dan akurat.

Tahapan:
✅ data dibagi menjadi 5 bagian
✅ 4 fold digunakan untuk training
✅ 1 fold digunakan untuk testing
✅ proses diulang sebanyak 5 kali

📷 **Dokumentasi Cross Validation**

```markdown
![Cross Validation](ss10_cross_validation.png)
```

![Cross Validation](ss10_cross_validation.png)

---

# 📌 9. Visualisasi Grafik 📈

Visualisasi dilakukan menggunakan Matplotlib.

Grafik digunakan untuk:
✨ melihat hubungan nilai K dengan akurasi
✨ mempermudah analisis hasil
✨ membuat project lebih informatif

📷 **Dokumentasi Grafik**

```markdown
![Grafik Akurasi](ss11_grafik_akurasi.png)
```

![Grafik Akurasi](ss11_grafik_akurasi.png)

---

# 📊 HASIL PENGUJIAN

Berdasarkan hasil pengujian:

✅ Implementasi manual berhasil berjalan dengan baik
✅ Hasil manual hampir sama dengan sklearn
✅ Nilai K mempengaruhi performa model
✅ Cross Validation menghasilkan evaluasi lebih stabil

Semakin tepat nilai K yang digunakan, maka performa model dapat menjadi lebih optimal 🚀

---

# 🧠 KESIMPULAN

Algoritma K-Nearest Neighbor (KNN) dapat diimplementasikan secara manual menggunakan Python dengan konsep dasar:

* menghitung jarak,
* mencari tetangga terdekat,
* melakukan voting kelas.

Implementasi manual berhasil memberikan hasil akurasi yang baik dan hampir sama dengan library sklearn.

Selain itu, penggunaan beberapa nilai K dan cross validation membantu menghasilkan evaluasi model yang lebih optimal dan stabil ✨

---

# 🌟 TERIMA KASIH 🌟

✨ Project ini dibuat untuk memenuhi tugas mata kuliah Pengolahan Citra ✨

<div align="center">

💖 Terima Kasih 💖

</div>

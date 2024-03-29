import pandas as pd
import numpy as np

# Mengganti 'nama_file.csv' dengan nama file CSV yang sesuai
file_path = 'Python\\Covid19Patient.csv'

# Membaca data dari file CSV
data = pd.read_csv(file_path, delimiter=',')

# Memilih 10 variabel independen yang numerik
independent_variables = ['intubed', 'pneumonia', 'sex', 'pregnancy', 'diabetes','asthma','inmsupr','hypertension','cardiovascular','obesity']

# Menambahkan kolom konstanta ke variabel independen
X = np.column_stack((np.ones(len(data)), data[independent_variables]))

# Variabel dependen yang ingin diprediksi
y = data['age']  # Ganti 'Target_Variable' dengan variabel dependen yang sesuai

# Menghitung matriks (X'X) inverse
XtX_inv = np.linalg.inv(np.dot(X.T, X))

# Menghitung matriks (X'Y)
XtY = np.dot(X.T, y)

# Menghitung koefisien regresi
beta = np.dot(XtX_inv, XtY)

# Menampilkan koefisien regresi
print("Koefisien Regresi:")
for i, var in enumerate(['Intercept'] + independent_variables):
    print(f"{var}: {beta[i]}")
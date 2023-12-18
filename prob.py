import pandas as pd
from tabulate import tabulate

# Membaca file excel
path = r'C:\Users\azxx\Documents\1. KULIAH\3. SEMESTER 3\7. STATISTIK KOMPUTASI\naive_bayes\dataziz.xlsx'
df = pd.read_excel(path)

# Menghitung probabilitas untuk kolom "perawatan"
def hitung_probabilitas_perawatan(data, kondisi, kasus):
    count_kondisi = data.loc[(data['perawatan'] == kondisi) & (data['kasus'] == kasus)].shape[0]
    total_kasus = data.loc[data['kasus'] == kasus].shape[0]
    
    prob_kondisi = (count_kondisi + 1) / (total_kasus + 3)  # Laplace smoothing
    return round(prob_kondisi, 2)


# Menghitung probabilitas untuk kolom "sembuh"
def hitung_probabilitas_sembuh(data, kondisi, kasus):
    count_kondisi = data.loc[(data['sembuh'] == kondisi) & (data['kasus'] == kasus)].shape[0]
    total_kasus = data.loc[data['kasus'] == kasus].shape[0]
    
    prob_kondisi = (count_kondisi + 1) / (total_kasus + 3)  # Laplace smoothing
    return round(prob_kondisi, 2)

# Menghitung probabilitas untuk kolom "meninggal"
def hitung_probabilitas_meninggal(data, kondisi, kasus):
    count_kondisi = data.loc[(data['meninggal'] == kondisi) & (data['kasus'] == kasus)].shape[0]
    total_kasus = data.loc[data['kasus'] == kasus].shape[0]
    
    prob_kondisi = (count_kondisi + 1) / (total_kasus + 3)  # Laplace smoothing
    return round(prob_kondisi, 2)

# Meminta inputan user
perawatan = input("Masukkan nilai perawatan (ringan/menengah/berat): ")
sembuh = input("Masukkan nilai sembuh (normal/otg/rehabilitasi): ")
meninggal = input("Masukkan nilai meninggal (pemulihan/komplikasi/covid): ")

# Menghitung probabilitas untuk input user
prob_perawatan_negatif = hitung_probabilitas_perawatan(df, perawatan, 'negatif')
prob_perawatan_positif = hitung_probabilitas_perawatan(df, perawatan, 'positif')

prob_sembuh_negatif = hitung_probabilitas_sembuh(df, sembuh, 'negatif')
prob_sembuh_positif = hitung_probabilitas_sembuh(df, sembuh, 'positif')

prob_meninggal_negatif = hitung_probabilitas_meninggal(df, meninggal, 'negatif')
prob_meninggal_positif = hitung_probabilitas_meninggal(df, meninggal, 'positif')

# Menghitung probabilitas total
prob_negatif = prob_perawatan_negatif * prob_sembuh_negatif * prob_meninggal_negatif
prob_positif = prob_perawatan_positif * prob_sembuh_positif * prob_meninggal_positif

# Menentukan hasil prediksi
kasus_prediksi = 'Positif' if prob_positif > prob_negatif else 'Negatif'

# Menampilkan hasil
print(f"Probabilitas Kasus Negatif: {prob_negatif:.4f}")
print(f"Probabilitas Kasus Positif: {prob_positif:.4f}")
print(f"Hasil Prediksi: {kasus_prediksi}")

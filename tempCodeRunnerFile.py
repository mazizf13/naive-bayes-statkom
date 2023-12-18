import pandas as pd
from tabulate import tabulate

# Membaca file excel
path = r'C:\Users\azxx\Documents\1. KULIAH\3. SEMESTER 3\7. STATISTIK KOMPUTASI\naive_bayes\dataziz.xlsx'
df = pd.read_excel(path)

# Fungsi untuk menghitung probabilitas
def hitung_probabilitas(data, kolom, kondisi, kasus):
    count_negatif = data.loc[(data[kolom] == kondisi) & (data['kasus'] == 'negatif')].shape[0]
    count_positif = data.loc[(data[kolom] == kondisi) & (data['kasus'] == 'positif')].shape[0]
    total_negatif = data.loc[data['kasus'] == 'negatif'].shape[0]
    total_positif = data.loc[data['kasus'] == 'positif'].shape[0]

    prob_negatif = count_negatif / total_negatif
    prob_positif = count_positif / total_positif

    return count_negatif, count_positif, round(prob_negatif, 2), round(prob_positif, 2)

# Menyiapkan data untuk tabel
def siapkan_data_tabel(data):
    tabel = []
    for kondisi in ['ringan', 'menengah', 'berat']:
        count_negatif, count_positif, prob_negatif, prob_positif = hitung_probabilitas(data, 'perawatan', kondisi, 'positif')
        tabel.append([kondisi, count_negatif, count_positif, prob_negatif, prob_positif])

    tabel.append(['Total', data.loc[data['kasus'] == 'negatif'].shape[0], data.loc[data['kasus'] == 'positif'].shape[0],
                  round(data.loc[data['kasus'] == 'negatif'].shape[0] / len(data), 2),
                  round(data.loc[data['kasus'] == 'positif'].shape[0] / len(data), 2)])
    return tabel

# Menampilkan tabel perawatan
print(tabulate(siapkan_data_tabel(df.head(140)), headers=["Ringan", "Negatif", "Positif", "Probabilitas Negatif", "Probabilitas Positif"], tablefmt='fancy_grid'))

# Meminta inputan user
perawatan = input("Masukkan nilai ringan/menengah/berat: ")
sembuh = input("Masukkan nilai sembuh normal/otg/rehabilitasi: ")
meninggal = input("Masukkan nilai meninggal pemulihan/komplikasi/covid: ")

# Fungsi untuk mendapatkan probabilitas
def dapatkan_probabilitas(data, kolom, kondisi):
    prob_negatif = hitung_probabilitas(data, kolom, kondisi, 'negatif')[2]
    prob_positif = hitung_probabilitas(data, kolom, kondisi, 'positif')[3]
    return prob_negatif, prob_positif

# Mendapatkan probabilitas
perawatan_negatif, perawatan_positif = dapatkan_probabilitas(df.head(140), 'perawatan', perawatan)
sembuh_negatif, sembuh_positif = dapatkan_probabilitas(df.head(140), 'sembuh', sembuh)
meninggal_negatif, meninggal_positif = dapatkan_probabilitas(df.head(140), 'meninggal', meninggal)

# Menghitung hasil prediksi
negatif = perawatan_negatif * sembuh_negatif * meninggal_negatif
positif = perawatan_positif * sembuh_positif * meninggal_positif

# Menyimpan hasil prediksi
kasus_prediksi = 'Positif' if positif > negatif else 'Negatif'
dataziz = df.head(140).copy()
dataziz.loc[:, 'kasus_prediksi'] = kasus_prediksi

# Menghitung akurasi
akurasi = sum(dataziz['kasus'] == dataziz['kasus_prediksi']) / len(dataziz) * 100
print(f"Akurasi: {akurasi:.2f}%")
print(f"Hasilnya adalah: {kasus_prediksi}")

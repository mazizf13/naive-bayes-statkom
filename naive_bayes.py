import pandas as pd
import numpy as np
from tabulate import tabulate

# Membaca file excel
path = r'C:\Users\azxx\Documents\1. KULIAH\3. SEMESTER 3\7. STATISTIK KOMPUTASI\naive_bayes\dataziz.xlsx'
df = pd.read_excel(path)

prob_perawatan = df['perawatan'].head(141).value_counts()
print(prob_perawatan)

dataziz = df.head(140)
kasus = dataziz["kasus"]
perawatan = dataziz["perawatan"]

# Jumlah Kejadian berdasarkan hasil negatif kolom perawatan
count_perawatan_ringan_negatif = dataziz.loc[dataziz['perawatan']
                                             == 'ringan'].loc[dataziz['kasus'] == 'negatif'].shape[0]
count_perawatan_menengah_negatif = dataziz.loc[dataziz['perawatan']
                                               == 'menengah'].loc[dataziz['kasus'] == 'negatif'].shape[0]
count_perawatan_berat_negatif = dataziz.loc[dataziz['perawatan']
                                            == 'berat'].loc[dataziz['kasus'] == 'negatif'].shape[0]
total_perawatan_negatif = count_perawatan_ringan_negatif + \
    count_perawatan_menengah_negatif+count_perawatan_berat_negatif

# Jumlah Kejadian berdasarkan hasil positif kolom perawatan
count_perawatan_ringan_positif = dataziz.loc[dataziz['perawatan']
                                             == 'ringan'].loc[dataziz['kasus'] == 'positif'].shape[0]
count_perawatan_menengah_positif = dataziz.loc[dataziz['perawatan']
                                               == 'menengah'].loc[dataziz['kasus'] == 'positif'].shape[0]
count_perawatan_berat_positif = dataziz.loc[dataziz['perawatan']
                                            == 'berat'].loc[dataziz['kasus'] == 'positif'].shape[0]
total_perawatan_positif = count_perawatan_ringan_positif + \
    count_perawatan_menengah_positif+count_perawatan_berat_positif

# probabilitas ringan negatif kolom perawatan
prob_count_perawatan_ringan_negatif = count_perawatan_ringan_negatif / \
    total_perawatan_negatif
prob_count_perawatan_menengah_negatif = count_perawatan_menengah_negatif / \
    total_perawatan_negatif
prob_count_perawatan_berat_negatif = count_perawatan_berat_negatif / \
    total_perawatan_negatif
total_negatif = prob_count_perawatan_ringan_negatif + \
    prob_count_perawatan_menengah_negatif + prob_count_perawatan_berat_negatif

# probabilitas ringan positif kolom perawatan
prob_count_perawatan_ringan_positif = count_perawatan_ringan_positif / \
    total_perawatan_positif
prob_count_perawatan_menengah_positif = count_perawatan_menengah_positif / \
    total_perawatan_positif
prob_count_perawatan_berat_positif = count_perawatan_berat_positif / \
    total_perawatan_positif
total_positif = prob_count_perawatan_ringan_positif + \
    prob_count_perawatan_menengah_positif + prob_count_perawatan_berat_positif

# Menyusun data untuk tabel kolom perawatan
data_table = [
    ["Ringan", count_perawatan_ringan_negatif, count_perawatan_ringan_positif, round(
        prob_count_perawatan_ringan_negatif, 2), round(prob_count_perawatan_ringan_positif, 2)],
    ["Menengah", count_perawatan_menengah_negatif, count_perawatan_menengah_positif, round(
        prob_count_perawatan_menengah_negatif, 2), round(prob_count_perawatan_menengah_positif, 2)],
    ["Berat", count_perawatan_berat_negatif, count_perawatan_berat_positif, round(
        prob_count_perawatan_berat_negatif, 2), round(prob_count_perawatan_berat_positif, 2)],
    ["Total", total_perawatan_negatif, total_perawatan_positif,
        round(total_negatif, 2), round(total_positif, 2)]
]

# Menampilkan tabel kolom perawatan
table_headers = ["Ringan", "Negatif", "Positif",
                 "Probabilitas Negatif", "Probabilitas Positif"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# KOLOM SEMBUH
prob_sembuh = df['sembuh'].head(140).value_counts()
print(prob_sembuh)

dataziz = df.head(140)
kasus = dataziz["kasus"].head(140)
sembuh = dataziz["sembuh"].head(140)

# Jumlah Kejadian berdasarkan hasil negatif kolom sembuh
count_sembuh_normal_negatif = dataziz.loc[sembuh ==
                                          'normal'].loc[kasus == 'negatif'].shape[0]
count_sembuh_otg_negatif = dataziz.loc[sembuh ==
                                       'otg'].loc[kasus == 'negatif'].shape[0]
count_sembuh_rehabilitasi_negatif = dataziz.loc[sembuh ==
                                                'rehabilitasi'].loc[kasus == 'negatif'].shape[0]
total_sembuh_negatif = count_sembuh_normal_negatif + \
    count_sembuh_otg_negatif+count_sembuh_rehabilitasi_negatif

# Jumlah Kejadian berdasarkan hasil positif kolom sembuh
count_sembuh_normal_positif = dataziz.loc[sembuh ==
                                          'normal'].loc[kasus == 'positif'].shape[0]
count_sembuh_otg_positif = dataziz.loc[sembuh ==
                                       'otg'].loc[kasus == 'positif'].shape[0]
count_sembuh_rehabilitasi_positif = dataziz.loc[sembuh ==
                                                'rehabilitasi'].loc[kasus == 'positif'].shape[0]
total_sembuh_positif = count_sembuh_normal_positif + \
    count_sembuh_otg_positif+count_sembuh_rehabilitasi_positif

# probabilitas sembuh negatif kolom sembuh
prob_count_sembuh_normal_negatif = count_sembuh_normal_negatif / \
    total_sembuh_negatif
prob_count_sembuh_otg_negatif = count_sembuh_otg_negatif / total_sembuh_negatif
prob_count_sembuh_rehabilitasi_negatif = count_sembuh_rehabilitasi_negatif / \
    total_sembuh_negatif
total_negatif = prob_count_sembuh_normal_negatif + \
    prob_count_sembuh_otg_negatif + prob_count_sembuh_rehabilitasi_negatif

# probabilitas sembuh positif
prob_count_sembuh_normal_positif = count_sembuh_normal_positif / \
    total_sembuh_positif
prob_count_sembuh_otg_positif = count_sembuh_otg_positif / total_sembuh_positif
prob_count_sembuh_rehabilitasi_positif = count_sembuh_rehabilitasi_positif / \
    total_sembuh_positif
total_negatif = prob_count_sembuh_normal_positif + \
    prob_count_sembuh_otg_positif + prob_count_sembuh_rehabilitasi_positif

# Menyusun data untuk tabel
data_table = [
    ["normal", count_sembuh_normal_negatif, count_sembuh_normal_positif, round(
        prob_count_sembuh_normal_negatif, 2), round(prob_count_sembuh_normal_positif, 2)],
    ["otg", count_sembuh_otg_negatif, count_sembuh_otg_positif, round(
        prob_count_sembuh_otg_negatif, 2), round(prob_count_sembuh_otg_positif, 2)],
    ["rehabilitasi", count_sembuh_rehabilitasi_negatif, count_sembuh_rehabilitasi_positif, round(
        prob_count_sembuh_rehabilitasi_negatif, 2), round(prob_count_sembuh_rehabilitasi_positif, 2)],
    ["Total", total_sembuh_negatif, total_sembuh_positif,
        round(total_negatif, 2), round(total_positif, 2)]
]

# Menampilkan tabel
table_headers = ["Sembuh", "Negatif", "Positif",
                 "Probabilitas Negatif", "Probabilitas Positif"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

prob_meninggal = df['meninggal'].head(140).value_counts()
print(prob_meninggal)

dataziz = df.head(140)
kasus = dataziz["kasus"].head(140)
meninggal = dataziz["meninggal"].head(140)
# Jumlah Kejadian berdasarkan hasil negatif
count_meninggal_pemulihan_negatif = dataziz.loc[meninggal ==
                                                'pemulihan'].loc[kasus == 'negatif'].shape[0]
count_meninggal_komplikasi_negatif = dataziz.loc[meninggal ==
                                                 'komplikasi'].loc[kasus == 'negatif'].shape[0]
count_meninggal_covid_negatif = dataziz.loc[meninggal ==
                                            'covid'].loc[kasus == 'negatif'].shape[0]
total_meninggal_negatif = count_meninggal_pemulihan_negatif + \
    count_meninggal_komplikasi_negatif+count_meninggal_covid_negatif

# Jumlah Kejadian berdasarkan hasil positif
count_meninggal_pemulihan_positif = dataziz.loc[meninggal ==
                                                'pemulihan'].loc[kasus == 'positif'].shape[0]
count_meninggal_komplikasi_positif = dataziz.loc[meninggal ==
                                                 'komplikasi'].loc[kasus == 'positif'].shape[0]
count_meninggal_covid_positif = dataziz.loc[meninggal ==
                                            'covid'].loc[kasus == 'positif'].shape[0]
total_meninggal_positif = count_meninggal_pemulihan_positif + \
    count_meninggal_komplikasi_positif+count_meninggal_covid_positif

# probabilitas meninggal negatif
prob_count_meninggal_pemulihan_negatif = count_meninggal_pemulihan_negatif / \
    total_meninggal_negatif
prob_count_meninggal_komplikasi_negatif = count_meninggal_komplikasi_negatif / \
    total_meninggal_negatif
prob_count_meninggal_covid_negatif = count_meninggal_covid_negatif / \
    total_meninggal_negatif
total_negatif = prob_count_meninggal_pemulihan_negatif + \
    prob_count_meninggal_komplikasi_negatif + prob_count_meninggal_covid_negatif

# probabilitas meninggal positif
prob_count_meninggal_pemulihan_positif = count_meninggal_pemulihan_positif / \
    total_meninggal_positif
prob_count_meninggal_komplikasi_positif = count_meninggal_komplikasi_positif / \
    total_meninggal_positif
prob_count_meninggal_covid_positif = count_meninggal_covid_positif / \
    total_meninggal_positif
total_positif = prob_count_meninggal_pemulihan_positif + \
    prob_count_meninggal_komplikasi_positif + prob_count_meninggal_covid_positif

# Menyusun data untuk tabel
data_table = [
    ["pemulihan", count_meninggal_pemulihan_negatif, count_meninggal_pemulihan_positif, round(
        prob_count_meninggal_pemulihan_negatif, 2), round(prob_count_meninggal_pemulihan_positif, 2)],
    ["komplikasi", count_meninggal_komplikasi_negatif, count_meninggal_komplikasi_positif, round(
        prob_count_meninggal_komplikasi_negatif, 2), round(prob_count_meninggal_komplikasi_positif, 2)],
    ["covid", count_meninggal_covid_negatif, count_meninggal_covid_positif, round(
        prob_count_meninggal_covid_negatif, 2), round(prob_count_meninggal_covid_positif, 2)],
    ["Total", total_meninggal_negatif, total_meninggal_positif,
        round(total_negatif, 2), round(total_positif, 2)]
]

# Menampilkan tabel
table_headers = ["Meninggal", "Negatif", "Positif",
                 "Probabilitas negatif", "Probabilitas positif"]
print(tabulate(data_table, headers=table_headers, tablefmt='fancy_grid'))

# Meminta inputan user
perawatan = input("Masukkan nilai ringan/menengah/berat: ")
sembuh = input("Masukkan nilai sembuh normal/otg/rehabilitasi: ")
meninggal = input("Masukkan nilai meninggal pemulihan/komplikasi/covid: ")

# Cek inputan
if perawatan == "ringan":
    perawatan_negatif = prob_count_perawatan_ringan_negatif
    perawatan_positif = prob_count_perawatan_ringan_positif
elif perawatan == "menengah":
    perawatan_negatif = prob_count_perawatan_menengah_negatif
    perawatan_positif = prob_count_perawatan_menengah_positif
else:
    perawatan_negatif = prob_count_perawatan_berat_negatif
    perawatan_positif = prob_count_perawatan_berat_positif

if sembuh == "normal":
    sembuh_negatif = prob_count_sembuh_normal_negatif
    sembuh_positif = prob_count_sembuh_normal_positif
elif sembuh == "otg":
    sembuh_negatif = prob_count_sembuh_otg_negatif
    sembuh_positif = prob_count_sembuh_otg_positif
else:
    sembuh_negatif = prob_count_sembuh_rehabilitasi_negatif
    sembuh_positif = prob_count_sembuh_rehabilitasi_positif

if meninggal == "pemulihan":
    meninggal_negatif = prob_count_meninggal_pemulihan_negatif
    meninggal_positif = prob_count_meninggal_pemulihan_positif
elif meninggal == "komplikasi":
    meninggal_negatif = prob_count_meninggal_komplikasi_negatif
    meninggal_positif = prob_count_meninggal_komplikasi_positif
else:
    meninggal_negatif = prob_count_meninggal_covid_negatif
    meninggal_positif = prob_count_meninggal_covid_positif

negatif = perawatan_negatif * sembuh_negatif * meninggal_negatif
positif = perawatan_positif * sembuh_positif * meninggal_positif

if positif > negatif:
    kasus = "Positif"
else:
    kasus = "Negatif"

print(f"Hasilnya adalah: {kasus}")

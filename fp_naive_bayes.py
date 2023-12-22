import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style

# Membaca file excel
path = r'C:\Users\azxx\Documents\1. KULIAH\3. SEMESTER 3\7. STATISTIK KOMPUTASI\naive_bayes\dataziz.xlsx'
df = pd.read_excel(path)

# Fungsi untuk menghitung jumlah kejadian berdasarkan hasil
def count_occurrences(data, column, value, case):
    return data.loc[data[column] == value].loc[data['kasus'] == case].shape[0]

# Fungsi untuk menghitung probabilitas
def calculate_probability(count, total):
    return count / total

# Fungsi untuk menyusun data tabel
def create_data_table(count_neg, count_pos, prob_neg, prob_pos):
    return [
        ["Ringan", count_neg[0], count_pos[0], round(prob_neg[0], 2), round(prob_pos[0], 2)],
        ["Menengah", count_neg[1], count_pos[1], round(prob_neg[1], 2), round(prob_pos[1], 2)],
        ["Berat", count_neg[2], count_pos[2], round(prob_neg[2], 2), round(prob_pos[2], 2)],
        ["Total", sum(count_neg), sum(count_pos), round(sum(prob_neg), 2), round(sum(prob_pos), 2)]
    ]

# Kolom PERAWATAN
perawatan_values = ['ringan', 'menengah', 'berat']
total_perawatan_negatif = sum(count_occurrences(df.head(140), 'perawatan', val, 'negatif') for val in perawatan_values)
total_perawatan_positif = sum(count_occurrences(df.head(140), 'perawatan', val, 'positif') for val in perawatan_values)

count_perawatan_negatif = [count_occurrences(df.head(140), 'perawatan', val, 'negatif') for val in perawatan_values]
count_perawatan_positif = [count_occurrences(df.head(140), 'perawatan', val, 'positif') for val in perawatan_values]

prob_perawatan_negatif = [calculate_probability(count, total_perawatan_negatif) for count in count_perawatan_negatif]
prob_perawatan_positif = [calculate_probability(count, total_perawatan_positif) for count in count_perawatan_positif]

# Menyusun data untuk tabel kolom perawatan
data_table_perawatan = create_data_table(count_perawatan_negatif, count_perawatan_positif, prob_perawatan_negatif, prob_perawatan_positif)

# Menampilkan tabel kolom perawatan dengan warna
table_headers_perawatan = [Fore.YELLOW + "Ringan", Fore.YELLOW + "Negatif", Fore.YELLOW + "Positif", Fore.YELLOW + "Probabilitas Negatif", Fore.YELLOW + "Probabilitas Positif" + Style.RESET_ALL]
print(tabulate(data_table_perawatan, headers=table_headers_perawatan, tablefmt='fancy_grid'))

# Kolom SEMBUH
sembuh_values = ['normal', 'otg', 'rehabilitasi']
total_sembuh_negatif = sum(count_occurrences(df.head(140), 'sembuh', val, 'negatif') for val in sembuh_values)
total_sembuh_positif = sum(count_occurrences(df.head(140), 'sembuh', val, 'positif') for val in sembuh_values)

count_sembuh_negatif = [count_occurrences(df.head(140), 'sembuh', val, 'negatif') for val in sembuh_values]
count_sembuh_positif = [count_occurrences(df.head(140), 'sembuh', val, 'positif') for val in sembuh_values]

prob_sembuh_negatif = [calculate_probability(count, total_sembuh_negatif) for count in count_sembuh_negatif]
prob_sembuh_positif = [calculate_probability(count, total_sembuh_positif) for count in count_sembuh_positif]

# Menyusun data untuk tabel kolom sembuh
data_table_sembuh = create_data_table(count_sembuh_negatif, count_sembuh_positif, prob_sembuh_negatif, prob_sembuh_positif)

# Menampilkan tabel kolom sembuh dengan warna
table_headers_sembuh = [Fore.CYAN + "Sembuh", Fore.CYAN + "Negatif", Fore.CYAN + "Positif", Fore.CYAN + "Probabilitas Negatif", Fore.CYAN + "Probabilitas Positif" + Style.RESET_ALL]
print(tabulate(data_table_sembuh, headers=table_headers_sembuh, tablefmt='fancy_grid'))

# Kolom MENINGGAL
meninggal_values = ['pemulihan', 'komplikasi', 'covid']
total_meninggal_negatif = sum(count_occurrences(df.head(140), 'meninggal', val, 'negatif') for val in meninggal_values)
total_meninggal_positif = sum(count_occurrences(df.head(140), 'meninggal', val, 'positif') for val in meninggal_values)

count_meninggal_negatif = [count_occurrences(df.head(140), 'meninggal', val, 'negatif') for val in meninggal_values]
count_meninggal_positif = [count_occurrences(df.head(140), 'meninggal', val, 'positif') for val in meninggal_values]

prob_meninggal_negatif = [calculate_probability(count, total_meninggal_negatif) for count in count_meninggal_negatif]
prob_meninggal_positif = [calculate_probability(count, total_meninggal_positif) for count in count_meninggal_positif]

# Menyusun data untuk tabel kolom meninggal
data_table_meninggal = create_data_table(count_meninggal_negatif, count_meninggal_positif, prob_meninggal_negatif, prob_meninggal_positif)

# Menampilkan tabel kolom meninggal dengan warna
table_headers_meninggal = [Fore.RED + "Meninggal", Fore.RED + "Negatif", Fore.RED + "Positif", Fore.RED + "Probabilitas Negatif", Fore.RED + "Probabilitas Positif" + Style.RESET_ALL]
print(tabulate(data_table_meninggal, headers=table_headers_meninggal, tablefmt='fancy_grid'))

# Meminta inputan user
perawatan = input("Masukkan nilai ringan/menengah/berat: ")
sembuh = input("Masukkan nilai sembuh normal/otg/rehabilitasi: ")
meninggal = input("Masukkan nilai meninggal pemulihan/komplikasi/covid: ")

# Mencari probabilitas berdasarkan input user
perawatan_negatif = prob_perawatan_negatif[perawatan_values.index(perawatan)]
perawatan_positif = prob_perawatan_positif[perawatan_values.index(perawatan)]

sembuh_negatif = prob_sembuh_negatif[sembuh_values.index(sembuh)]
sembuh_positif = prob_sembuh_positif[sembuh_values.index(sembuh)]

meninggal_negatif = prob_meninggal_negatif[meninggal_values.index(meninggal)]
meninggal_positif = prob_meninggal_positif[meninggal_values.index(meninggal)]

# Menghitung probabilitas total
negatif = perawatan_negatif * sembuh_negatif * meninggal_negatif
positif = perawatan_positif * sembuh_positif * meninggal_positif

# Menentukan hasil kasus
kasus = "Positif" if positif > negatif else "Negatif"
print(f"Probabilitas Kasus Positif: {positif:.4f}")
print(f"Probabilitas Kasus Negatif: {negatif:.4f}")
if kasus == "Positif":
    print(Fore.GREEN + f"Hasilnya adalah: {kasus}" + Style.RESET_ALL)
else:
    print(Fore.YELLOW + f"Hasilnya adalah: {kasus}" + Style.RESET_ALL)

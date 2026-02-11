stok = [15, 50, 30, 25, 40]

# No 1
stok.append(100)
print(stok)

# No 2
stok.insert(2, 75)
print(stok)

# No 3
stok.sort(reverse=True)
print(stok)

# No 4
    # Rata - rata = (Jumlah Total) / (Banyak Indeks)
Jumlah_Total = sum(stok)
Banyak_Indeks = len(stok)

Rata_Rata = Jumlah_Total / Banyak_Indeks
print(f'Rata-rata dari stok adalah : {Rata_Rata}')

# No 5
print(f'Isi list setelah semua perubahan : {stok}')
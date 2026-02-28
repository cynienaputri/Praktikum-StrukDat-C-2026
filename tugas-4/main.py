#sebagai program utama yang mengimport kedua module di atas.

from kurs import kurs
from konverter import idr_ke_mata_uang, mata_uang_ke_idr
from tabulate import tabulate

def tampilkan_kurs():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, f"{nilai:,}".replace(",", ".")])
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    print("=== KONVERTER MATA UANG ===")
    tampilkan_kurs()

    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    if dari == "IDR" and ke in kurs:
        hasil = idr_ke_mata_uang(jumlah, ke)
        print(f"Rp {jumlah:,.0f}".replace(",", ".") + f" = {hasil:.2f} {ke}")

    elif ke == "IDR" and dari in kurs:
        hasil = mata_uang_ke_idr(jumlah, dari)
        print(f"{jumlah:.2f} {dari} = Rp {hasil:,.0f}".replace(",", "."))

    else:
        print("Konversi tidak valid.")

if __name__ == "__main__":
    main()
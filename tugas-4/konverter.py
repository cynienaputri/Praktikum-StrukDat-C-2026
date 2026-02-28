#konverter.py berisi fungsi konversi

from kurs import kurs

def idr_ke_mata_uang(jumlah, kode):
    if kode in kurs:
        return jumlah / kurs[kode]
    else:
        return None

def mata_uang_ke_idr(jumlah, kode):
    if kode in kurs:
        return jumlah * kurs[kode]
    else:
        return None
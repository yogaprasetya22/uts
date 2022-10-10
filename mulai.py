import androidhelper
import soal
import tambah
import baca
import ujian
droid = androidhelper.Android()


def utama():
    droid.dialogCreateAlert("PILIH")
    droid.dialogSetItems(
        ["Tambah Soal Baru", "Tampil Soal", "Tambah File", "Ujian", "Keluar"])
    droid.dialogShow()
    ket = droid.dialogGetResponse().result
    if ket['item'] == 0:
        soal.isisoal()
    elif ket['item'] == 1:
        baca.tampilsoal()
    elif ket['item'] == 2:
        tambah.tambahfile()
    elif ket['item'] == 3:
        ujian.ujian()
    else:
        droid.dialogCreateAlert("Error")
        droid.dialogShow()
utama()
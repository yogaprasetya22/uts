import androidhelper
import utama
droid = androidhelper.Android()


def tambahfile():
    filesoal = droid.dialogGetInput("Membuat File Baru", "Nama File").result
    file = filesoal
    file = "/storage/emulated/0/uts/" + file + ".txt"
    objekfile = open(file, "w+")
    utama.utama()

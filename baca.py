import androidhelper
import utama
droid = androidhelper.Android()


def tampilsoal():
    filesoal = droid.dialogGetInput("Menampilkan Soal", "Masukan file").result
    ok = droid.dialogGetResponse().result
    if ok == ["none"]:
        exit()
    else:
        file = filesoal
        file = "/storage/emulated/0/uts/" + file + ".txt"
        objekfile = open(file, "r")
        droid.dialogCreateAlert("Menampilkan", objekfile.read())
        droid.dialogSetPositiveButtonText('Lanjut')
        droid.dialogSetNegativeButtonText('Keluar')
        droid.dialogShow()
        plh = droid.dialogGetResponse().result
        plh = plh['which']
        if plh == "positive":
            utama.utama()
        else:
            exit()

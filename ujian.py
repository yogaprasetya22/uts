import os
import utama
import androidhelper
droid = androidhelper.Android()


def ujian():
    filesoal = droid.dialogGetInput("Mengambil File Soal", "Nama File").result
    rootPath = "/storage/emulated/0/qpython/scripts3/uts/"
    file = open(os.path.join(rootPath, filesoal+".txt"), "r")
    lis = []
    ok = 0
    for num, line in enumerate(file, 1):
        for i in range(100):
            if str(i+1)+'.' in line:
                ok += 1
                index = line.index(str(line))
                index = str(index)
                index = index.replace('0', str(ok+1))
                lis = [index]
    i = 1
    poin = 0
    no = int(lis[0])
    rootPath = "/storage/emulated/0/qpython/scripts3/uts/"
    file = open(os.path.join(rootPath, filesoal+".txt"), "r")
    while i < no:
        i += 1
        text = file.readline()
        pager = text
        text = file.readline()
        soal = text
        text = file.readline()
        a = text
        text = file.readline()
        b = text
        text = file.readline()
        c = text
        text = file.readline()
        d = text
        text = file.readline()
        e = text
        text = file.readline()
        bintang = text
        text = file.readline()
        kunci = text.strip().split(" ")[1]
        text = file.readline()
        pager2 = text
        droid.dialogCreateAlert(soal)
        droid.dialogSetItems([a, b, c, d, e])
        droid.dialogShow()
        jawab = droid.dialogGetResponse().result["item"]

        if jawab == 0:
            cek("a", kunci)
        elif jawab == 1:
            cek("b", kunci)
        elif jawab == 2:
            cek("c", kunci)
        elif jawab == 3:
            cek("d", kunci)
        elif jawab == 4:
            cek("e", kunci)


def cek(jawab, kunci):
    hasil = ""
    if jawab == kunci:
        hasil = "benar"
    else:
        hasil = "kamu jawab (" + jawab + ")\nyang benar (" + kunci + ")"
    droid.dialogCrateAlert("Periksa Jawaban")
    droid.dialogSetItems([hasil])
    droid.dialogSetPositiveButtonText("OK")
    droid.dialogShow()

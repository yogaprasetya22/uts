import androidhelper
import utama
droid = androidhelper.Android()


def isisoal():
    lis = []
    filesoal = droid.dialogGetInput("Mengambil File Soal", "Nama File").result
    isisoal = droid.dialogGetInput("Mengisi Soal", "isi Soal").result
    soala = droid.dialogGetInput("Masukan", "Jawaban A").result
    soalb = droid.dialogGetInput("Masukan", "Jawaban B").result
    soalc = droid.dialogGetInput("Masukan", "Jawaban C").result
    soald = droid.dialogGetInput("Masukan", "Jawaban D").result
    soale = droid.dialogGetInput("Masukan", "Jawaban E").result
    file = filesoal
    file = "/storage/emulated/0/uts/" + file + ".txt"
    fi = open(file, "r+")
    l = fi.readline()
    if len(l) == 0:
        lis = 'ok'
    else:
        ok = 0
        for num, line in enumerate(fi, 1):
            for i in range(100):
                if str(i+1)+'.' in line:
                    ok += 1
                    index = line.index(str(line))
                    index = str(index)
                    index = index.replace('0', str(ok+1))
                    lis = [index]
    if 'ok' in str(lis):
        lis = ['1']
    objekfile = open(file, "a")
    strsoal = str(lis[0]) + '. ' + isisoal
    strA = "a. " + soala
    strB = "b. " + soalb
    strC = "c. " + soalc
    strD = "d. " + soald
    strE = "e. " + soale
    tmpl = "#\n" + strsoal + "\n" + strA + "\n" + strB + \
        "\n" + strC + "\n" + strD + "\n" + strE + "\n" + "*" + "\n" + "?" + "\n" + "##\n"
    kunci = droid.dialogGetInput("Kunci jawaban", tmpl).result
    strkunci = "J= " + kunci
    strmasuk = "#\n" + strsoal + "\n" + strA + "\n" + strB + \
        "\n" + strC + "\n" + strD + "\n" + strE + "\n" + "*" + "\n" + strkunci + "\n" + "##\n"
    objekfile.write(strmasuk)
    droid.dialogCreateAlert("Menampilkan", strmasuk)
    objekfile.close()

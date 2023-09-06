def bilangan_asli(jumlah):
    for i in range(1,jumlah+1):
        print(i)

def cek_bilangan_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, int(angka**0.5)+1):
        if angka % i == 0:
            return False
    return True

def bilangan_prima(jumlah):
    count = 0
    angka = 2
    while count < jumlah:
        if cek_bilangan_prima(angka):
            print(angka, end=" ")
            count += 1
        angka += 1    


def bilangan_fibonaci(jumlah):
    urutan_fibonaci = [0,1]

    for i in range (2,jumlah):
        angka_selanjutnya = urutan_fibonaci[-1] + urutan_fibonaci[-2]
        urutan_fibonaci.append(angka_selanjutnya)
    return urutan_fibonaci


def bilangan_faktorial(jumlah):
    hasil = 1
    for i in range(1 + jumlah+1):
        hasil *= i
    return hasil

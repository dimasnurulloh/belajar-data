def luas_persegi(sisi):
    return(sisi*sisi)

def luas_persegi_panjang(panjang,lebar):
    return(panjang*lebar)

def luas_lingkaran(r):
    phi = 0.314
    luas = phi*r*r
    return luas

def luas_segitiga(alas,tinggi):
    luas = 0.5*alas*tinggi
    return luas

def luas_jajar_genjang(alas,tinggi):
    luas = alas*tinggi
    return luas

def luas_belah_ketupat(diagonal_1,diagonal_2):
    luas = 0.5*diagonal_1*diagonal_2
    return luas

def luas_trapesium(sisi_atas,sisi_bawah,tinggi):
    luas = ((sisi_atas+sisi_bawah)*tinggi)/0.5
    return luas

def luas_layang_layang(diagonal_1,diagonal_2):
    luas = 0.5*diagonal_1*diagonal_2
    return luas

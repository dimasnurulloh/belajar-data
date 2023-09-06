import tkinter as tk
from tkinter import ttk

def cek_ganjil_genap():
    angka = int(angka_entry.get())
    if angka % 2 == 0:
        hasil_label.config(text=f"{angka} adalah angka GENAP!")
    else:
        hasil_label.config(text=f"{angka} adalah angka GANJIL!")

windows = tk.Tk()
windows.title("CEK ANGKA GANJIL ATAU GENAP")
windows.configure(bg="White")
windows.geometry("450x150")

frame = ttk.Frame(windows)
frame.pack(pady=10,padx=10,fill='both',expand=True)

angka_label = ttk.Label(frame,text="Masukan Angka:")
angka_label.pack(pady=5)

angka_entry = ttk.Entry(frame)
angka_entry.pack(pady=5)

tombol_cek = ttk.Button(frame,text="CEK",command=cek_ganjil_genap)
tombol_cek.pack(pady=5)

hasil_label = ttk.Label(frame,text="")
hasil_label.pack(pady=7)

windows.mainloop()
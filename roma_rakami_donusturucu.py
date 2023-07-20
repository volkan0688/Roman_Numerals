from tkinter import *

window = Tk()
window.title("Roma Rakamı Dönüştürücü (by Volkan)")
window.geometry("500x300")
window.config(bg="lightgray")

title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 13, "italic")
button_font = ("Helvetica", 13, "bold")


class RomaRakami:
    hata_mesaj = "Yanlış değer girdiniz."

    @staticmethod
    def sayidan_donusturme(input_number):
        roma_sayilari = {
            4000: "MV̄",
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        sonuc_roma_sayisi = ""
        for sayi in roma_sayilari:
            while input_number >= sayi:
                sonuc_roma_sayisi += roma_sayilari[sayi]
                input_number -= sayi

        return sonuc_roma_sayisi

    @staticmethod
    def roma_rakaminden_donusturme(roma_sayisi):
        roma_sayilari = {
            "MV̄": 4000,
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "İX": 9,
            "V": 5,
            "IV": 4,
            "İV": 4,
            "I": 1,
            "İ": 1,
        }

        sonuc_sayi = 0
        harf = 0
        while harf < len(roma_sayisi):
            if harf + 1 < len(roma_sayisi) and roma_sayisi[harf:harf + 2] in roma_sayilari:
                sonuc_sayi += roma_sayilari[roma_sayisi[harf:harf + 2]]
                harf += 2
            else:
                if roma_sayisi[harf] not in roma_sayilari:
                    return RomaRakami.hata_mesaji()
                sonuc_sayi += roma_sayilari[roma_sayisi[harf]]
                harf += 1

        return sonuc_sayi

    @staticmethod
    def hata_mesaji():
        return "Yanlış değer girdiniz."

    @staticmethod
    def donusturme(event=None):
        input_deger = my_entry.get().upper()

        if input_deger.isdigit():
            if 4999 < int(input_deger):
                my_label_sonuc.config(text="Bu program 1-4999 aralığı için yazılmıştır.")
            else:
                sonuc_roma_sayisi = RomaRakami.sayidan_donusturme(int(input_deger))
                my_label_sonuc.config(text=sonuc_roma_sayisi)
        else:
            if "IIII" in input_deger or "İİİİ" in input_deger:
                my_label_sonuc.config(text=RomaRakami.hata_mesaji())
            else:
                decimal_number = RomaRakami.roma_rakaminden_donusturme(input_deger)
                my_label_sonuc.config(text=decimal_number)
                if isinstance(decimal_number, str):
                    my_label_sonuc.config(text=RomaRakami.hata_mesaji())


# Label Ana Başlık
my_title = Label(text="Roma Rakamı Dönüştürücü")
my_title.config(bg="grey", font=('Helvetica', 18, 'italic'), fg="black")
my_title.config(padx=10, pady=10)
my_title.pack()


# Label Alt Başlık
my_label = Label(text="Roma Rakamlarını Sayılara dönüştürün:", font=label_font, fg="black", bg="lightgray")
my_label.pack()


# Entry Numara
my_entry = Entry(width=20, font=label_font)
my_entry.pack(pady=10)
my_entry.focus()
my_entry.bind("<Return>", RomaRakami.donusturme)


# Button
button = Button(text="Dönüştür", command=RomaRakami.donusturme, font=button_font)
button.pack(pady=5)


# Label Alt Sonuç
my_label_sonuc = Label(text="", font=label_font, fg="black", bg="lightgray")
my_label_sonuc.pack()


window.mainloop()
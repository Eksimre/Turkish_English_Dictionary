import random
import pandas as pd
from tkinter import *


window = Tk()
window.title("Türkçe - İngilizce Sözlük")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

#path bölümüne indireceğiniz kelime klasörünün yolunu giriniz.
path = ""
okunan= pd.read_excel(path)
ing = list(okunan.ing)
tr = list(okunan.tr)
dict = dict(zip(ing, tr))

 
def getir(event):        
    global kilit
    global anahtar    
    soru.delete(first=0,last="end")
    value = random.choice(list(dict.items()))
    kilit = value[0]
    anahtar = value[1]
    soru.insert(0,anahtar)
    
    
def sorgula(event):

    cevap = (ingcevap.get())
    if cevap == kilit:
        ingcevap.delete(first=0,last="end")
        soru.delete(first=0,last="end")
        
        
    else:
        ingcevap.delete(first=0,last="end")
        soru.delete(first=0,last="end")
        yanlis = Label(text=(f"Doğru Cevap: {kilit}---->{anahtar}") , font=("Ariel", 12, "bold"))           
        yanlis.pack() 



Giris = Label(text= "Aşağıda Çıkacak Türkçe Kelimelerin İngilizce Karşılığını Yazınız.", font=("Ariel", 12, "bold"))
Giris.pack()

not1 = Label(text= "Not:İngilizcede en çok kullanılan 500 kelime rastgele olarak getirilecektir.", font=("Ariel", 8, "normal"))
not1.pack()

acıklama = Label(text= "L-Shift Kelime Getirir. \nEnter Cevabınızı Doğrular.", font=("Ariel", 8, "normal"))
acıklama.pack()


soru = Entry (width=20)
soru.pack()

ingcevap = Entry(width=20)
ingcevap.focus_set()
ingcevap.pack()


window.bind("<Return>", sorgula)
window.bind("<KeyPress-Shift_L>", getir)


window.mainloop()
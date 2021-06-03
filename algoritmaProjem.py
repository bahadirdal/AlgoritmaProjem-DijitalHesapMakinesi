from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))
    #print(x)  # Yorum satırına almamızın sebebi sadece işlem sonucunu aşağıda göstermesini istediğimizden.

hesap = 5
s1 = 0

def islemler(x):  # s1 birinci işlem ve 0'ı atadık en başta
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())  # s1'in girişini istedik float şekilde
    print(hesap)
    print(s1)
    giris.delete(0,'end')


s2 = 0
def hesapla():  # s2 ile ikinci sayıyı istedik kullanıcıdan ve 0'ı atadık ilk başta
    global s2
    s2 = float(giris.get())  # s2'nin girişini istedik float şeklinde
    print(s2)
    global hesap
    sonuc=0
    if(hesap==0):
        sonuc = s1 + s2  # Toplama işlemini yaptırdık.
    elif(hesap==1):
        sonuc = s1 - s2  # Çıkarma işlemini yaptırdık.
    elif (hesap == 2):
        sonuc = s1 * s2  # Çarpma işlemini yaptırdık.
    elif (hesap == 3):
        sonuc = s1 / s2  # Bölme işlemini yaptırdık.
    giris.delete(0,'end')
    giris.insert(0,str(sonuc))  # Sonucu str cinsinden yazdırdık.


pencere = Tk()
pencere.geometry("250x300") # Tk'nın boyutlarını ayarladık.

giris = Entry(font="spacing1 14 bold",width=15,justify=RIGHT) # justify ile right yani sağdan yazıma başlattırdık.
giris.place(x=20,y=20)  # Burda da y ve x eksenlerinde ki yerini ayarladık

b = []  # butonları tutmak için butonların dizi olduğunu belirtmek gerekiyor.

for i in range(1,10):
    b.append(Button(text=str(i),font="spacing1 15 bold",command=lambda x=i:yaz(x))) #command ile tıklanan sayıları yazdırdık.

sayac=0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50) # butonların boyutlarını ve yerlerini ayarladık.
        sayac += 1 # Sayaç ile de 1'den 9'a kadar 1'er 1'er arttırarak yazdırdık for ile.

islem = []

for i in range(0,4):
    islem.append(Button(font="spacing1 15 bold",width=4,command=lambda x=i:islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"     ## Burda da işlemlerin simgesini nasıl olması gerektiğini yazdık.
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(0,4):
    islem[i].place(x=170,y=50+50*i)

sb = Button(text="0",font="spacing2 15 bold",command=lambda x=0:yaz(x))
sb.place(x=20,y=200)

nb = Button(text=".",font="spacing2 15 bold",width=2,command=lambda x=".":yaz(x)) # Double sayı girilmek istenirse diye
nb.place(x=70,y=200)

eb = Button(text="=",fg ="RED",font="relief 15 bold",command=hesapla)  # Eşittir butonu, RED diyerek rengini kırmızı yaptık
eb.place(x=120,y=200)


pencere.mainloop()
f = open("HesapMakinesi.txt",)
print(f.read())

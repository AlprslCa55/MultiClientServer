#coding: utf-8
import socket
from tkinter import *
from threading import Thread
from multiprocessing import *

from tkinter import messagebox

global s
host = "localhost"
port = 8090

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
pencere = Tk()

baslik = pencere.title("AlpChat v0.1")
pencere.resizable(width =False,height = False)
pgen = 760
pyuks = 380
ekrangen = pencere.winfo_screenwidth()
ekranyuks = pencere.winfo_screenheight()
x = int((ekrangen - pgen) / 2)
y = int((ekranyuks - pyuks) / 2)

def sendData():
    while(True):
        message = MesajBolge.get()
        if(message):
            s.send(message.encode("utf-8"))
            MesajBolge.delete(0,END)
    
def hello():
   messagebox.showinfo("AlpChat v0.1", "Bu yazılımın tüm hakları saklıdır.Görsel dizayn, kodlama vb. her türlü işlev Alparslan tarafından yapılmıştır")

scrollbar = Scrollbar(pencere)
scrollbar.place()

menu = Menu(pencere)
dosya = Menu(menu)
pencere.config(menu = menu)
menu.add_cascade(label = "Yardım",menu = dosya)
dosya.add_command(label = "Yardım1",command = hello )
pencere.configure(background='purple')




YollaButon = Button(pencere, text = "Mesajı gönder",fg = "blue", bg = "red",command = sendData)
YollaButon.place(x = 250, y = 45)


MesajBolge = Entry(pencere)

MesajBolge.place(x = 375, y = 45,height = 30,width = 200)

Ekran = Text(pencere,fg = "black",bg = "orange",yscrollcommand = scrollbar.set)


Ekran.place(x = 155 , y = 85,height =230,width = 475)

scrollbar.config(command = Ekran.yview)


pencere.geometry("{}x{}+{}+{}".format(pgen,pyuks,x,y))
pencere.mainloop()

pencere = Tk()
baslik = pencere.title("AlpChat v0.1")
frame = Frame(pencere,width = 360,height = 768)

pencere.geometry("768x360+500+400")
pencere.resizable(width =False,height = False)


            
YollaButon = Button(frame, text = "Mesajı gönder",fg = "blue", bg = "red",command = sendData)


YollaButon.pack(fill = X)
MesajBolge = Entry(frame)
MesajBolge.pack()
Ekran = Entry(pencere,fg = "black",bg = "orange")
Ekran.pack()




def getData():
    while(True):
        mesaj = s.recv(1024).decode("utf-8")
        if(mesaj):
            gelen_veri = Ekran.get(1.0,END) + "\n" + mesaj
            print("{}".format(mesaj))
            Ekran.insert(END,mesaj)
            gelen_veri = ""
            


def tred():
    Thread(Thread(target = getData).start()).start().start()
    Thread(Thread(target = sendData).start()).start().start()



Thread(target = tred, args =()).start()

import socket
from threading import Thread
import time

class Misafir:
    def __init__(self,obje,isim):
        self.name = isim
        self.obje = obje


class Server():
    def __init__(self,host,port):
         self.host = host
         self.port = port
         self.list = []
         self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         self.server.bind((host,port))
         self.server.listen(60)

         listenThread = Thread(target = self.listen,args = ()).start() # Dinleyici thread
                 


    def listen(self):
        print("Server start on {} port {}".format(self.host,self.port))
        while(True):
            machine,adres = self.server.accept()

            while(True): # Kullanıcıdan ismini yazmasını bekliyoruz
                print("(~) get name...")
                machine.send("What is your name>".encode("utf-8"))
                name = machine.recv(1024).decode("utf-8")
                if(name):
                    print("{} is online now".format(name))
                    self.list.append(Misafir(machine,name))
                    Thread(target = self.newGuest,args = (machine,name)).start() # Gelen makineyi Thread ile dinlemeye alıyoruz
                    break

        self.server.close()



    def newGuest(self,machine,name): # Gelen mesajları bununla alıyoruz

        while(True):
            mesaj = machine.recv(1024).decode("utf-8")
            if(mesaj):
                label = "({}) {}".format(name,mesaj)
                print(label)
                Thread(target = self.sendAll,args = (label,name)).start()

        machine.close()
        
    def sendAll(self,message,name):
        for i in self.list:
            if(i.name != name): # Mesajı gönderen makineye, kendi mesajını geri göndermemek için
                i.obje.send(message.encode("utf-8"))

Server("localhost",8090)

import socket
from threading import Thread
import time

class Misafir:
    def __init__(self,obje,isim):
        self.name = isim
        self.obje = obje

class Dosya:
    def __init__(self,dosya):
        try: 
            self.dosya = dosya
            self.dosya.flush()
        except:
            self.dosya_kapa()
            
    def write_file(self,message):
        while (True):
            if (message):
                self.dosya.write(message)

    def show_all(self):
        if self.dosya.readlines() != []:
            return True
        else:
            return False
    def dosya_kapa(self):
        self.dosya.close()

    def read_one(self,one):
        if one == True:
            return self.dosya.readlines()
        if one == False:
            return self.dosya.readline()

    def send_al(self,c):
        while self.dosya.readline() != None:
            c.send(self.dosya.readline().encode('utf-8'))


class Server():
    def __init__(self,host,port):
         self.host = host
         global label
         self.port = port
         self.file1 = open('Mesajlar.log',"a+")
         self.list = []
         self.dosya = Dosya(self.file1)
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
                if (1 != 1):
                    name = self.dosya.read_one(False)
                    print("There is an error")
                    self.dosya.send_al(machine)
                else:
                    machine.send("What is your name>".encode("utf-8"))
                    name = machine.recv(1024).decode("utf-8")
                if(name):
                    print("{} is online now".format(name))
                    self.list.append(Misafir(machine,name))
                    Thread(target = self.newGuest,args = (machine,name)).start() # Gelen makineyi Thread ile dinlemeye alıyoruz
                    time.sleep(0.8)
                    Thread(target = self.write_file1,args = ()).start()
                    break

        self.server.close()

    def write_file1(self):
        while(True):
            mesage = label
            if (mesage):
                self.dosya.write_file(mesage)
                mesage = ""


    def newGuest(self,machine,name): # Gelen mesajları bununla alıyoruz

        while(True):
            mesaj = machine.recv(1024).decode("utf-8")
            if(mesaj):
                label = "({}) {}".format(name,mesaj) + "\n"
                print(label)
                Thread(target = self.sendAll,args = (label,name)).start()

        machine.close()
 
    def sendAll(self,message,name):
        for i in self.list:
      	    i.obje.send(message.encode("utf-8"))

Server("localhost",8090)

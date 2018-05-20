import socket
from threading import Thread
import time

global gosterim
global kul_liste

kul_liste = dict()
gosterim = 12 * '-' + "Editor = |AlprslCa55 |" + 12 * '-'
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
global HOST
global PORT
HOST = '192.168.2.81'

PORT = 5555


class Server():
    def __init__(self):
         global SocketServer
         global isim
         global data
         
         t1 = Thread(target = self.yeni_ekle)
         t1.start()
         
         
 
    def veriVer(self):
        self.b = 1
        while self.b > 0:
            if self.b == 1:
                self.SocketServer.send((gosterim + "\n\n\nİsminiz : ").encode('utf-8'))
                self.isim = self.SocketServer.recv(1024)
                self.isim = self.isim.decode('utf-8')
            
                kul_liste[str(self.addr)] = self.isim
                self.SocketServer.send(("Hoş Geldiniz : "+kul_liste[str(self.addr)]).encode('utf-8'))
                self.b +=1
            else:
                self.data = self.SocketServer.recv(1024)
                self.data = self.data.decode('utf-8')
                print(kul_liste[str(self.addr)] + " :" + str(self.data))
                self.message = kul_liste[str(self.addr)] + " : " + str(self.data)
                self.SocketServer.sendall((self.message).encode('utf-8'))
                self.a = 1
        
          
           

    def yeni_ekle(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.bind((HOST,PORT))

        self.s.listen(60)
        print("Server Hazırlanıyor...")
        self.a = 1
        while self.a >= 0:
            try:
                print("|+| Server Başladı... ")
                self.SocketServer, self.addr = self.s.accept()
                Thread(target = self.veriVer).start()
            except(Exception):
                print("Sistem çöktü ...")
                SocketServer.close()
                s.close()
            

        SocketServer.close()
        s.close()
        


Server()


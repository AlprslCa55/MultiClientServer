import socket

from threading import Thread


global s


class Cli():
    def veriAl():
        while True:
            data = s.recv(1024)
            data = data.decode('utf-8')
            
            print(data)
            data = ""
           


    def veriVer():
        while True:
            message = input("")
            if "cikis" in message:
                s.close()
                break

            message = message.encode('utf-8')
            s.send(message)






s = socket.socket()

host = '192.168.2.81'

port = 5555

s.connect((host,port))

t1 = Thread(target = Cli.veriAl)
t2 = Thread(target = Cli.veriVer)

t1.start()
t2.start()










            

import socket, threading
from tkinter import *

mesg = 'hey'


def snd():
    client.send(message_entry.get().encode(encoding))
    message_entry.delete(0, END)


def snd2(evnt):
    snd()


def recvs():
    while True:
        mesg = client.recv(1024).decode(encoding)
        msg.configure(text=mesg)
        msg.update()
        msg.pack()
        print(mesg)


def take_input():
    while True:
        txt = input()
        snd(txt)


xy = True

IP = '127.0.0.1'
if xy:
    IP = '192.168.43.4'

IP = socket.gethostbyname(socket.gethostname())

PORT = 8080

ADDRESS = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

encoding = 'utf-8'

client.send("PC___1111".encode("utf-8"))


# client.recv(1024).decode("utf-8")"
def discon():
    client.send('disconn'.encode(encoding))


window = Tk()

msg = Label(text=mesg, font='forte 20')
msg.pack()
threading.Thread(target=recvs).start()
threading.Thread(target=take_input).start()

message_entry = Entry(font='forte 15')
message_entry.pack()

btn = Button(text='Send', command=snd)
btn.pack()
message_entry.bind('<Return>', snd2)

btn2 = Button(text='disconnect', command=discon)
btn2.pack()

window.mainloop()
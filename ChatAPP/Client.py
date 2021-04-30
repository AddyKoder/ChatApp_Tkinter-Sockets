import socket
import threading
from tkinter import *

##################### VARIABLES ########################
###### SOCKETS #######
IP = 0
PORT = 8080
server = 0
encoding = 'utf-8'

height = 650
width = 1150
window_color = 'cyan'

#### GUI COMPONENTS ####
window = 0
control_pane = 0
connection_frame = 0
chat_pane = 0
chat_section = 0
chat_frame = 0
scroll = 0
canvas = 0
last_message = ''

messages = []


def start_server():
    global server


    IP = socket.gethostbyname(socket.gethostname())

    ADDRESS = (IP, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDRESS)

    server.send("Client___1111".encode("utf-8"))

def disconnect():
    server.send('disconn'.encode(encoding))


def recvs():
    global last_message

    while True:
        mesg = server.recv(1024).decode(encoding)

        print(mesg)
        if mesg == 'kick':
            Label(chat_section, text='You were kicked out by the server', font='forte 14', bg=window_color, fg = 'red').pack()

        name, message = mesg.split('___')

        message_frame = Frame(chat_section, bg=window_color)
        if last_message != name:
            Label(message_frame, text=f'{name} : ', font='forte 18', bg=window_color, fg='blue').pack(side=LEFT)
        Label(message_frame, text=f'        {message}', font='forte 18', bg=window_color).pack(side=LEFT)
        message_frame.pack()
        messages.append(message_frame)
        last_message = name

        if len(messages) > 19:
            messages[0].destroy()
            messages.pop(0)




def window_init():
    global window
    window = Tk()
    window.geometry(f'{width}x{height}')
    window.maxsize(width,height)
    window.minsize(width,height)
    window.title('SERVER Control Panel')



def add_chat_pane_components(chat_pane):
    global chat_section, last_message

    def snd(e):
        global last_message
        user_message = entry_section.get()
        entry_section.delete(0,END)

        server.send(user_message.encode(encoding))

        message_frame = Frame(chat_section, bg=window_color)
        if last_message != 'YOU':
            Label(message_frame, text = 'You : ', font='forte 18', bg=window_color, fg='red').pack(side=LEFT)
        Label(message_frame, text=f'        {user_message}', font='forte 18', bg=window_color).pack(side=LEFT)
        message_frame.pack()
        messages.append(message_frame)
        last_message = 'YOU'

        # messages.append(Label(chat_section, text = message, font = 'forte 18', bg = window_color))
        # messages[-1].pack()

        if len(messages) > 19:
            messages[0].destroy()
            messages.pop(0)

    chat_section = Frame(chat_pane, bg = window_color)
    chat_section.pack(fill=BOTH, expand=1)

    # canvas = Canvas(chat_section)
    # canvas.pack(side=LEFT, fill = BOTH, expand = 1)
    #
    # scroll = Scrollbar(chat_section, orient = VERTICAL, command = canvas.yview)
    # scroll.pack(side = RIGHT, fill = Y)
    #
    # canvas.configure(yscrollcommand= scroll.set, bg = window_color)
    # canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion = canvas.bbox('all')))
    #
    # chat_frame = Frame(canvas, bg = window_color)
    #
    # canvas.create_window((0,0),window = chat_frame, anchor = 'nw' )

    entry_section = Entry(chat_pane, bg = 'lightgreen', font='forte 20')
    entry_section.bind('<Return>',snd)
    entry_section.pack(fill = X)




def add_window_components():
    global control_pane, chat_pane

    chat_pane = Frame(window, bg=window_color)
    chat_pane.pack(side=LEFT, fill=BOTH, expand=1)


    add_chat_pane_components(chat_pane)

start_server()
window_init()
threading.Thread(target=recvs).start()
add_window_components()
window.mainloop()
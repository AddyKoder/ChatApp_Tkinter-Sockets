import socket
import threading
from tkinter import *

##################### VARIABLES ########################

###### GUI ######
height = 650
width = 1150
window_color = 'cyan'

#### SOCKETS ####
IP = 0
ADDRESS = 0
server = 0
connections = {}
clientID_label = {}

PORT = 8080
PASSWORD = '1111'
encoding = 'utf-8'

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

###################### METHODS #########################

###### SOCKETS ######

def start_sockets():
    start_server()
    threading.Thread(target=listen_connections).start()
    threading.Thread(target=send_message).start()


def remove_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            dictionary.pop(key)
            break


def send_message():
    while True:
        user_message = '___'.join(['SERVER', input()])
        for c_id, client in connections.items():
            client.send(user_message.encode(encoding))


def send_to_all(name, message, client):
    message = '___'.join([name, message])
    for c_id, client_obj in connections.items():
        if client_obj != client:
            client_obj.send(message.encode(encoding))


def listen_connections():
    client_id = 1
    while True:
        conn, addr = server.accept()

        connections[client_id] = conn
        threading.Thread(target=handle_connection, args=(conn, client_id, addr)).start()
        client_id += 1


def handle_connection(client, c_id, address):
    global last_message

    connected = False
    name = None

    name_pass = client.recv(1024).decode(encoding)
    try:
        name, password = name_pass.split('___')

    except:
        pass

    else:
        if password == PASSWORD:
            connected = True
            print(f'[CONNECTION] :  {name} joined')
            add_client_label(name, c_id)

    while connected:
        try:
            message = client.recv(1024).decode(encoding)
        except:
            remove_client(name, client, c_id)
            return 0

        if message != 'disconn' and message:
            print(f'[{name}] :  {message}')


            message_frame = Frame(chat_section, bg=window_color)
            if last_message != name:
                Label(message_frame, text = f'{name} : ', font = 'forte 18', bg = window_color, fg = 'blue').pack(side = LEFT)
            Label(message_frame, text = f'        {message}', font = 'forte 18', bg = window_color).pack(side = LEFT)
            message_frame.pack()
            messages.append(message_frame)

            # messages.append(Label(chat_section, text = message, font = 'forte 18', bg = window_color))
            # messages[-1].pack()

            if len(messages) > 19:
                messages[0].destroy()
                messages.pop(0)

            send_to_all(name, message, client)
            last_message = name
        else:
            connected = False

    remove_client(name, client, c_id)
    client.send('You were disconnected by the server'.encode(encoding))


def start_server():
    global IP, ADDRESS, server

    IP = socket.gethostbyname(socket.gethostname())
    ADDRESS = (IP, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)

    server.listen(4)


def remove_client(name, client, c_id):
    print(f'[DISCONNECTED] :  {name} left')
    remove_key_by_value(connections, client)
    clientID_label[c_id].destroy()
    clientID_label.pop(c_id)


######## GUI ########

def window_init():
    global window
    window = Tk()
    window.geometry(f'{width}x{height}')
    window.maxsize(width,height)
    window.minsize(width,height)
    window.title('SERVER Control Panel')


def add_client_label(name, c_id):
    def kick_client():
        connections[c_id].send('You were kicked out'.encode(encoding))
        connections[c_id].close()

    frame_color = 'cyan'

    frame_1 = Frame(connection_frame, bg=frame_color, borderwidth=5)

    label = Label(frame_1, text=f'      {name}', bg=frame_color, font='forte 15')
    kick_button = Button(frame_1, text='x', bg='red', fg='white', font='10', command=kick_client, relief=FLAT)

    kick_button.grid(row=0, column=0)
    label.grid(row=0, column=1)
    frame_1.pack(fill=X)
    clientID_label[c_id] = frame_1


def add_control_pane_components(control_pane):
    global connection_frame

    title = Label(control_pane, text='Server Control', font='forte 25', bg=window_color)
    title.pack()

    title_connection = Label(control_pane, text='Connections', font='forte 20', bg=window_color)
    title_connection.pack()

    connection_frame = Frame(control_pane, bg=window_color, pady=30)
    connection_frame.pack(fill=BOTH)


def add_chat_pane_components(chat_pane):
    global chat_section, last_message

    def snd(e):
        global last_message
        user_message = entry_section.get()
        entry_section.delete(0,END)
        for c_id, client in connections.items():
            client.send(user_message.encode(encoding))

        message_frame = Frame(chat_section, bg=window_color)
        if last_message != 'SERVER':
            Label(message_frame, text = 'You : ', font='forte 18', bg=window_color, fg='red').pack(side=LEFT)
        Label(message_frame, text=f'        {user_message}', font='forte 18', bg=window_color).pack(side=LEFT)
        message_frame.pack()
        messages.append(message_frame)
        last_message = 'SERVER'

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

    control_pane = Frame(window, width=250, borderwidth=5, bg=window_color)
    control_pane.pack(side=LEFT, fill=Y)

    border = Frame(window, bg='black', width=3)
    border.pack(side=LEFT, fill=Y)

    chat_pane = Frame(window, bg=window_color)
    chat_pane.pack(side=LEFT, fill=BOTH, expand=1)

    add_control_pane_components(control_pane)
    add_chat_pane_components(chat_pane)


start_sockets()
window_init()
add_window_components()
window.mainloop()

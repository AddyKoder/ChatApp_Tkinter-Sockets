from tkinter import *

result = ''
result_label = 0


def _1():
    global result
    result += '1'
    result_label.configure(text=result)
    result_label.update()
def _2():
    global result
    result += '2'
    result_label.configure(text=result)
    result_label.update()
def _3():
    global result
    result += '3'
    result_label.configure(text=result)
    result_label.update()
def _4():
    global result
    result += '4'
    result_label.configure(text=result)
    result_label.update()
def _5():
    global result
    result += '5'
    result_label.configure(text=result)
    result_label.update()
def _6():
    global result
    result += '6'
    result_label.configure(text=result)
    result_label.update()
def _7():
    global result
    result += '7'
    result_label.configure(text=result)
    result_label.update()
def _8():
    global result
    result += '8'
    result_label.configure(text=result)
    result_label.update()
def _9():
    global result
    result += '9'
    result_label.configure(text=result)
    result_label.update()
def _0():
    global result
    result += '0'
    result_label.configure(text=result)
    result_label.update()
def _p():
    global result
    result += '+'
    result_label.configure(text=result)
    result_label.update()
def _s():
    global result
    result += '-'
    result_label.configure(text=result)
    result_label.update()
def _m():
    global result
    result += '*'
    result_label.configure(text=result)
    result_label.update()
def _bs():
    global result
    
    result = result[0:-1]
    result_label.configure(text=result)
    result_label.update()

def eq():
    global result
    
    result = str(eval(result))
    result_label.configure(text = result)
    result_label.update()








def make_layout():
    global result_label
    result_label = Label(text = result, font = 'forte 35' )
    
    # defining buttons
    btn1 = Button(text='1', font = 'forte 20', width=7, height=2,command=_1)
    btn2 = Button(text='2', font = 'forte 20', width=7, height=2,command = _2)
    btn3 = Button(text='3', font = 'forte 20', width=7, height=2,command = _3)
    
    btn4 = Button(text='4', font = 'forte 20', width=7, height=2,command = _4)
    btn5 = Button(text='5', font = 'forte 20', width=7, height=2,command = _5)
    btn6 = Button(text='6', font = 'forte 20', width=7, height=2,command = _6)
    
    btn7 = Button(text='7', font = 'forte 20', width=7, height=2,command = _7)
    btn8 = Button(text='8', font = 'forte 20', width=7, height=2,command = _8)
    btn9 = Button(text='9', font = 'forte 20', width=7, height=2,command = _9)
    _0
    btn0 = Button(text='0', font = 'forte 20', width=7, height=2,command = _0)
    btneq = Button(text='=', font = 'forte 20', width=7, height=2,command = eq)
    
    btnp = Button(text='+', font = 'forte 20', width=7, height=2,command = _p)
    btns = Button(text='-', font = 'forte 20', width=7, height=2,command = _s)
    btnm = Button(text='x', font = 'forte 20', width=7, height=2,command = _m)
    
    btnbs = Button(text='back', font = 'forte 20', width=7, height=2,command = _bs)
    
    result_label.grid(row = 0 , column=0, columnspan=3)
    
    btn1.grid(row=1,column=0)
    btn2.grid(row=1,column=1)
    btn3.grid(row=1,column=2)
    
    btn4.grid(row=2,column=0)
    btn5.grid(row=2,column=1)
    btn6.grid(row=2,column=2)
    
    btn7.grid(row=3,column=0)
    btn8.grid(row=3,column=1)
    btn9.grid(row=3,column=2)
    
    btn0.grid(row=4,column=0)
    btnbs.grid(row=4, column=1)
    btneq.grid(row=4,column=2)
    
    btnp.grid(row=5,column=0)
    btns.grid(row=5,column=1)
    btnm.grid(row=5,column=2)
    
    
    
    
    

root = Tk()
root.geometry('340x475')
# root.maxsize(340,500)
# root.minsize(340,500)


make_layout()




root.mainloop()
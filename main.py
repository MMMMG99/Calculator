from tkinter import *
DARK_GREEN = '#395b64'
BLACK = '#2c3333'

#definire functii butoane
def adaugare_buton0():
    text = button_0.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton1():
    text = button_1.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton2():
    text = button_2.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton3():
    text = button_3.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton4():
    text = button_4.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton5():
    text = button_5.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton6():
    text = button_6.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton7():
    text = button_7.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton8():
    text = button_8.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton9():
    text = button_9.cget('text')
    introducere_calcule.insert(END, string=text)

def adaugare_buton_point():
    text = point.cget('text')
    introducere_calcule.insert(END, string=text)


def adaugare_buton_plus():
    text = plus.cget('text')
    introducere_calcule.insert(END, string=text)


def adaugare_buton_multiply():
    text = multiply.cget('text')
    introducere_calcule.insert(END, string=text)


def adaugare_buton_divide():
    text = divide.cget('text')
    introducere_calcule.insert(END, string=text)


def adaugare_buton_minus():
    text = minus.cget('text')
    introducere_calcule.insert(END, string=text)

#functia egal care realizeaza si toate operatiile in spate
def adaugare_buton_egal():
    numere = []
    numere_reale = []
    result = 0
    text = introducere_calcule.get()
    semn = ""

    if '+' in text:
        numere = text.split('+')
        semn = "+"
    elif '-' in text:
        numere = text.split('-')
        semn = "-"
    elif 'x' in text:
        numere = text.split('x')
        semn = "x"
    elif '/' in text:
        numere = text.split('/')
        semn = "/"

    for i in numere:
        i = float(i)
        numere_reale.append(i)

    if semn == "+":
        result = numere_reale[0] + numere_reale[1]
    elif semn == '-':
        result = numere_reale[0] - numere_reale[1]
    elif semn == 'x':
        result = numere_reale[0] * numere_reale[1]
        result = round(result, 3)
    elif semn == '/':
        result = numere_reale[0] / numere_reale[1]
        result = round(result, 3)

    introducere_calcule.delete(0, END)
    introducere_calcule.insert(END, string=str(result))

    calcule.config(text=f'{text} = {result}')


#definire interfata grafica
window = Tk()
window.title("Calculator")
window.config(bg=DARK_GREEN, padx=50, pady=50)
window.columnconfigure(1, weight=3)

button_0 = Button(text = '0', height=1, width=4, command=adaugare_buton0)
button_0.grid(row=5, column=0)

button_1 = Button(text = '1', height=1, width=4, command=adaugare_buton1)
button_1.grid(row=4, column=0)

button_2 = Button(text = '2', height=1, width=4, command=adaugare_buton2)
button_2.grid(row=4, column=1)

button_3 = Button(text = '3', height=1, width=4, command=adaugare_buton3)
button_3.grid(row=4, column=2)

button_4 = Button(text = '4', height=1, width=4, command=adaugare_buton4)
button_4.grid(row=3, column=0)

button_5 = Button(text = '5', height=1, width=4, command=adaugare_buton5)
button_5.grid(row=3, column=1)

button_6 = Button(text = '6', height=1, width=4, command=adaugare_buton6)
button_6.grid(row=3, column=2)

button_7 = Button(text = '7', height=1, width=4, command=adaugare_buton7)
button_7.grid(row=2, column=0)

button_8 = Button(text = '8', height=1, width=4, command=adaugare_buton8)
button_8.grid(row=2, column=1)

button_9 = Button(text = '9', height=1, width=4, command=adaugare_buton9)
button_9.grid(row=2, column=2)

point = Button(text = '.', height=1, width=4, command=adaugare_buton_point)
point.grid(row=5, column=1)

plus = Button(text = '+', height=1, width=4, command=adaugare_buton_plus)
plus.grid(row=5, column=2)

equal = Button(text = '=', height=1, width=4, command=adaugare_buton_egal)
equal.grid(row=5, column=3)

minus = Button(text = '-', height=1, width=4, command=adaugare_buton_minus)
minus.grid(row=4, column=3)

multiply = Button(text = 'x', height=1, width=4, command=adaugare_buton_multiply)
multiply.grid(row=3, column=3)

divide = Button(text = '/', height=1, width=4, command=adaugare_buton_divide)
divide.grid(row=2, column=3)

calcule = Label(bg = DARK_GREEN, fg = BLACK, text='')
calcule.grid(row= 1, column= 1, columnspan=4)

introducere_calcule =Entry(width=15)
introducere_calcule.grid(row=0, column=0, columnspan=4)


window.mainloop()
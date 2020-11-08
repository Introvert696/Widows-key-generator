import string
import random
from tkinter import *

#   GWJCG-7C73B-JV8MR-F7GWJ-MCYYG  5 символов 5 строк
def randomLater():
    letTemp = random.choice(string.ascii_uppercase)
    return letTemp


def randomKey():
    i=1
    keyArray=[]
    while i < 26:
        tempLet = randomLater()
        keyArray.append(tempLet)
        if i == 5 or i == 10 or i == 15 or i ==20:
            keyArray.append('-')

        i +=1
    goodKey = ''.join(keyArray)
    return goodKey


def WriteKey(quantity):
    f = open('text.txt', 'a')
    b = 0
    while b < quantity:
        f.write(randomKey() + '\n')
        b+=1
    f.close()
#quantity = int(input("Введите количество ключей: "))


#/////////////////////////////////////////////////////////

def get_elen(event):
    s = ent.get()
    s = int(s)
    texting = WriteKey(s)
    lab['text'] = s , '- Ключ(а,ей) сгенерированно '


# ................................................
root = Tk()

ent = Entry(width=20)
but = Button(text="Преобразовать")
lab = Label(width=30,height=1, bg='black', fg='white')

# temtemp = int(ent)

but.bind('<Button-1>',get_elen)

ent.pack()
but.pack()
lab.pack()
root.mainloop()

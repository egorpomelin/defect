from os import name
import sqlite3
from tkinter import *

def cler(a):
    a.delete(0, END)

def cler1():
    frame.destroy()

def cler2():
    messege.destroy()


def ms(i):
    one = str(i[0])
    two = str(i[1])
    free = str(i[2])
    fo = str(i[3])
    faif = str(i[4])
    one1 = 20 - len(one)
    one2 = '-' * one1
    two1 = 50 - len(two)
    two2 = '-' * two1

    free1 = 30 - len(free)
    free2 = '-' * free1

    fo1 = 30 - len(fo)
    fo2 = '-' * fo1

    faif1 = 30 - len(faif)
    faif2 = '-' * faif1

    mes = one + one2 + two + two2 + free + free2 + fo + fo2 +faif + faif2
    return mes

def VivodSrok(vs):
    cler2()
    messege = Frame()
    messege.place(x = 50, y = 100, width=800, height=650)

    Label1 = Label(text='штрихкод')
    Label1.place(x =50, y = 100, width= 150, height= 25)

    Label2 = Label(text='название')
    Label2.place(x =200, y = 100, width= 200, height= 25)

    Label3 = Label(text='количество')
    Label3.place(x =400, y = 100, width= 100, height= 25)

    Label4 = Label(text='дата поставки')
    Label4.place(x =500, y = 100, width= 150, height= 25)

    Label4 = Label(text='срок годности')
    Label4.place(x =650, y = 100, width= 150, height= 25)

    mesege = Listbox()
    mesege.place(x = 50, y = 125, width=750, height=650)


    scrol = Scrollbar(command=mesege.yview, width=4 )
    scrol.place(x = 800, y = 125, height=650)
    mesege['yscrollcommand'] = scrol.set
    

    b =1
    c = ' '*10
    for i in vs:
        mes = ms(i)
        mesege.insert(END,(b, '.',mes))
        b += 1


def VivodBrak(a):
    cler2()
    messege = Frame()
    messege.place(x = 50, y = 100, width=800, height=650)

    Label1 = Label(text='штрихкод')
    Label1.place(x =50, y = 100, width= 150, height= 25)

    Label2 = Label(text='название')
    Label2.place(x =200, y = 100, width= 200, height= 25)

    Label3 = Label(text='количество')
    Label3.place(x =400, y = 100, width= 100, height= 25)

    Label4 = Label(text='склад')
    Label4.place(x =500, y = 100, width= 150, height= 25)

    Label4 = Label(text='дата нахождения')
    Label4.place(x =650, y = 100, width= 150, height= 25)

    mesege = Listbox()
    mesege.place(x = 50, y = 125, width=750, height=650)

    scrol = Scrollbar(command=mesege.yview, width=4 )
    scrol.place(x = 800, y = 125, height=650)
    mesege['yscrollcommand'] = scrol.set
    
    b =1
    for i in a:
        mes = ms(i)
        mesege.insert(END,(b, '.',mes))
        b += 1

def DabSrok():
    cler1()

    def DabSrok1():
        stri = strih.get()
        nam = name.get()
        coll = col.get()
        data = dat.get()
        sroc = srok.get()
        cursor.execute('''INSERT INTO сроки(штрихкод, название, количество, дата_поставки, срок_годности) VALUES(?, ?, ?, ?, ?)''', (stri, nam, coll, data, sroc))
        db.commit()
        cler(strih)
        cler(name)
        cler(col)
        cler(dat)
        cler(srok)

    frame = Frame()
    frame.place(x = 850, y = 100, width=750, height=700)

    label1 = Label(master = frame, text='штрихкод')
    label1.place(x = 50, y = 0, width=200, height=25)
    strih = Entry(master = frame, text='')
    strih.place(x = 50, y = 25, width=200, height=25)

    label2 = Label(master= frame, text='название')
    label2.place(x = 50, y = 50, width=200, height=25)
    name = Entry(master = frame, text='')
    name.place(x = 50, y = 75, width=200, height=25)

    label3 = Label(master= frame, text='количество')
    label3.place(x = 50, y = 100, width=200, height=25)
    col = Entry(master = frame, text='')
    col.place(x = 50, y = 125, width=200, height=25)

    label4 = Label(master= frame, text='дата поставки')
    label4.place(x = 50, y = 150, width=200, height=25)
    dat = Entry(master = frame, text='')
    dat.place(x = 50, y = 175, width=200, height=25)

    label5 = Label(master= frame, text='срок годности')
    label5.place(x = 50, y = 200, width=200, height=25)
    srok = Entry(master = frame, text='')
    srok.place(x = 50, y = 225, width=200, height=25)
    button = Button(master= frame, text='добавить', command=DabSrok1)
    button.place(x = 50, y = 250, width=200, height=25)
    button['bg'] = 'green'

def DabBrak():
    cler1()

    def DabBrak1():
        stri = strih.get()
        nam = name.get()
        coll = col.get()
        sclad = skl.get()
        data = dat.get()
        cursor.execute('''INSERT INTO брак(штрихкод, название, количество, склад, дата_нахождения) VALUES(?, ?, ?, ?, ?)''', (stri, nam, coll, sclad, data))
        db.commit()
        cler(strih)
        cler(name)
        cler(col)
        cler(skl)
        cler(dat)

    frame = Frame()
    frame.place(x = 850, y = 100, width=750, height=700)

    label1 = Label(master = frame, text='штрихкод')
    label1.place(x = 50, y = 0, width=200, height=25)
    strih = Entry(master = frame, text='')
    strih.place(x = 50, y = 25, width=200, height=25)

    label2 = Label(master= frame, text='название')
    label2.place(x = 50, y = 50, width=200, height=25)
    name = Entry(master = frame, text='')
    name.place(x = 50, y = 75, width=200, height=25)

    label3 = Label(master= frame, text='количество')
    label3.place(x = 50, y = 100, width=200, height=25)
    col = Entry(master = frame, text='')
    col.place(x = 50, y = 125, width=200, height=25)

    label4 = Label(master= frame, text='склад')
    label4.place(x = 50, y = 150, width=200, height=25)
    skl = Entry(master = frame, text='')
    skl.place(x = 50, y = 175, width=200, height=25)

    label5 = Label(master= frame, text='дата нахождения')
    label5.place(x = 50, y = 200, width=200, height=25)
    dat = Entry(master = frame, text='')
    dat.place(x = 50, y = 225, width=200, height=25)
    button = Button(master= frame, text='добавить', command=DabBrak1)
    button.place(x = 50, y = 250, width=200, height=25)
    button['bg'] = 'green'

def VseSrok():
    
    cursor.execute('SELECT * FROM сроки')
    vs = cursor.fetchall()
    VivodSrok(vs)


def VseBrak():

    cursor.execute('SELECT * FROM брак')
    vs = cursor.fetchall()
    VivodBrak(vs)
    
        

def PoiskBrak():
    cler1()
    frame = Frame()
    frame.place(x = 850, y = 100, width=750, height=700)
    def PoiskBrak1():
        
        hud = strih.get()
        cursor.execute('''SELECT * FROM брак WHERE штрихкод =?''', [hud])
        vs = cursor.fetchall()
        VivodBrak(vs)

        cler(strih)

    def PoiskBrak2():
        hud = name.get()
        cursor.execute('''SELECT * FROM брак WHERE название =?''', [hud])
        vs = cursor.fetchall()
        VivodBrak(vs)

        cler(name)

    def PoiskBrak3():
        hud = sclad.get()
        cursor.execute('''SELECT * FROM брак WHERE склад=?''', [hud])
        vs = cursor.fetchall()
        VivodBrak(vs)

        cler(sclad)

    def PoiskBrak4():
        hud = data.get()
        cursor.execute('''SELECT * FROM брак WHERE дата_нахождения=?''', [hud])
        vs = cursor.fetchall()
        VivodBrak(vs)

        cler(data)

    label1 = Label(master = frame, text='штрихкод')
    label1.place(x = 50, y = 0, width=200, height=25)
    strih = Entry(master = frame, text='')
    strih.place(x = 50, y = 25, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak1)
    Button1.place(x = 260, y = 25, width=100, height=25)
    Button1['bg'] = 'green'

    label1 = Label(master = frame, text='название')
    label1.place(x = 50, y = 55, width=200, height=25)
    name = Entry(master = frame, text='')
    name.place(x = 50, y = 80, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak2)
    Button1.place(x = 260, y = 80, width=100, height=25)
    Button1['bg'] = 'green'

    label1 = Label(master = frame, text='склад')
    label1.place(x = 50, y = 110, width=200, height=25)
    sclad = Entry(master = frame, text='')
    sclad.place(x = 50, y = 135, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak3)
    Button1.place(x = 260, y = 135, width=100, height=25)
    Button1['bg'] = 'green'

    label1 = Label(master = frame, text='дата обнаружения')
    label1.place(x = 50, y = 165, width=200, height=25)
    data = Entry(master = frame, text='')
    data.place(x = 50, y = 190, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak4)
    Button1.place(x = 260, y = 190, width=100, height=25)
    Button1['bg'] = 'green'

def PoiskSrok():
    cler1()
    frame = Frame()
    frame.place(x = 850, y = 100, width=750, height=700)
    def PoiskBrak1():
        
        hud = strih.get()
        cursor.execute('''SELECT * FROM сроки WHERE штрихкод =?''', [hud])
        vs = cursor.fetchall()
        VivodSrok(vs)

        cler(strih)

    def PoiskBrak2():
        hud = name.get()
        cursor.execute('''SELECT * FROM сроки WHERE название =?''', [hud])
        vs = cursor.fetchall()
        VivodSrok(vs)

        cler(name)

    def PoiskBrak3():
        hud = sroc.get()
        cursor.execute('''SELECT * FROM сроки WHERE срок_годности=?''', [hud])
        vs = cursor.fetchall()
        VivodSrok(vs)

        cler(sroc)

    def PoiskBrak4():
        hud = data.get()
        cursor.execute('''SELECT * FROM сроки WHERE дата_поставки=?''', [hud])
        vs = cursor.fetchall()
        VivodSrok(vs)

        cler(data)

    label1 = Label(master = frame, text='штрихкод')
    label1.place(x = 50, y = 0, width=200, height=25)
    strih = Entry(master = frame, text='')
    strih.place(x = 50, y = 25, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak1)
    Button1.place(x = 260, y = 25, width=100, height=25)
    Button1['bg'] = 'green'

    label1 = Label(master = frame, text='название')
    label1.place(x = 50, y = 55, width=200, height=25)
    name = Entry(master = frame, text='')
    name.place(x = 50, y = 80, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak2)
    Button1.place(x = 260, y = 80, width=100, height=25)
    Button1['bg'] = 'green'

    label1 = Label(master = frame, text='срок годности')
    label1.place(x = 50, y = 110, width=200, height=25)
    sroc = Entry(master = frame, text='')
    sroc.place(x = 50, y = 135, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak3)
    Button1.place(x = 260, y = 135, width=100, height=25)
    Button1['bg'] = 'green'

    label1 = Label(master = frame, text='дата поставки')
    label1.place(x = 50, y = 165, width=200, height=25)
    data = Entry(master = frame, text='')
    data.place(x = 50, y = 190, width=200, height=25)
    Button1 = Button(master= frame,text='поиск', command=PoiskBrak4)
    Button1.place(x = 260, y = 190, width=100, height=25)
    Button1['bg'] = 'green'

def DeletBrak():
    cler1()

    def DabBrak1():
        stri = strih.get()
        nam = name.get()
        coll = col.get()
        cursor.execute('DELETE FROM брак WHERE название = ? AND склад = ? AND дата_нахождения = ?', (stri, nam, coll))
        db.commit()
        cler(strih)
        cler(name)
        cler(col)
    

    frame = Frame()
    frame.place(x = 850, y = 100, width=750, height=700)

    label1 = Label(master = frame, text='название')
    label1.place(x = 50, y = 0, width=200, height=25)
    strih = Entry(master = frame, text='')
    strih.place(x = 50, y = 25, width=200, height=25)

    label2 = Label(master= frame, text='склад')
    label2.place(x = 50, y = 50, width=200, height=25)
    name = Entry(master = frame, text='')
    name.place(x = 50, y = 75, width=200, height=25)

    label3 = Label(master= frame, text='дата нахождения')
    label3.place(x = 50, y = 100, width=200, height=25)
    col = Entry(master = frame, text='')
    col.place(x = 50, y = 125, width=200, height=25)

    button = Button(master= frame, text='удалить', command=DabBrak1)
    button.place(x = 50, y = 160, width=200, height=25)
    button['bg'] = 'green'


def DeletSrok():
    cler1()

    def DabBrak1():
        stri = strih.get()
        nam = name.get()
        cursor.execute('DELETE FROM сроки WHERE название = ? AND срок_годности = ? ', (stri, nam))
        db.commit()
        cler(strih)
        cler(name)
    

    frame = Frame()
    frame.place(x = 850, y = 100, width=750, height=700)

    label1 = Label(master = frame, text='название')
    label1.place(x = 50, y = 0, width=200, height=25)
    strih = Entry(master = frame, text='')
    strih.place(x = 50, y = 25, width=200, height=25)

    label2 = Label(master= frame, text='срок годности')
    label2.place(x = 50, y = 50, width=200, height=25)
    name = Entry(master = frame, text='')
    name.place(x = 50, y = 75, width=200, height=25)


    button = Button(master= frame, text='удалить', command=DabBrak1)
    button.place(x = 50, y = 110, width=200, height=25)
    button['bg'] = 'green'


with sqlite3.connect('брак.db') as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS сроки(штрихкод integer, название text NOT NULL, количество integer NOT NULL, дата_поставки integer NOT NULL, срок_годности integer NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS брак(штрихкод integer, название text NOT NULL, количество integer NOT NULL, склад text NOT NULL, дата_нахождения text NOT NULL)''')



root = Tk()
root.title('брак и сроки годности')
root.geometry('1600x800')


messege = Frame()
messege.place(x = 50, y = 100, width=800, height=650)

menu1 = Button(text= 'добавить брак', command=DabBrak)
menu1.place(x = 50, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

menu1 = Button(text= 'добавить сроки', command=DabSrok)
menu1.place(x = 160, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

menu1 = Button(text= 'удалить брак', command=DeletBrak)
menu1.place(x = 270, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

menu1 = Button(text= 'удалить сроки', command=DeletSrok)
menu1.place(x = 380, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

menu1 = Button(text= 'поиск брак', command=PoiskBrak)
menu1.place(x = 490, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

menu1 = Button(text= 'поиск сроки', command= PoiskSrok)
menu1.place(x = 600, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

menu1 = Button(text= 'все сроки', command=VseSrok)
menu1.place(x = 710, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

menu1 = Button(text= 'весь брак', command=VseBrak)
menu1.place(x = 820, y = 25, width= 100, height= 25)
menu1['bg'] = 'green'

frame = Frame()
frame.place(x = 850, y = 100, width=750, height=700)
root.mainloop()
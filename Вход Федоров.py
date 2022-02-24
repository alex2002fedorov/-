from tkinter import *
from tkinter import messagebox
font_header = ('Arial Black', 20)
font_entry = ('Times New Roman', 18)
label_font = ('Times New Roman', 16)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 8}
def nach():
    global username_entry,password_entry,o
    o = Tk()
    o.title('Авторизация')
    o.geometry('500x250')
    o.resizable(False, False)
    main_label = Label(o, text='Вход', font=font_header, justify=CENTER, **header_padding)
    username_label = Label(o, text='Логин', font=label_font , **base_padding)
    password_label = Label(o, text='Пароль', font=label_font , **base_padding)
    username_entry = Entry(o, bg='#fff', fg='#444', font=font_entry)
    password_entry = Entry(o, bg='#fff', fg='#444', font=font_entry)
    btn = Button(o, text='Войти', command=vh)
    main_label.pack()
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    btn.pack(**base_padding)
    o.mainloop()
def vh():
    global username_entry,password_entry,o,mis,mis_1
    o.withdraw()
    if username_entry.get()!="" and password_entry.get()!="":
        em_pas=[]
        with open('email.txt', "r") as f:
            for line in f:
                a11=line.split(";")
                em_pas.append(a11)
        ooo=0
        for i in em_pas:
            if username_entry.get()==i[0] and password_entry.get()==i[1]:
                ooo=1
        if ooo==1:
            mis=Toplevel()
            mis.geometry('600x100')
            mis.resizable(False, False)
            mis.title("ВХОД")
            vv = Label(mis, text='Вход произошел', font=font_header, justify=CENTER, **header_padding)
            btn_2 = Button(mis, text='Закрыть',command=ex_1)
            vv.pack()
            btn_2.pack()
            mis.mainloop()
        else:
            mis_1=Toplevel()
            mis_1.geometry('600x100')
            mis_1.resizable(False, False)
            mis_1.title("ОШИБКА")
            vv_1 = Label(mis_1, text='Что-то не так. Попробуйте еще раз', font=font_header, justify=CENTER, **header_padding)
            btn_1 = Button(mis_1, text='Войти',command=ex_2)
            vv_1.pack()
            btn_1.pack()
            mis_1.mainloop()
    else:
        mis_1=Toplevel()
        mis_1.geometry('600x100')
        mis_1.resizable(False, False)
        mis_1.title("ОШИБКА")
        vv_1 = Label(mis_1, text='Что-то не так. Попробуйте еще раз', font=font_header, justify=CENTER, **header_padding)
        btn_1 = Button(mis_1, text='Войти',command=ex_2)
        vv_1.pack()
        btn_1.pack()
        mis_1.mainloop()
def ex_1():
    global mis
    mis.withdraw()
def ex_2():
    global mis_1
    mis_1.withdraw()
    nach()
nach()

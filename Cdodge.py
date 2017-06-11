from Tkinter import *
import ttk as ttk
import tkMessageBox

root = Tk()
root.resizable(0,0)
root.title("CS-dodge BY[error1096]")
s = ttk.Style()
s.theme_names()
s.theme_use('clam')
root.iconbitmap("py.ico")


def help_():  # help DEF

    help_TK = Tk()
    help_TK.title("help")

    Label(help_TK,
          text="for adding keyword use down side text box and past in your KEY").pack()

    help_TK.mainloop()


def error1096():  # error1096 DEF

    error1096_TK = Tk()
    error1096_TK.title("error1096")

    # just simpel label simpel

    Label(error1096_TK, text="""hello \n my name is error1096 \n and im a simpel \n programmer 
if you nead any help contact \n me you can find my email address in \n contact menu """).pack()

    Label(error1096_TK, text="""

                 hello                                                
                   my name                                         
                     is error1096                                      
                      and im a simpel                                     
                        programmer                                    
                        if                                     
                        you nead                                   
                         any help                                  
                           contact                                 
                             me you                                
                              can find                              
                               my email                           
                                address in    
                                
                                contact me 
                               
                               ---------------
                            https://cs-team.in/
                                and thanks to
                                    my 
                                frind :
                                    kiler-TM
                                

""").pack()

    error1096_TK.mainloop()


def contactME():  # contact DEF

    contactME_TK = Tk()
    contactME_TK.title("contact")

    # just simpel label simpel

    Label(contactME_TK, text="my GMAIL :", fg='red').grid(row=0, column=0)
    Label(contactME_TK, text="assasin.shahin@gmail.com", fg='blue').grid(row=0, column=1)

    Label(contactME_TK, text="GIThub :", fg='red').grid(row=1, column=0)
    Label(contactME_TK, text="https://github.com/error1096", fg='blue').grid(row=1, column=1)

    Label(contactME_TK, text="tw&instagram :", fg='red').grid(row=2, column=0)
    Label(contactME_TK, text="error1096", fg='blue').grid(row=2, column=1)

    contactME_TK.mainloop()

root.resizable(0, 0)

menu = Menu(root)  # menu
root.config(menu=menu)

sMENU = Menu(menu)  # sube menu (help menu)
menu.add_cascade(label="Help", menu=sMENU)
sMENU.add_command(label="Help", command=help_)

s1MENU = Menu(menu)  # sube menu (about menu)
menu.add_cascade(label="ABOUT ME", menu=s1MENU)
s1MENU.add_command(label="ERRO1096", command=error1096)  # sube menu 1
s1MENU.add_command(label="CONTACT ME.", command=contactME)  # sube menu 2

textFRAME = ttk.LabelFrame(root,text='~COMBO~')
textFRAME1 = ttk.LabelFrame(root,text='~COMBO~')

S = ttk.Scrollbar(textFRAME)
text = Text(textFRAME,height=15,width=60)
S.pack(side=RIGHT,fill=Y)
text.pack()

S.config(command=text.yview)

text.config(yscrollcommand=S.set)

##################################

S1 = ttk.Scrollbar(textFRAME)
text1 = Text(textFRAME,height=15,width=60)
S1.pack(side=LEFT,fill=Y)
text1.pack()

S1.config(command=text1.yview)

text1.config(yscrollcommand=S.set)

textFRAME.grid(row=0,column=0)
textFRAME1.grid(row=1,column=0)

buttonFRAME = ttk.LabelFrame(root,height=30,width=20,text='Main')
ttk.Label(buttonFRAME,text='split user from password :').grid(row=0,column=0)
ttk.Label(buttonFRAME,text='split combo to list COUNT  :').grid(row=2,column=0)
ttk.Label(buttonFRAME,text='add user/email to password:').grid(row=4,column=0)
ttk.Label(buttonFRAME,text='delet word from pass word:').grid(row=10,column=0)
ttk.Label(buttonFRAME,text='addd @email.com to userlist :').grid(row=6,column=0)

word = StringVar()

def SPLIT():
    Z = text.get("1.0", END)
    z_ = Z.encode('utf-8')
    with open('date.txt', 'w') as v:
        v.write(z_)
    with open('date.txt', 'r') as v:
        with open('user.txt','w') as x :
            with open('pass.txt', 'w') as c:
                V = v.read().split("\n")
                for line in V :
                    try :

                        user = line.split(":")[0]
                        passw = line.split(":")[1]
                        x.write(str(user)+"\n")
                        c.write(str(passw)+"\n")
                    except:
                        pass
                tkMessageBox.showinfo("", "proses is finished")

def DELL():

    try:
        z = text.get('1.0',END)
        x=  z.encode('utf-8')
        I= text1.get('1.0',END)
        i=  I.encode('utf-8')

        with open('date.txt','w') as w :
            w.write(x)

        with open("date.txt") as f:
            contents1, sentinel, contents2 = f.read().partition("cut\n")
        with open("date1.txt", "w") as f:
            f.write(contents1)
        with open("date2.txt", "w") as f:
            f.write(contents2)
    except :
        pass
    tkMessageBox.showinfo("", "proses is finished")

def addU_p ():

    try:

        z = text.get('1.0',END)
        x =  z.encode('utf-8')
        I = text1.get('1.0',END)
        c =  I.encode('utf-8')

        with open("date.txt",'w') as q :
            q.write(x+"\n")
        with open("date1.txt",'w') as q:
            q.write(c+"\n")

        with open("date.txt", 'r') as g:

            l = g.read().split("\n")

            with open("date1.txt", 'r') as p:

                u = p.read().split("\n")

                with open ("userpass.txt",'w') as  w :

                    for user in l :

                        for passw in u :

                            w.write(str(user)+":"+str(passw)+"\n")
    except :
        pass
    tkMessageBox.showinfo("", "proses is finished")
def DEELw():
    z = text.get('1.0',END)
    x=  z.encode('utf-8')
    I= text1.get('1.0',END)
    c=  I.encode('utf-8')
    dell = word.get()
    try:
        with open("date.txt",'w') as q :
            q.write(x+"\n")

        f =open('date.txt','r')
        lines = f.readlines()
        f.close()

        w = open('CPMB0_edi.txt','w')
        for line in lines :
            if line != str(dell)+"\n" :
                w.write(line)
        w.close()
    except:
        pass
    tkMessageBox.showinfo("", "proses is finished")

def ADD_EMAIL():
    dell = word.get()
    z = text.get('1.0',END)
    x=  z.encode('utf-8')

    I= text1.get('1.0',END)
    c=  I.encode('utf-8')


    try:

        with open("date.txt",'w') as q :
            q.write(x+"\n")

        f = open("date.txt",'r')
        lines0 = f.read().split("\n")
        f.close()

        w = open("combo.txt",'w')
        for line in lines0 :
            w.write(str(line)+dell+"\n")
        w.close()
    except:
        pass
    tkMessageBox.showinfo("", "proses is finished")



ttk.Button(buttonFRAME,text='mode1 ',command=SPLIT).grid(row=1,column=0)
ttk.Button(buttonFRAME,text='mode2', command=DELL).grid(row=3,column=0)
ttk.Button(buttonFRAME,text='mode3',command=addU_p).grid(row=5,column=0)
ttk.Button(buttonFRAME,text='mode5',command=ADD_EMAIL).grid(row=8,column=0)
ttk.Button(buttonFRAME,text='mode6',command=DEELw).grid(row=11,column=0)
ttk.Entry(buttonFRAME,textvariable=word).grid(row=12,column=0)
ttk.Label(buttonFRAME,text="""\nCS-dodge\n
for help plass\n
click on help \n
menu :)\n
BY - ERROR1096\n\n""",font='Tim').grid(row=13,column=0)
buttonFRAME.grid(row=0,column=1)

root.mainloop()
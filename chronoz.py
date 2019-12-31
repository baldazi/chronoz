from tkinter import*
fen = Tk()
fen.title("chronoz")
fen.geometry("240x180")
fen.minsize(240,180)
fen.maxsize(320,240)
fen.iconbitmap("chronos.ico")
fen.config(bg = "#c0c0c0")
#_______________________________zone de reperage_________________________
frm = Frame(fen,borderwidth = 2)
#_____________________________fonctions__________________________________    
def stop():
    global t
    t = False
    

def res():
    global sec,mn,hr
    sec,mn,hr = 0,0,0
    snd["text"] = "0" + str(sec)
    mnt["text"] = "0" + str(sec)
    hrs["text"] = "0" + str(sec)
    


def compt():
    global sec,mn,hr,t
    if t == True:
        if sec == 59:
            sec = 0
            mn = mn + 1
        else:
            sec = sec + 1
        if mn == 59:
            mn = 0
            hr = hr + 1
        if hr == 23:
            hr = 0
        if sec <= 9:
            s = "0" + str(sec)
        else:
            s = str(sec)
        if mn <= 9:
            m = "0" + str(mn)
        else:
            m = str(mn)
        if hr <= 9:
            h = "0" + str(hr)
        else:
            h = str(hr)
        snd["text"] = s
        mnt["text"] = m
        hrs["text"] = h
        fen.after(1000,compt)
    t = True
  

#_____________________________valeurs-zeros_____________________________
sec = 0
mn = 0
hr = 0
t = True
#_____________________________composants d'affiche________________________
snd = Label(frm, text = "0" + str(sec),fg = "red", font = ("courrier",30))
mnt = Label(frm, text = "0" + str(mn), font = ("courrier",30))
hrs = Label(frm, text = "0" + str(hr), font = ("courrier",30))
sep1 = Label(frm, text = ":", font = ("courrier",30)).grid(row=0,column=4)
sep2 = Label(frm, text = ":", font = ("courrier",30)).grid(row=0,column=2)
snd.grid(row=0,column=5)
mnt.grid(row=0,column=3)
hrs.grid(row=0,column=1)
#______________________________bouttons_________________________________
but = Button(text = "demarrer", command = compt)
but1 = Button(text = "arreter", command = stop)
but2 = Button(text = "reset", fg = "red", command = res)
but1.pack(side = "bottom",fill = "x")
but2.pack(side = "bottom",fill = "x")
but.pack(side = "bottom",fill = "x")
#_____________________________ouverture__________________________________
frm.pack(side = "top")
fen.mainloop()
#___________________________________________________________________________
#|**************************************************************************|
#|*                    ecrit par: Balde Abdoul Aziz                        *|
#|**************************************************************************|
#|__________________________________________________________________________|

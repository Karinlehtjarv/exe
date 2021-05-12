#ITT20
#Karin Leht-Järv
#Ülesanne 5 kodutöö

#akna tegemine
from tkinter import *
from tkinter import ttk
#panen aknale pealkirja ja 
aken = Tk()
aken.title("Külvamine")
aken.geometry("500x600")
#loon rea, et akent ei saadaks muuta
aken.resizable(0,0)
#Loon aknale ka tervituse
tekstikast = Label(aken, text="Tere külvaja!", width=20, font="Tahoma 12", anchor="w")
tekstikast.grid(row=0, column=1)

nr=0
def OK():
    hektarid = int(sisestus.get())
    sem = rbValue.get()
    hektaridSEM = (hektarid*sem)/1000
    kogus.config(text=hektaridSEM)
    hektarile.config(text=sem)
    
#tekitan tühja rea vahele
tuhikast1 = Label(aken, text="", width=20, font="Tahoma 12", anchor="w")
tuhikast1.grid(row=1, column=1)

#tekitan radiobutton nuppudega valiku võimalused
tekstikast = Label(aken, text="Vali seeme :", width=20, font="Tahoma 12", anchor="w")
tekstikast.grid(row=3, column=0)
rbValue=DoubleVar() #ühine muutuja väärtuste hoidmiseks
vk1 = Radiobutton(aken, text="nisu", value=200, variable=rbValue, font="Tahoma12", anchor="w")
vk1.grid(row=2, column=1, sticky="w")
vk2 = Radiobutton(aken, text="oder", value=160, variable=rbValue,font="Tahoma12", anchor="w" )
vk2.grid(row=3, column=1, sticky="w")
vk1 = Radiobutton(aken, text="kaer", value=180, variable=rbValue, font="Tahoma12", anchor="w")
vk1.grid(row=4, column=1, sticky="w")
vk2 = Radiobutton(aken, text="uba", value=230, variable=rbValue,font="Tahoma12", anchor="w" )
vk2.grid(row=5, column=1, sticky="w")


#loon sisestusvälja
tekstikast = Label(aken, text="Vali hektarid :", width=20, font="Tahoma 12", anchor="w")
tekstikast.grid(row=6, column=0, pady=(20,0))
sisestus = Entry(aken, width=20, font="Tahoma 12")
sisestus.grid(row=6, column=1, pady=(20.0))

#loon nupu, mis käivitab funktsioonid
nupp = Button(aken, text="OK", width=10, font="Tahoma12", command=OK)
nupp.grid(row=7, column=1, padx=2, pady=2)

#lisan eraldusriba 
separator = ttk.Separator(aken, orient="horizontal")
separator.grid(row=8, column=0, columnspan=2, sticky="ew", padx=20)

#loon vastusevälja
tekstikast = Label(aken, text="Vilja 1 ha kohta :", width=20, font="Tahoma12", anchor="w")
tekstikast.grid(row=9, column=0)
hektarile = Label(aken, text="0.0kg", width=20, font="Tahoma12", anchor="w")
hektarile.grid(row=9, column=1)
tekstikast5 = Label(aken, text="kg", width=20, font="Tahoma 12", anchor="w")
tekstikast5.grid(row=9, column=2, pady=(20,0))
#teine vastuseväli
tekstikast = Label(aken, text="Seemet vaja:", width=20, font="Tahoma12", anchor="w")
tekstikast.grid(row=10, column=0)
kogus = Label(aken, text="0.0kg", width=20, font="Tahoma12", anchor="w")
kogus.grid(row=10, column=1)
tekstikast5 = Label(aken, text="t", width=20, font="Tahoma 12", anchor="w")
tekstikast5.grid(row=10, column=2, pady=(20,0))

aken.mainloop

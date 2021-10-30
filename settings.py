from tkinter import *
import csv
import os.path
import os
import platform

if platform.system() == "Windows":
    cpc = 1
elif platform.system() == "Linux":
    cpc = 2
elif platform.system() == "macOS":
    cpc = 3
else:
    cpc = 4


bgc = "light grey"
fc = "black"

setwindow = Tk()
setwindow.geometry("700x300")
setwindow.title("Settings")
setwindow.configure(background=bgc)
setwindow.resizable(width=False, height=False)
if cpc == 1:
    setwindow.iconbitmap('data/varia.ico')

# rows
row1 = 25
row2 = 50
row3 = 75
row4 = 100
row5 = 125
row6 = 160
row7 = 195
row8 = 255

# columns
column_l = 75
column_s = 275
column_c = 550

frame1 = LabelFrame(setwindow, text="Set Configuration", font=('arial', 10, 'bold'), height=275, width=250, bg=bgc)
frame1.place(x=column_s, y=150, anchor="center")

frame2 = LabelFrame(setwindow, text="Current Configuration", font=('arial', 10, 'bold'), height=275, width=250, bg=bgc)
frame2.place(x=column_c, y=150, anchor="center")


# font
l_font = ('arial', 10, 'bold')
t_font = ('arial', 15, 'bold')

b_width = 30

cong_f = 'data/data_txt/cong_name.txt'
zmw_f = 'data/data_txt/midweek_id.txt'
zwe_f = 'data/data_txt/weekend_id.txt'
nbl_f = 'data/data_txt/noticeboard_link.txt'
cl_f = 'data/data_txt/zoom_client.txt'
cm_f = 'data/data_txt/colour_mode.txt'

def read():
    cong = open(cong_f, "r").read()
    mw_id = open(zmw_f, "r").read()
    we_id = open(zwe_f, "r").read()
    nbl = open(nbl_f, "r").read()
    cl_mode = open(cl_f, "r").read()
    cm_mode = open(cm_f, "r").read()
    if int(cl_mode) == 1:
        client = "Web Client"
    else:
        client = "Zoom App"
    if int(cm_mode) == 1:
        mode = "Light Mode"
        bgc = "light grey"
        fc = "black"
    else:
        mode = "Dark Mode"
        bgc = "grey12"
        fc = "white"

    c_cong = Label(setwindow, text=cong, bg=bgc, fg=fc, justify="center", font=l_font, width=30)
    c_cong.place(x=column_c, y=row2, anchor="center")

    c_mw_id = Label(setwindow, text=mw_id, bg=bgc, fg=fc, justify="center", font=l_font, width=30)
    c_mw_id.place(x=column_c, y=row3, anchor="center")

    c_we_id = Label(setwindow, text=we_id, bg=bgc, fg=fc, justify="center", font=l_font, width=30)
    c_we_id.place(x=column_c, y=row4, anchor="center")

    c_nbl = Label(setwindow, text=nbl, bg=bgc, fg=fc, justify="center", font=l_font, width=30)
    c_nbl.place(x=column_c, y=row5, anchor="center")

    c_client = Label(setwindow, text=client, bg=bgc, fg=fc, justify="center", font=l_font, width=30)
    c_client.place(x=column_c, y=row6, anchor="center")

    c_cm = Label(setwindow, text=mode, bg=bgc, fg=fc, justify="center", font=l_font, width=30)
    c_cm.place(x=column_c, y=row7, anchor="center")
    cong_l.config(bg=bgc, fg=fc)
    zml.config(bg=bgc, fg=fc)
    zwl.config(bg=bgc, fg=fc)
    nbt.config(bg=bgc, fg=fc)
    client_l.config(bg=bgc, fg=fc)
    mode_l.config(bg=bgc, fg=fc)
    entbutton.config(bg=bgc, fg=fc)
    setwindow.config(bg=bgc)
    frame1.config(bg=bgc, fg=fc)
    frame2.config(bg=bgc, fg=fc)


def setconfig():
    if len(cong_ent.get()) > 0:
        if os.path.isfile(cong_f):
            os.remove(cong_f)
        with open(cong_f, "x") as f1:
            f1.writelines(str(cong_ent.get()))
            f1.close()

    if len(zm_ent.get()) > 0:
        if os.path.isfile(zmw_f):
            os.remove(zmw_f)
        with open(zmw_f, "x") as f2:
            f2.writelines(str(zm_ent.get()))
            f2.close()

    if len(zw_ent.get()) > 0:
        if os.path.isfile(zwe_f):
            os.remove(zwe_f)
        with open(zwe_f, "x") as f3:
            f3.writelines(str(zw_ent.get()))
            f3.close()

    if len(nb_ent.get()) > 0:
        if os.path.isfile(nbl_f):
            os.remove(nbl_f)
        with open(nbl_f, "x") as f4:
            f4.writelines(str(nb_ent.get()))
            f4.close()


    if os.path.isfile(cl_f):
        os.remove(cl_f)
    with open(cl_f, "x") as f5:
        if variable.get() == "Web Client":
            c_g = 1
        else:
            c_g = 0
        f5.writelines(str(c_g))
        f5.close()

    if os.path.isfile(cm_f):
        os.remove(cm_f)
    with open(cm_f, "x") as f6:
        if variable2.get() == "Light Mode":
            m_g = 1
        else:
            m_g = 0
        f6.writelines(str(m_g))
        f6.close()
    read()


cong_l = Label(setwindow, text="Congregation Name", bg=bgc, fg="black", font=l_font)
cong_l.place(x=column_l, y=row2, anchor="center")
cong_ent = Entry(setwindow, justify="center", width=b_width, font=l_font)
cong_ent.place(x=column_s, y=row2, anchor="center")

zml = Label(setwindow, text="Zoom Midweek ID", bg=bgc, fg="black", justify="center", font=l_font)
zml.place(x=column_l, y=row3, anchor="center")
zm_ent = Entry(setwindow, justify="center", width=b_width, font=l_font)
zm_ent.place(x=column_s, y=row3, anchor="center")

zwl = Label(setwindow, text="Zoom Weekend ID", bg=bgc, fg="black", justify="center", font=l_font)
zwl.place(x=column_l, y=row4, anchor="center")
zw_ent = Entry(setwindow, justify="center", width=b_width, font=l_font)
zw_ent.place(x=column_s, y=row4, anchor="center")

nbt = Label(setwindow, text="Noticeboard Link", bg=bgc, fg="black", justify="center", font=l_font)
nbt.place(x=column_l, y=row5, anchor="center")
nb_ent = Entry(setwindow, justify="center", width=b_width, font=l_font)
nb_ent.place(x=column_s, y=row5, anchor="center")

client_l = Label(setwindow, text="Client", bg=bgc, fg="black", justify="center", font=l_font)
client_l.place(x=column_l, y=row6, anchor="center")
options = ["Web Client","Zoom App"]
variable = StringVar(setwindow)
variable.set(options[0])
client_ent = OptionMenu(setwindow, variable, *options)
client_ent.place(x=column_s, y=row6, anchor="center")

mode_l = Label(setwindow, text="Colour Mode", bg=bgc, fg="black", justify="center", font=l_font)
mode_l.place(x=column_l, y=row7, anchor="center")

options2 = ["Light Mode","Dark Mode"]
variable2 = StringVar(setwindow)
variable2.set(options2[0])
mode_ent = OptionMenu(setwindow, variable2, *options2)
mode_ent.place(x=column_s, y=row7, anchor="center")



entbutton = Button(setwindow, text="Set new data", justify="center", font=('arial', 10, 'bold'), command=setconfig)
entbutton.place(x=column_s, y=row8, anchor="center")

if __name__ == '__main__':
    #read()
    setwindow.mainloop()
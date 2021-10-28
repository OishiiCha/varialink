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
    setwindow.iconbitmap('data/links.ico')

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

frame1 = LabelFrame(setwindow,
                    text="Set Configuration",
                    font=('arial', 10, 'bold'),
                    height=275,
                    width=250,
                    bg=bgc)
frame1.place(x=column_s,
             y=150,
             anchor="center")

frame2 = LabelFrame(setwindow,
                    text="Current Configuration",
                    font=('arial', 10, 'bold'),
                    height=275,
                    width=250,
                    bg=bgc)
frame2.place(x=column_c,
             y=150,
             anchor="center")


# font
l_font = ('arial', 10, 'bold')
t_font = ('arial', 15, 'bold')

b_width = 30

file = 'data/data.csv'


def read():
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            line.append(line)

    cong = str(line[1])
    mw_id = str(line[3])
    we_id = str(line[5])
    nbl = str(line[7])
    if int(line[9]) == 1:
        client = "Web Client"
    else:
        client = "Zoom App"
    if int(line[11]) == 1:
        mode = "Light Mode"
        bgc = "light grey"
        fc = "black"
    else:
        mode = "Dark Mode"
        bgc = "grey12"
        fc = "white"

    c_cong = Label(setwindow,
                   text=cong,
                   bg=bgc,
                   fg=fc,
                   justify="center",
                   font=l_font,
                   width=30)
    c_cong.place(x=column_c,
                 y=row2,
                 anchor="center")

    c_mw_id = Label(setwindow,
                    text=mw_id,
                    bg=bgc,
                    fg=fc,
                    justify="center",
                    font=l_font,
                    width=30)
    c_mw_id.place(x=column_c,
                  y=row3,
                  anchor="center")

    c_we_id = Label(setwindow,
                    text=we_id,
                    bg=bgc,
                    fg=fc,
                    justify="center",
                    font=l_font,
                    width=30)
    c_we_id.place(x=column_c,
                  y=row4,
                  anchor="center")

    c_nbl = Label(setwindow,
                  text=nbl,
                  bg=bgc,
                  fg=fc,
                  justify="center",
                  font=l_font,
                  width=30)
    c_nbl.place(x=column_c,
                y=row5,
                anchor="center")

    c_client = Label(setwindow,
                     text=client,
                     bg=bgc,
                     fg=fc,
                     justify="center",
                     font=l_font,
                     width=30)
    c_client.place(x=column_c,
                   y=row6,
                   anchor="center")

    c_cm = Label(setwindow,
                 text=mode,
                 bg=bgc,
                 fg=fc,
                 justify="center",
                 font=l_font,
                 width=30)
    c_cm.place(x=column_c,
               y=row7,
               anchor="center")
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
    if os.path.isfile(file):
        os.remove(file)
    f = open(file, "x", newline="")
    cong_g = str(cong_ent.get())
    zm_g = str(zm_ent.get())
    zw_g = str(zw_ent.get())
    nbl_g = str(nb_ent.get())
    if variable.get() == "Web Client":
        c_g = 1
    else:
        c_g = 0
    if variable2.get() == "Light Mode":
        m_g = 1
    else:
        m_g = 0

    new_data_string = ("congregation",
                       cong_g,
                       "zoom id (midweek)",
                       zm_g,"zoom id (weekend)",
                       zw_g,"noticeboard",
                       nbl_g,
                       "client",
                       c_g,
                       "colour",
                       m_g)
    writer = csv.writer(f)
    writer.writerow(new_data_string)
    f.close()
    read()


cong_l = Label(setwindow,
               text="Congregation Name",
               bg=bgc,
               fg="black",
               font=l_font)
cong_l.place(x=column_l,
             y=row2,
             anchor="center")
cong_ent = Entry(setwindow,
                 justify="center",
                 width=b_width,
                 font=l_font)
cong_ent.place(x=column_s,
               y=row2,
               anchor="center")

zml = Label(setwindow,
            text="Zoom Midweek ID",
            bg=bgc,
            fg="black",
            justify="center",
            font=l_font)
zml.place(x=column_l,
          y=row3,
          anchor="center")
zm_ent = Entry(setwindow,
               justify="center",
               width=b_width,
               font=l_font)
zm_ent.place(x=column_s,
             y=row3,
             anchor="center")

zwl = Label(setwindow,
            text="Zoom Weekend ID",
            bg=bgc,
            fg="black",
            justify="center",
            font=l_font)
zwl.place(x=column_l,
          y=row4,
          anchor="center")
zw_ent = Entry(setwindow,
               justify="center",
               width=b_width,
               font=l_font)
zw_ent.place(x=column_s,
             y=row4,
             anchor="center")

nbt = Label(setwindow,
            text="Noticeboard Link",
            bg=bgc,
            fg="black",
            justify="center",
            font=l_font)
nbt.place(x=column_l,
          y=row5,
          anchor="center")
nb_ent = Entry(setwindow,
               justify="center",
               width=b_width,
               font=l_font)
nb_ent.place(x=column_s,
             y=row5,
             anchor="center")

client_l = Label(setwindow,
                 text="Client",
                 bg=bgc,
                 fg="black",
                 justify="center",
                 font=l_font)
client_l.place(x=column_l,
               y=row6,
               anchor="center")
options = ["Web Client","Zoom App"]
variable = StringVar(setwindow)
variable.set(options[0])
client_ent = OptionMenu(setwindow,
                        variable,
                        *options)
client_ent.place(x=column_s,
                 y=row6,
                 anchor="center")

mode_l = Label(setwindow,
                 text="Colour Mode",
                 bg=bgc,
                 fg="black",
                 justify="center",
                 font=l_font)
mode_l.place(x=column_l,
               y=row7,
               anchor="center")

options2 = ["Light Mode","Dark Mode"]
variable2 = StringVar(setwindow)
variable2.set(options2[0])
mode_ent = OptionMenu(setwindow,
                        variable2,
                        *options2)
mode_ent.place(x=column_s,
                 y=row7,
                 anchor="center")



entbutton = Button(setwindow,
                   text="Set new data",
                   justify="center",
                   font=('arial', 10, 'bold'),
                   command=setconfig)
entbutton.place(x=column_s,
                y=row8,
                anchor="center")

if __name__ == '__main__':
    read()
    setwindow.mainloop()
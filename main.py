from tkinter import *
import webbrowser
from time import strftime
from PIL import ImageTk, Image
from datetime import date
import calendar
import csv

# Data
filename = "data/data.csv"
lines = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvreader:
        line.append(line)

if int(line[11]) == 1:
    mysetting = 1
    directory = "data/icons/light_mode/"
    bgc = "lightsteelblue"
    bc = "lightsteelblue3"
    fc = "black"
else:
    mysetting = 0
    directory = "data/icons/dark_mode/"
    bgc = "grey12"
    bc = "grey18"
    fc = "white"


class Win(Tk):

    def __init__(self,master=None):
        Tk.__init__(self,master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)

    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y


win = Win()


windowWidth = 600
windowHeight = 520
win.geometry(str(windowWidth)+"x"+str(windowHeight))
positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(win.winfo_screenheight()/2 - windowHeight/2)
win.geometry("+{}+{}".format(positionRight, positionDown))
win.configure(bg=bgc)
win.resizable(width=False, height=False)
win.iconbitmap('data/links.ico')

xb = Button(win, text="x", width=3, bg=bgc, fg=fc, font=('arial', 25, 'bold'), borderwidth=0, highlightthickness=0, activebackground=bgc, command=win.destroy)
xb.place(x=windowWidth, y=0, anchor="ne")


if int(str(line[9])):
    web_client = "https://pwa.zoom.us/wc/join/"
else:
    web_client = "https://pwa.zoom.us/j/"

def jw_org():
    jw_org_link = "https://jw.org"
    webbrowser.open(jw_org_link, 1)

def wol():
    wol_link = "https://wol.jw.org"
    webbrowser.open(wol_link, 1)

def zoom_mw():
    zoom_link = str(web_client+str(line[3]))
    # https://pwa.zoom.us/wc/join/ --Meeting ID
    webbrowser.open(zoom_link)

def zoom_we():
    zoom_link = str(web_client+str(line[5]))
    # https://pwa.zoom.us/wc/join/ --Meeting ID
    webbrowser.open(zoom_link)

def notice():
    notice_link = str(line[7])
    webbrowser.open(notice_link)

def meeting_choice():
    if calendar.day_name[date.today().weekday()] in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        zoom_mw()
    else:
        zoom_we()

width_i = 320
height_i = 100

jw_photo = Image.open(str(directory+"jw_lrg.png"))
jw_r = jw_photo.resize((width_i, height_i), Image.ANTIALIAS)
jw_image = ImageTk.PhotoImage(jw_r)

wol_photo = Image.open(str(directory+"wol_lrg.png"))
wol_r = wol_photo.resize((width_i, height_i), Image.ANTIALIAS)
wol_image = ImageTk.PhotoImage(wol_r)

zoom_photo = Image.open(str(directory+"zoom_lrg.png"))
zoom_r = zoom_photo.resize((width_i, height_i), Image.ANTIALIAS)
zoom_image = ImageTk.PhotoImage(zoom_r)

notice_photo = Image.open(str(directory+"notice_lrg.png"))
notice_r = notice_photo.resize((width_i, height_i), Image.ANTIALIAS)
notice_image = ImageTk.PhotoImage(notice_r)


# Buttons
b_width = 14
button_frame = Frame(win, height=450, width=330, bg=bgc)
button_frame.place(x=190, y=275, anchor="center")

row1 = int((450/30)*5)
row2 = int((450/30)*12)
row3 = int((450/30)*19)
row4 = int((450/30)*26)
b_col = int(330/2)

jw_org = Button(button_frame, image=jw_image, bg=bc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=jw_org)
jw_org.place(x=b_col, y=row1, anchor="center")

wol = Button(button_frame, image=wol_image, bg=bc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=wol)
wol.place(x=b_col, y=row2, anchor="center")

zoom = Button(button_frame, image=zoom_image, bg=bc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=meeting_choice)
zoom.place(x=b_col, y=row3, anchor="center")

noticeboard = Button(button_frame, image=notice_image, bg=bc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=notice)
noticeboard.place(x=b_col, y=row4, anchor="center")


# Time frame
def timed():
    string = strftime('%I:%M:%S %p\n\n%A\n%d %B\n%Y')
    clock_text.config(text=string)
    clock_text.after(1000, timed)

tframe = Frame(win, height=300, width=200, bg=bgc)
tframe.place(x=480, y=int(windowHeight/2), anchor="center")
clock_text = Label(tframe, bg=bgc, fg=fc, font=('calibri', 25))
clock_text.place(x=str(200/2), y=100, anchor="center")

mytitle = Label(win, text=str(line[1]), font=('calibri', 25, 'bold'), bg=bgc, fg=fc)
mytitle.place(x=30, y=10, anchor="nw")

if __name__ == '__main__':
    timed()
    win.mainloop()
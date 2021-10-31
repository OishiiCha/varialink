from tkinter import *
import webbrowser
from time import strftime
from PIL import ImageTk, Image
from datetime import date
import calendar
import platform


# Data
cong_f = 'data/data_txt/cong_name.txt'
zmw_f = 'data/data_txt/midweek_id.txt'
zwe_f = 'data/data_txt/weekend_id.txt'
nbl_f = 'data/data_txt/noticeboard_link.txt'
cl_f = 'data/data_txt/zoom_client.txt'
cm_f = 'data/data_txt/colour_mode.txt'

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


win = Tk()


windowWidth = 600
windowHeight = 520
win.geometry(str(windowWidth)+"x"+str(windowHeight))
positionRight = int(win.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(win.winfo_screenheight()/2 - windowHeight/2)
win.geometry("+{}+{}".format(positionRight, positionDown))
win.title("VariaLink")
win.configure(bg=bgc)
win.resizable(width=False, height=False)
if platform.system() == "Windows":
    win.iconbitmap('data/varia.ico')


if str(client) == "Web Client":
    web_client = "https://pwa.zoom.us/wc/join/"
else:
    web_client = "https://pwa.zoom.us/j/"

def newsroom_link():
    news_link = "https://www.jw.org/en/news/jw/"
    webbrowser.open(news_link, 1)

def jw_org():
    jw_org_link = "https://jw.org"
    webbrowser.open(jw_org_link, 1)

def wol():
    wol_link = "https://wol.jw.org"
    webbrowser.open(wol_link, 1)

def zoom_mw():
    zoom_link = str(web_client+str(mw_id))
    # https://pwa.zoom.us/wc/join/ --Meeting ID
    webbrowser.open(zoom_link)

def zoom_we():
    zoom_link = str(web_client+str(we_id))
    # https://pwa.zoom.us/wc/join/ --Meeting ID
    webbrowser.open(zoom_link)

def notice():
    notice_link = str(nbl)
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

newsroom_p = Image.open(str(directory+"newsroom.png"))
newsroom_r = newsroom_p.resize((80, 80), Image.ANTIALIAS)
newsroom_image = ImageTk.PhotoImage(newsroom_r)


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
clock_text = Label(tframe, bg=bgc, fg=fc, font=('calibri', 20))
if platform.system() == "Windows":
    clock_text.config(font=('calibri', 25))
clock_text.place(x=str(200/2), y=100, anchor="center")

mytitle = Label(win, text=str(cong), font=('calibri', 20, 'bold'), bg=bgc, fg=fc)
if platform.system() == "Windows":
    mytitle.config(font=('calibri', 25))
mytitle.place(x=30, y=10, anchor="nw")

nr = Button(win, image=newsroom_image, bg=bgc, borderwidth=0, highlightthickness=0, activebackground=bgc, command=newsroom_link)
nr.place(x=windowWidth-30, y=windowHeight-30, anchor="se")

if __name__ == '__main__':
    timed()
    win.mainloop()
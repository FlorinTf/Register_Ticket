import os
import smtplib
import imghdr
from email.message import EmailMessage
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageFont, ImageDraw
from tkinter import messagebox
from tkinter import filedialog
import win32api


root = Tk()
root.title("Register Now")
root.config(bg="#2ca9d8")
root.geometry("500x700")
root.resizable(width=False,height=False)
oras=[]
nume=[]
prenume=[]
tel=[]
mail=[]
loc=[]

def value():
    global nume1
    global prenume1

    nume1= name.get()
    nume1=nume1.upper()
    prenume1=first_name.get()
    prenume1=prenume1.upper()
    mail1=email.get()
    tel1=phone.get()

    def corect_choice():
        def num():
            try:
                int(nume1)
                messagebox.showerror("Error","Only letters")
                nume.clear()
            except ValueError:
                if name.get() in '!@#$%^&*()_+" "':
                    nume.clear()
                    messagebox.showerror("Error", "Insert your name")
                else:
                    pass

        def pre():
            global prenume1
            try:
                int(prenume1)
                messagebox.showerror("Error","Only letters")
                nume.clear()
            except ValueError:
                if first_name.get() in '!@#$%^&*()_+" "':
                    prenume.clear()
                    messagebox.showerror("Error", "Insert your name")
                elif len(tel1) < 10:
                    messagebox.showerror("Error", "Please insert phone")
                elif ".com" not in email.get():
                    messagebox.showerror("Error", "Please insert e-mail adress")
                elif "@" not in email.get():
                    messagebox.showerror("Error", "Please insert e-mail adress")
                elif oras == []:
                    messagebox.showerror("Error", "Please select the city")
                elif loc == []:
                    messagebox.showerror("Error", "Please select a seat")

                    nume1 = name.get()
                    nume1 = nume1.upper()

                    prenume1 = first_name.get()
                    prenume1 = prenume1.upper()

                else:
                    tel.append(tel1)
                    mail.append(mail1)

                    top = Toplevel()
                    top.geometry("600x500")
                    my_menu = Menu(top)
                    top.config(menu=my_menu)

                    def text_on():
                        global image
                        global prenume1
                        global nume1
                        global city1
                        image = Image.open("blank_ticket.png")
                        text_font = ImageFont.truetype("arial.ttf",16)
                        text_to_add = str(nume1)+("  ")+ (prenume1)
                        text_city = oras[0]
                        text_loc = loc[0]

                        edit_img = ImageDraw.Draw(image)
                        edit_img.text((45,88),text_to_add,"white",text_font)
                        edit_img.text((120, 125), text_city, "white", text_font)
                        edit_img.text((150, 160), text_loc, "white", text_font)
                        edit_img.text((470, 25), str(nume1), "white", text_font)
                        edit_img.text((470, 55), str(prenume1), "white", text_font)
                        edit_img.text((470, 80), text_city, "white", text_font)
                        edit_img.text((470, 105), text_loc, "white", text_font)

                        image.save("ticket.png")
                        bg_label.after(2000, show_pic)

                    def show_pic():
                        global image2
                        image2= PhotoImage(file="ticket.png")
                        bg_label.config(image=image2)

                    def print_ticket():

                        file_to_print = filedialog.askopenfilename(initialdir="/Receptie",
                                                                   title="Select a file", filetypes=(
                            ("png files", "*.png"), ("all files", "*.*")))
                        if file_to_print:
                            win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


                    def send_email():
                        global nume1

                        EMAIL_PASSWORD = os.environ.get('password')

                        msg = EmailMessage()
                        msg["Subject"] = "Your ticket for Dj Python"
                        msg["From"] = "code.python2022@gmail.com"
                        msg["To"] = mail1
                        msg.set_content(f"Hello {nume1} ! Thank you for registering. Attached is the entry ticket with the data you filled in. Have fun!")

                        with open("ticket.png", "rb") as f:
                            file_data = f.read()
                            file_type = imghdr.what(f.name)
                            file_name = f.name

                        msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            smtp.login("code.python2022@gmail.com", EMAIL_PASSWORD)

                            smtp.send_message(msg)

                    file_menu = Menu(my_menu)
                    my_menu.add_cascade(label="File",menu=file_menu)
                    file_menu.add_command(label="Print",command=print_ticket)
                    file_menu.add_separator()
                    file_menu.add_command(label="Send email",command=send_email)

                    bg = PhotoImage(file="blank_ticket.png")
                    bg_label = Label(top,image=bg, anchor = 'nw')
                    bg_label.place(x=0,y=0, relwidth = 1, relheight = 1)

                    text_on()
                    top.mainloop()

        num()
        pre()

    corect_choice()

info = Label(root, text= "Hello! Thank you for choosing our services\n"
                              "Please fill in the following form! \n"
                              "At the end you will be able to print the ticket\n"
                         " and you will receive it attached in the confirmation email.",bg="#2ca9d8", font=("Arial",12,"bold"))
info.place(x=50, y=10)

name_lbl = Label(root, text="Name",bg="#2ca9d8",font=("Arial",16,"bold"))
name_lbl.place(x=20, y=100)
name = Entry(root,width= 10, font=("Arial",16))
name.place(x=200, y=100)
first_nameL = Label(root, text="First name",bg="#2ca9d8",font=("Arial",16,"bold"))
first_nameL.place(x= 20, y=160)
first_name = Entry(root,width= 10, font=("Arial",16))
first_name.place(x=200, y=160)
tel_l = Label(root, text="Phone",bg="#2ca9d8",font=("Arial",16,"bold"))
tel_l.place(x=20, y=220)
phone = Entry(root,width= 12, font=("Arial",16))
phone.place(x=200, y=220)
mail_l = Label(root, text="E-mail",bg="#2ca9d8",font=("Arial",16,"bold"))
mail_l.place(x=20, y=280)
email = Entry(root,width= 22, font=("Arial",16))
email.place(x=200, y=280)

def selected(event):

    city = Label(root, text=city_e.get(), font=("Arial",16))
    city1= city_e.get()
    oras.append(city1)

options = [
    "Bucuresti",
    "Constanta",
    "Galati",
    "Timisoara",]

def selected2(event2):
    loc_lb = Label(root, text=loc_e.get(), font=("Arial", 16))
    loc1 = loc_e.get()
    loc.append(loc1)

motivex = [
        "Front",
        "Back",
        "Vip 1",
        "Backstage",]

city_l = Label(root,text="City",bg="#2ca9d8",font=("Arial",16,"bold"))
city_l.place(x=20, y=340)

loc_lbl = Label(root, text="Seat",bg="#2ca9d8",font=("Arial",16,"bold"))
loc_lbl.place(x=20 , y=400)

city_e = ttk.Combobox(root, value=options, width=9,font=("Arial",16))
city_e.insert(0,"Select")
city_e.bind("<<ComboboxSelected>>", selected)
city_e.place(x=197, y=340)

loc_e = ttk.Combobox(root, value=motivex, width=9,font=("Arial",16))
loc_e.insert(0,"Select")
loc_e.bind("<<ComboboxSelected>>",selected2)
loc_e.place(x=197, y=400)

enter_btn = PhotoImage(file="Register Buttons.png")
img_label = Label(root,bg="#2ca9d8", image=enter_btn)

button = Button(root, image=enter_btn,bg="#2ca9d8",borderwidth=0,command=value)
button.place(x=100, y=530)

root.mainloop()

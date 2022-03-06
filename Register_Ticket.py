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



from tkinter import *
from tkinter import filedialog,messagebox
import os
from PIL import Image, ImageTk
import time
from zipfile import ZipFile
from ntpath import join
from posixpath import split
from colorama import *
import time
mixer.init()
os.system('cls')
path = os.path.dirname(__file__)
root = Tk()
root.title('Creak_zip')
Numoffiles = 0
nameoffiles = []
address_logo = os.path.join(path,'data/hacker_logo.png')
mixer.init()
mixer.music.load(join(path,r"data/true.mp3"))
def exit_program():
    while True :
        d = input()
def start():
    label_error.pack_forget()
    button_refresh.pack_forget()
    try:
        img= Image.open(address_logo)
        tryimg()
    except:
        no_logo()
def top_level_4():
    label_msg.pack_forget()
    label_none_2.pack_forget()
    button_next_2.pack_forget()
    list_box.pack_forget()
    label_action = Label(root,text=' ',font=('OCR A Extended',50),pady=120)
    label_action.pack()
    root.update()
    label_action.config(text='3')
    root.update()
    time.sleep(1)
    root.update()
    label_action.config(text='2')
    root.update()
    time.sleep(1)
    root.update()
    label_action.config(text='1')
    root.update()
    time.sleep(1)
    root.update()
    label_action.config(text='Starting')
    time.sleep(1)
    root.update()
    label_action.config(text='Activity In Concol',font=('OCR A Extended',25))
    date_now = int(time.time())
    
    files_old = os.listdir(path)
    for k in nameoffiles :
        print(Fore.YELLOW+'\nopen Password List :{}\n'.format(k))
        try:
            file = open(k,"r+").read().split()
        except:
            messagebox.showerror('ERROR','File {} Yaft Nashod !'.format(k))
            break
        for password in file :
            
            try:
                file_for_creak = ZipFile(str(root.filename))
                file_for_creak.extractall(path,pwd=password.encode())
                files_new = os.listdir(path)
                for v in files_new :
                    if v in files_old :
                        pass
                    else:
                        joining = join(path,v)
                        os.remove(joining)
                
                date_now_2 = int(time.time())
                result_time = (date_now_2 - date_now)/10
                print(Fore.YELLOW+"\n[+]"+Fore.GREEN,'password found it : {}'.format(password))
                print(Fore.YELLOW+"\n[#]"+Fore.BLUE,'Run Time : {} second'.format(result_time))

                label_none_2.pack()
                messagebox.showinfo('True','Password Found')
                label_action.config(text='Password Found',fg='green',font=('Arial Rounded MT Bold',36),pady=15)
                password_found = Label(text='Password Is : {}'.format(password),fg='magenta',font=('Arial Rounded MT Bold',20))
                password_found.pack()
                runtime_password = Label(text='Run Time : {}'.format(result_time),fg='darkorange',font=('Arial Rounded MT Bold',20))
                runtime_password.pack()
                org = Label(text='Coded By : Mr_Alone',font=('Segoe Print',15),fg='black')
                org.pack(side='bottom')


                exit_program()
            except RuntimeError:
                print(Fore.YELLOW+"[-]"+Fore.RED,'password not found : {}'.format(password))
    messagebox.showerror('False','Password Not Found')
    label_action.config(text='Password Not Found',fg='red',font=('OCR A Extended',25))
    print(Fore.RED+"\n Password Not Found ")
def top_level_3():
    global label_files
    global buthon_no
    global buthon_yes
    global label_msg
    global label_none_2
    global button_next_2
    global list_box
    butthon_next.pack_forget()
    path = os.path.dirname(os.path.abspath(__file__))
    list_of_passes = os.listdir(path)
    for fp in list_of_passes : # Tabdil esm file ha be esm kamel

    
        address = os.path.join(path,fp)
        ext = os.path.splitext(fp)[-1].lower()
        
        if  ext == '.txt' :
            nameoffiles.append((address))
            
    logo.pack_forget()
    Label_name.pack_forget()
    label_msg = Label(root,text='your Passwords List Are : ',font=('OCR A Extended',16),pady=20)
    label_msg.pack()
    list_box = Listbox(root)
    
    
    list_box.pack(fill=X)
    

    for hl in nameoffiles :
        list_box.insert(END,hl)
    label_none_2 = Label(root,text=' ',pady=15)
    label_none_2.pack()
    button_next_2 = Button(root,text='Next',font=('OCR A Extended',13),bg='black',fg='white',width=15,bd=7,command=top_level_4,pady=20)
    button_next_2.pack()
def top_level_2():
    global butthon_next
    global filename
    messagebox.showinfo('select file','Please Select Zip File')
    root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select zip file",filetypes=[('Zip File', '*.zip')])
    root.update()
    if bool(root.filename) == False:
        top_level_2()
    if bool(root.filename) == True:
        butthon_select_file.pack_forget()
        messagebox.showinfo('Info','Lotfan Password List Hara Dar Pooshe Barname ghara Dade Va "Next" Ra Bezanid')
    
        butthon_next = Button(root,text='Next',font=('OCR A Extended',16),bg='gray',fg='black',width=15,bd=7,pady=20,command=top_level_3)
        butthon_next.pack()
def top_level_1():
    global label_none
    global butthon_select_file
    global Label_name
    Label_name = Label(root,text='Coded By Mr_Alone',font=('OCR A Extended',16))
    Label_name.pack()

    label_none = Label(root,text=' ',pady=35)
    label_none.pack()

    butthon_select_file = Button(root,text='Select File',font=('OCR A Extended',13),bg='black',fg='white',width=15,bd=7,command=top_level_2,pady=20)
    butthon_select_file.pack()
def no_logo():
    global label_error
    global button_refresh
    label_error = Label(root,text='Logo Program Is Not find !',font=('OCR A Extended',16),pady=50)
    label_error.pack()
    button_refresh = Button(root,text='Refresh',font=('OCR A Extended',13),bg='black',fg='white',width=15,bd=7,pady=20,command=start)
    button_refresh.pack()
def tryimg():
    global img
    global photo
    global logo
    img= Image.open(address_logo)
    img = img.resize((200,200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    logo = Label(image=photo)
    logo.pack()
    top_level_1()
try:
    img= Image.open(address_logo)
    print()
    tryimg()
except:
    no_logo()
root.minsize(500,500)
root.maxsize(500,500)
root.mainloop()







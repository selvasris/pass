# Author : Selvasri
# Code : creating "Password gener" using python with the help of tkinter GUI module & pyperclip-copy,paste module


#importing modules (tkinter,pyperclip)
from tkinter import * 
import string 
import random 
import pyperclip 

#execution of called function

#generating password

def generator():
    small_letter=string.ascii_lowercase 
    capital_letter=string.ascii_uppercase 
    numbers=string.digits 
    special_characters=string.punctuation

    all=small_letter+capital_letter+numbers+special_characters
    password_length=int(length_Box.get()) 

    if choice.get()==1:
      passwordField.insert(0,random.sample(small_letter,password_length)) 
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_letter+capital_letter,password_length)) 
    if choice.get()==3:
       passwordField.insert(0,random.sample(all,password_length)) 

# coping the password      

def copy():
    random_password=passwordField.get() 
    pyperclip.copy(random_password) 



#creating app interface

app=Tk() 
app.config(bg='#1A5276') 
choice=IntVar() 
Font=('Georgia',13,'bold') 
passwordLabel=Label(app,text='Password Generator',font=('architectural',20,'bold'),fg="#3A75E9",bg="#FFFFFF") 
passwordLabel.grid(pady=10) 

#creating buttons type

weakradioButton=Radiobutton(app,text='Weak',value=1,variable=choice,font=Font) 
weakradioButton.grid(pady=5) 

mediumradioButton=Radiobutton(app,text='Medium',value=2,variable=choice,font=Font) 
mediumradioButton.grid(pady=5) 

strongradioButton=Radiobutton(app,text='Strong',value=3,variable=choice,font=Font) 
strongradioButton.grid(pady=5) 

#creating lable,length_Box,generateButton,passwordField,copyButton

lengthLabel=Label(app,text='Password Length',font=Font,bg='red',fg='white') 
lengthLabel.grid(pady=5) 

length_Box=Spinbox(app,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(app,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5) 

passwordField=Entry(app,width=25,bd=2,font=Font)
passwordField.grid() 

copyButton=Button(app,text='Copy',font=Font,command=copy) 
copyButton.grid(pady=5)


app.mainloop()
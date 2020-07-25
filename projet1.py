#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.2
#  in conjunction with Tcl version 8.6
#    Jul 25, 2020 12:07:58 AM IST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import projet1_support
from tkinter import messagebox as mb
from tkinter import StringVar

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel2 (root)
    projet1_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel2(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel2(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel2 (w)
    projet1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel2():
    global w
    w.destroy()
    w = None

class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {URW Palladio L} -size 11 -underline 1"
        font11 = "-family {URW Palladio L} -size 10 -underline 1"
        font12 = "-family {URW Palladio L} -size 10"
        font13 = "-family {URW Palladio L} -size 9"
        font9 = "-family {URW Palladio L} -size 11"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("816x573+214+82")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Report Card App")
        top.configure(background="#ffffff")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.257, rely=0.017, height=64, width=393)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(borderwidth="6")
        self.Label1.configure(font="-family {URW Gothic L} -size 14 -weight bold")
        self.Label1.configure(text='''Report Card''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.038, rely=0.14, relheight=0.759, relwidth=0.382)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="6")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.317, rely=0.048,height=32, relwidth=0.5)
        self.Entry1.configure(background="white")
        self.Entry1.configure(borderwidth="4")
        self.Entry1.configure(font="TkFixedFont")

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.064, rely=0.172, height=34, width=74)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(borderwidth="2")
        self.Label3.configure(font="-family {URW Palladio L} -size 11")
        self.Label3.configure(text='''Name :''')

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.317, rely=0.172,height=32, relwidth=0.5)
        self.Entry2.configure(background="white")
        self.Entry2.configure(borderwidth="4")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.032, rely=0.297, height=33, width=74)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(background="#ffffff")
        self.Label4.configure(borderwidth="2")
        self.Label4.configure(font="-family {URW Palladio L} -size 11")
        self.Label4.configure(text='''Class :''')

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.247, rely=0.297,height=32, relwidth=0.212)
        self.Entry3.configure(background="white")
        self.Entry3.configure(borderwidth="4")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")

        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry4.place(relx=0.683, rely=0.297,height=32, relwidth=0.212)
        self.Entry4.configure(background="white")
        self.Entry4.configure(borderwidth="4")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(selectbackground="#c4c4c4")

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.465, rely=0.297, height=33, width=65)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(background="#ffffff")
        self.Label5.configure(borderwidth="2")
        self.Label5.configure(cursor="fleur")
        self.Label5.configure(font="-family {URW Palladio L} -size 11")
        self.Label5.configure(text='''Sec :''')

        self.Labelframe1 = tk.LabelFrame(self.Frame1)
        self.Labelframe1.place(relx=0.032, rely=0.375, relheight=0.577
                , relwidth=0.929)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(font=font10)
        self.Labelframe1.configure(text='''Marks''')
        self.Labelframe1.configure(background="#ffffff")

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.034, rely=0.159, height=33, width=74
                , bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(background="#ffffff")
        self.Label6.configure(borderwidth="2")
        self.Label6.configure(font="-family {URW Palladio L} -size 11")
        self.Label6.configure(text='''Sub1 :''')

        self.Label7 = tk.Label(self.Labelframe1)
        self.Label7.place(relx=0.434, rely=0.159, height=33, width=74
                , bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(background="#ffffff")
        self.Label7.configure(borderwidth="2")
        self.Label7.configure(font="-family {URW Palladio L} -size 11")
        self.Label7.configure(text='''Sub2 :''')

        self.Label8 = tk.Label(self.Labelframe1)
        self.Label8.place(relx=0.034, rely=0.359, height=33, width=74
                , bordermode='ignore')
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(background="#ffffff")
        self.Label8.configure(borderwidth="2")
        self.Label8.configure(font="-family {URW Palladio L} -size 11")
        self.Label8.configure(text='''Sub3 :''')

        self.Label9 = tk.Label(self.Labelframe1)
        self.Label9.place(relx=0.434, rely=0.359, height=33, width=74
                , bordermode='ignore')
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(background="#ffffff")
        self.Label9.configure(borderwidth="2")
        self.Label9.configure(font="-family {URW Palladio L} -size 11")
        self.Label9.configure(text='''Sub4 :''')

        self.Label10 = tk.Label(self.Labelframe1)
        self.Label10.place(relx=0.034, rely=0.558, height=33, width=74
                , bordermode='ignore')
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(background="#ffffff")
        self.Label10.configure(borderwidth="2")
        self.Label10.configure(font="-family {URW Palladio L} -size 11")
        self.Label10.configure(text='''Sub5 :''')

        self.Label11 = tk.Label(self.Labelframe1)
        self.Label11.place(relx=0.434, rely=0.558, height=33, width=74
                , bordermode='ignore')
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(background="#ffffff")
        self.Label11.configure(borderwidth="2")
        self.Label11.configure(font="-family {URW Palladio L} -size 11")
        self.Label11.configure(text='''Sub6 :''')

        self.Label12 = tk.Label(self.Labelframe1)
        self.Label12.place(relx=0.034, rely=0.757, height=33, width=74
                , bordermode='ignore')
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(background="#ffffff")
        self.Label12.configure(borderwidth="2")
        self.Label12.configure(font="-family {URW Palladio L} -size 11")
        self.Label12.configure(text='''Total :''')

        self.Label13 = tk.Label(self.Labelframe1)
        self.Label13.place(relx=0.434, rely=0.757, height=33, width=74
                , bordermode='ignore')
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(background="#ffffff")
        self.Label13.configure(borderwidth="2")
        self.Label13.configure(font="-family {URW Palladio L} -size 11")
        self.Label13.configure(text='''%-age :''')

        self.Entry5 = tk.Entry(self.Labelframe1)
        self.Entry5.place(relx=0.234, rely=0.159, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(borderwidth="4")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(selectbackground="#c4c4c4")

        self.Entry6 = tk.Entry(self.Labelframe1)
        self.Entry6.place(relx=0.666, rely=0.159, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry6.configure(background="white")
        self.Entry6.configure(borderwidth="4")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(selectbackground="#c4c4c4")

        self.Entry7 = tk.Entry(self.Labelframe1)
        self.Entry7.place(relx=0.234, rely=0.359, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry7.configure(background="white")
        self.Entry7.configure(borderwidth="4")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(selectbackground="#c4c4c4")

        self.Entry8 = tk.Entry(self.Labelframe1)
        self.Entry8.place(relx=0.666, rely=0.359, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry8.configure(background="white")
        self.Entry8.configure(borderwidth="4")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(selectbackground="#c4c4c4")

        self.Entry9 = tk.Entry(self.Labelframe1)
        self.Entry9.place(relx=0.234, rely=0.558, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry9.configure(background="white")
        self.Entry9.configure(borderwidth="4")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(selectbackground="#c4c4c4")

        self.Entry10 = tk.Entry(self.Labelframe1)
        self.Entry10.place(relx=0.666, rely=0.558, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry10.configure(background="white")
        self.Entry10.configure(borderwidth="4")
        self.Entry10.configure(font="TkFixedFont")
        self.Entry10.configure(selectbackground="#c4c4c4")

        self.Entry11 = tk.Entry(self.Labelframe1)
        self.Entry11.place(relx=0.234, rely=0.757, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry11.configure(background="white")
        # configure entry11 state as readonly
        self.Entry11.configure(state="readonly")
        self.Entry11.configure(borderwidth="4")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(selectbackground="#c4c4c4")

        self.Entry12 = tk.Entry(self.Labelframe1)
        self.Entry12.place(relx=0.666, rely=0.757, height=32, relwidth=0.228
                , bordermode='ignore')
        self.Entry12.configure(background="white")

        # configure entry12 state as readonly
        self.Entry12.configure(state="readonly")
        self.Entry12.configure(borderwidth="4")

        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(selectbackground="#c4c4c4")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.063, rely=0.175, height=31, width=77)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(borderwidth="2")
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''Roll no :''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.074, rely=0.908, height=34, width=59)
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(font=font13)
        self.Button1.configure(text='''Add''')
        # add student details 
        def addStudent(self):
            #clear total and %-age field
            self.Entry11.delete(0,tk.END)
            self.Entry12.delete(0,tk.END)

            #fetch the roll no 
            rollno=self.Entry1.get()
            #if the rollno is empty then the data cannot be entered.
            if rollno=="":
                #import messagebox from tkinter
                mb.showinfo(title="Data error",message="Some fields are Empty")

            else:
                #create 2 values of stringvar() 
                # import StringVar() from tkinter
                value1=StringVar()
                value2=StringVar()
                #calculate the total of 6 subjects
                totalvalue=int(self.Entry5.get())+int(self.Entry6.get())+int(self.Entry7.get())+int(self.Entry8.get())
                +int(self.Entry9.get())+int(self.Entry10.get())
                
                # now make total and %-age field as non editable
                self.Entry11.configure(textvariable=value1,foreground="black")
                self.Entry12.configure(textvariable=value2,foreground="black")
                
                #calculate the percentage
                per=(totalvalue/600)*100
                
                # i need only 2 decimal value after a decimal
                dper="{:.2f}".format(per)
                
                # append percent symbol to the value obtained.
                finalper=str(dper)+"%"

                #now set these sum and percentage values to their respective entryfields
                
                value2.set(finalper)
                value1.set(str(totalvalue))

                #now lets store the student details in their respective student rollno file
                rollno_file=rollno[0:10]+".txt"

                #now i need a seperate folder to store all the files
                #import join function from os
                from os.path import join as pjoin

                #place your own path and create a folder named studentFiles 

                path_to_file=pjoin("/","home","lonewolf","srcs_project","studentFiles",rollno_file)

                #now open the rollno file and enter the entries in it.
                with open(path_to_file,"w") as wr:
                    wr.write("Student RollNo:"+str(self.Entry1.get())+"\n"+
                        "Student Name:"+str(self.Entry2.get())+"\n"+
                        "Class:"+str(self.Entry3.get())+"\n"+
                        "Sec:"+str(self.Entry4.get())+"\n"+
                        "Sub1:"+str(self.Entry5.get())+"\n"+
                        "Sub2:"+str(self.Entry6.get())+"\n"+
                        "Sub3:"+str(self.Entry7.get())+"\n"+
                        "Sub4:"+str(self.Entry8.get())+"\n"+
                        "Sub5:"+str(self.Entry9.get())+"\n"+
                        "Sub6:"+str(self.Entry10.get())+"\n"+
                        "Total:"+str(self.Entry11.get())+"\n"+
                        "Percentage:"+str(self.Entry12.get())+"\n")
                    #show a dialog showing data added successfully
                    mb.showinfo(title="Data Storing",message="Student Detail Added")
                    wr.close()

        # call the function when add button is pressed.
        self.Button1.configure(command=lambda : addStudent(self))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.184, rely=0.908, height=33, width=63)
        self.Button2.configure(borderwidth="3")
        self.Button2.configure(font=font12)
        self.Button2.configure(text='''Clear''')
        def clearDetails(self):
            self.Entry1.delete(0,tk.END)
            self.Entry2.delete(0,tk.END)
            self.Entry3.delete(0,tk.END)
            self.Entry4.delete(0,tk.END)
            self.Entry5.delete(0,tk.END)
            self.Entry6.delete(0,tk.END)
            self.Entry7.delete(0,tk.END)
            self.Entry8.delete(0,tk.END)
            self.Entry9.delete(0,tk.END)
            self.Entry10.delete(0,tk.END)
            self.Entry11.delete(0,tk.END)
            self.Entry12.delete(0,tk.END)

        self.Button2.configure(command=lambda:clearDetails(self))    

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.306, rely=0.908, height=33, width=59)
        self.Button3.configure(borderwidth="3")
        self.Button3.configure(font=font12)
        self.Button3.configure(text='''Delete''')
        def deleteStudent(self):
            import os
            #to delete file fetch the rollno from entry1
            delFile=self.Entry1.get()
            if os.path.isfile('/home/lonewolf/srcs_project/studentFiles/'+delFile+'.txt')==True:
                os.remove('/home/lonewolf/srcs_project/studentFiles/'+delFile+'.txt')
                mb.showinfo(title="Data Deletion",message="Data Deleted")
            else:
                mb.showinfo(title="File Not Found",message="No Data Found")
    
        self.Button3.configure(command=lambda:deleteStudent(self))
        self.TSeparator2 = ttk.Separator(top)
        self.TSeparator2.place(relx=0.453, rely=0.14, relheight=0.75)
        self.TSeparator2.configure(orient="vertical")

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.478, rely=0.122, relheight=0.777
                , relwidth=0.477)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(borderwidth="4")
        self.Labelframe2.configure(font=font11)
        self.Labelframe2.configure(text='''VeiwData''')
        self.Labelframe2.configure(background="#ffffff")

        self.Text1 = tk.Text(self.Labelframe2)
        self.Text1.place(relx=0.026, rely=0.045, relheight=0.935, relwidth=0.53
                , bordermode='ignore')
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(wrap="word")

        self.Listbox1 = tk.Listbox(self.Labelframe2)
        self.Listbox1.place(relx=0.566, rely=0.045, relheight=0.926
                , relwidth=0.396, bordermode='ignore')
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="TkFixedFont")

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.49, rely=0.908, height=29, width=375)
        self.Button4.configure(borderwidth="3")
        self.Button4.configure(font=font12)
        self.Button4.configure(text='''View Data''')
        def viewData(self):
            self.Listbox1.delete(0,tk.END)
            import os
            flist=os.listdir('/home/lonewolf/srcs_project/studentFiles/')
            flist.sort()
            for item in flist:
                self.Listbox1.insert(tk.END,item)

        def showContent(event):
            x=self.Listbox1.curselection()[0]
            file=self.Listbox1.get(x)
            from os.path import join as pjoin
            pathfile=pjoin("/","home","lonewolf","srcs_project","studentFiles/"+file)
            with open(pathfile,'r') as file:
                file=file.read()
            self.Text1.delete('1.0',tk.END)
            self.Text1.insert(tk.END,file)
        self.Listbox1.bind("<<ListboxSelect>>",showContent)
        self.Button4.configure(command=lambda:viewData(self))                

if __name__ == '__main__':
    vp_start_gui()






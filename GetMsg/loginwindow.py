# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:26:09 2019
@author: adminster
"""
import tkinter as tk
import tkinter.messagebox
import pickle
from mailusr import MailUser
import  sys
from client import Client
from siglot import *
import mainwindow
from newthread import MyThread
from function.MainWindow import *
#窗口
from function.FramelessMainWindow import FramelessMainWindow
import os
import os.path
# 获取Windows平台临时文件夹
path = os.getenv('temp')
filename = os.path.join(path, 'info.txt')

window=tk.Tk()
window.title('欢迎使用九龙湖邮管队')
window.geometry('420x550+500+200')
window.resizable(0,0)
#画布放置图片
window.resizable(0,0)
tk.Label(window,text='Spam',fg='white',anchor='n',bg='FireBrick',font=('Ink Free',50),width=420,height=550).pack()
imageMail=tk.PhotoImage(file='mail.png')
imageLock=tk.PhotoImage(file='lock.png')
tk.Label(window,image=imageMail).place(x=50,y=125)
tk.Label(window,image=imageLock).place(x=55,y=200)
#标签 用户名密码
#用户名输入框
var_usr_name=tk.StringVar(window,value='')
entry_usr_name=tk.Entry(window,textvariable=var_usr_name,font=('Arial', 30),relief='solid',bg='DarkRed',width=10,bd=1)
entry_usr_name.place(x=100,y=120)
#密码输入框
var_usr_pwd=tk.StringVar(window,value='')
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*',font=('Arial', 30),bg='DarkRed',width=10,bd=1)
entry_usr_pwd.place(x=100,y=200)
try:
        with open(filename,'r') as fp:
           n, p = fp.read().strip().split(',')
           var_usr_name.set(n)
           var_usr_pwd.set(p)
except:
      pass     

#登录函数
def usr_log_in():
    #输入框获取用户名密码
    usr_name=var_usr_name.get()
    usr_pwd=var_usr_pwd.get()
    #从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    #判断用户名和密码是否匹配
    mailusr=MailUser(usr_name,usr_pwd)
    sta = mailusr.login(usr_name,usr_pwd)
    if sta == "not connected":
            tk.messagebox.showerror(title='警告',message='请检查账号或网络连接状态')
    elif sta == 'login fail':
            tk.messagebox.showerror(message='账号或密码错误')

    elif sta == 'login success':

            tk.messagebox.showinfo(title="欢迎",message="登录成功")
            if usr_command==1:
             with open(filename, 'w') as fp:
               fp.write(','.join((usr_name,usr_pwd)))
            window.destroy()

            app = mainwindow.QtWidgets.QApplication(sys.argv)

            clisock=Client()
            clisock.sendUsr(usr_name)

            mailusr.getmails()
            num=mailusr.getmailnum()
            for i in range(0,num):
                key=mailusr.getkey(i)

                result=mailwrite.compare(usr_name,key)
                if result==2:
                    send=mailusr.mailsender(i)
                    clisock.sendfrom(usr_name,send)
                    rs=clisock.get_sender()
                    #print(rs)
                    if rs=='1':
                        mailusr.setlabel(i, False)
                    elif rs=='2':
                        mailusr.setlabel(i,True)
                    elif rs=='3':
                        test=mailusr.mailtext(i)
                        clisock.sendmail(test)
                        #label=classify(test)
                        label=clisock.getresult()
                        print('测试内容  ',test,  "结果  " ,label)
                        mailusr.setlabel(i,label)
                else:
                    mailusr.setlabel(i, result)



            signal = SiganlObj()
            slot = TypeSlot()
            signal.sendMsg.connect(slot.get)


            ui = FramelessMainWindow(mailusr, clisock)

            ui.mainwindow.setUserName(usr_name)
            ui.show()
            newthread=MyThread(mailusr,signal,clisock)
            newthread.start()
            sys.exit(app.exec_())


    
def usr_sign_quit():
    window.destroy()
    
def usr_command():
    if(var.get()==1):
        return 1
    else:
        return 0    

#登录 按钮
bt_login=tk.Button(window,text='Login',width='16',height='1',font=('Ink Free', 17),anchor='center',cursor='hand2',command=usr_log_in,bg='LightCyan')
bt_login.place(x=100,y=310)
bt_logquit=tk.Button(window,text='Exit',width='16',height='1',font=('Ink Free', 17),anchor='center',cursor='hand2',command=usr_sign_quit,bg='LightCyan')
bt_logquit.place(x=100,y=390)
var=tk.IntVar()
bt_reme =tk.Checkbutton(window,text='记住密码',bg='FireBrick',variable=var,onvalue=1,offvalue=0,command=usr_command)
bt_reme.place(x=100,y=250)
#主循环
window.mainloop()


#imunylwkvtkhgjgc








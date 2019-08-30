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
from signal import SiganlObj
from signal import TypeSlot
from newthread import MyThread
from function.MainWindow import *
#窗口

window=tk.Tk()
window.title('欢迎使用九龙湖邮管队')
window.geometry('450x300')
window.resizable(0,0)
#画布放置图片
canvas=tk.Canvas(window,height=300,width=500)
imagefile=tk.PhotoImage(file='1.png')
image=canvas.create_image(-1,-30,anchor='nw',image=imagefile)
canvas.pack(side='top')
window.wm_attributes('-topmost',1)
#标签 用户名密码
tk.Label(window,text='用户名:').place(x=100,y=150)
tk.Label(window,text='密码:').place(x=100,y=190)
#用户名输入框
var_usr_name=tk.StringVar()
entry_usr_name=tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
#密码输入框
var_usr_pwd=tk.StringVar()
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=190)


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
            tk.messagebox.showerror(title='警告',message='网络未连接：')
    elif sta == 'login fail':
            tk.messagebox.showerror(message='密码错误')

    elif sta == 'login success':

            tk.messagebox.showinfo(title="欢迎",message="登录成功")
            window.destroy()

            app = mainwindow.QtWidgets.QApplication(sys.argv)

            clisock=Client()
            clisock.sendUsr(usr_name)

            mailusr.getmails()
            num=mailusr.getmailnum()
            for i in range(0,num):
                test=mailusr.mailtext(i)
                clisock.sendmail(test)
                #label=classify(test)
                label=clisock.getresult()
                print('测试内容  ',test,  "结果  " ,label)
                mailusr.setlabel(i,label)

            signal = SiganlObj()
            slot = TypeSlot()
            signal.sendMsg.connect(slot.get)


            ui=UI_MainWindow(mailusr,clisock)

            ui.setUserName(usr_name)
            ui.show()
            newthread=MyThread(mailusr,signal,clisock)
            newthread.start()
            sys.exit(app.exec_())


    
def usr_sign_quit():
    window.destroy()

#登录 按钮
bt_login=tk.Button(window,text='登录',command=usr_log_in)
bt_login.place(x=140,y=230)
bt_logquit=tk.Button(window,text='退出',command=usr_sign_quit)
bt_logquit.place(x=280,y=230)
#主循环
window.mainloop()


#imunylwkvtkhgjgc








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
from function.FramelessWindow import FramelessWindow
import os
import os.path
# 获取Windows平台临时文件夹
path = os.getenv('temp')
filename = os.path.join(path, 'info.txt')

window=tk.Tk()
window.title('欢迎使用九龙湖邮管队')
window.geometry('720x400+500+200')
window.resizable(0,0)
#画布放置图片
window.resizable(0,0)
frmlt=tk.Frame(window,width=360,height=450,bg='black')
frmlt.grid(row=0,column=0)
canvas1=tk.Canvas(window,height=450,width=360)
imagefile1=tk.PhotoImage(file='fina.png')
image=canvas1.create_image(0,-20,anchor='nw',image=imagefile1)
canvas1.grid(row=0,column=0)
canvas2=tk.Canvas(window,height=450,width=360)
imagefile2=tk.PhotoImage(file='3.png')
image=canvas2.create_image(0,0,anchor='nw',image=imagefile2)
canvas2.grid(row=0,column=1)
window.wm_attributes('-topmost',1)
#标签 用户名密码
#用户名输入框
var_usr_name=tk.StringVar(window,value='')
entry_usr_name=tk.Entry(window,textvariable=var_usr_name,bg='white')
entry_usr_name.place(x=360,y=78)
#密码输入框
var_usr_pwd=tk.StringVar(window,value='')
entry_usr_pwd=tk.Entry(window,textvariable=var_usr_pwd,show='*',bg='white')
entry_usr_pwd.place(x=510,y=78)
def pwd_reme():
   if(var.get()==1):
        with open(filename,'r') as fp:
           n, p = fp.read().strip().split(',')
           var_usr_name.set(n)
           var_usr_pwd.set(p)
   else:
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
            tk.messagebox.showerror(title='警告',message='网络未连接')
    elif sta == 'login fail':
            tk.messagebox.showerror(message='密码错误')

    elif sta == 'login success':

            tk.messagebox.showinfo(title="欢迎",message="登录成功")
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


            ui = FramelessWindow(mailusr, clisock)

            ui.mainwindow.setUserName(usr_name)
            ui.show()
            ui.showCenter()
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
var=tk.IntVar()
bt_reme =tk.Checkbutton(window,text='记录上次登录信息',variable=var,onvalue=1,offvalue=0,command=pwd_reme)
bt_reme.place(x=360,y=105)
#主循环
window.mainloop()


#imunylwkvtkhgjgc








import pickle



def write(diclist):
    mw = open("mails.pkl", 'wb')
    str = pickle.dump(diclist,mw)
    mw.close()


def read():
    mr=open("mails.pkl",'rb')
    diclist=pickle.load(mr)
    print(diclist)
    mr.close()
    return diclist


def compare(mail):
    dic=read()
    t=dic.get(mail,2)
    print(t)
    return t



if __name__=='__main__':


    read()



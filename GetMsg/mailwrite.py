import pickle



def write(usr,diclist):
    str=usr+'.pkl'
    mw = open(str, 'wb')
    str = pickle.dump(diclist,mw)
    mw.close()


def read(usr):
    str=usr+'.pkl'
    mr=open(str,'rb')
    diclist=pickle.load(mr)
    #print(diclist)
    mr.close()
    return diclist


def compare(usr,mail):
    try:
      dic=read(usr)
    except FileNotFoundError:
      return 2
    t=dic.get(mail,2)
    print(t)
    return t



if __name__=='__main__':


    read()



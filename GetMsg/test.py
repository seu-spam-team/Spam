# -*- coding: utf-8 -*-
import sqlite3


def transferContent(content):
    if content is None:
        return None
    else:
        string = ""
        for c in content:
            if c == '"':
                string += ''
            elif c == "'":
                string += "\'"
            elif c == "\\":
                string += "\\\\"
            else:
                string += c
        return string


def create(usr):
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS usr
           (
           USR_NAME           TEXT    ,
           BLACKED_LIST       TEXT    ,
           WHITE_LIST         TEXT    );''')
    print("Table created successfully")
    conn.commit()
    conn.close()


def add_black(usr,black):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")
    sql = 'INSERT INTO usr(USR_NAME,BLACKED_LIST,WHITE_LIST)\
    VALUES("' +usr + '","' + black + '","' +  "" + '")'
    c.execute(sql)
    conn.commit()
    print("Records created successfully")
    conn.close()

def add_white(usr,white):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")
    sql = 'INSERT INTO usr(USR_NAME,BLACKED_LIST,WHITE_LIST)\
    VALUES("' + usr + '","' + "" + '","' + white + '")'
    c.execute(sql)
    conn.commit()
    print("Records created successfully")
    conn.close()

def update_usr(mailusr):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")
    sql = 'INSERT INTO usr(USR_NAME,BLACKED_LIST,WHITE_LIST)\
    VALUES("' + mailusr.usr + '","' + mailusr.blacklist + '","' + mailusr.whitelist + '")'
    c.execute(sql)

    conn.commit()
    print("Records created successfully")
    conn.close()


def get_all(mailusr):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")

    cursor = c.execute("SELECT USR_NAME,BLACKED_LIST,WHITE_LIST  from usr")




    conn.close()


def search_usr(usr):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")

    sql='SELECT USR_NAME FROM usr WHERE USR_NAME="'+usr+' "'
    sql1 = 'SELECT USR_NAME,group_concat(BLACKED_LIST) FROM usr group by USR_NAME'
    cursor=c.execute(sql1)
    #cursor=c.execute(sql)

    for row in cursor:
        print(row[1])
    print("Operation done successfully")
    conn.close()


if __name__ == "__main__":
    usr = 'usr'
    create(usr)
    add_black('111','black')
    #add_white('user','white')
    search_usr('user')


'''
def create(usr):
    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "Seu123456.", "mydb", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql = transferContent('DROP TABLE IF EXISTS "' + usr + '"')

    # 如果数据表已经存在使用 execute() 方法删除表。
    cursor.execute(sql)

    # 创建数据表SQL语句
    # USR_NAME  CHAR(20) NOT NULL,

    sql = transferContent('CREATE TABLE USR ( USR_NAME CHAR(20), BLACKED_NAME  CHAR(20),WHITE_NAME  CHAR(20) )')

    cursor.execute(sql)

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    usr = transferContent('usr')
    create(usr)
'''

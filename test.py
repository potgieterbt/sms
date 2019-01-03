import sms
from sms import *
import sqlite3

conn=sqlite3.connect("recieved_messages1.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS recieved_messages1 (sender TEXT, recieved_time TEXT, content TEXT)")
conn.commit()
conn.close()

print("made database")

def search(number="",recieved_time="" ,content=""):
    global found
    found = True
    conn=sqlite3.connect("recieved_messages1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM recieved_messages1 WHERE sender=? AND recieved_time=? AND content=?", (str(number),str(recieved_time),str(content),))
    global rows
    rows=cur.fetchall()
    conn.close()
    if rows == []:
        found = False


def save_message():
    conn=sqlite3.connect("recieved_messages1.db")
    cur=conn.cursor()
    m = sms.Modem('/dev/ttyUSB0')
    msgs = m.messages()
    # print(msgs)
    # print(len(msgs))
    msgslen = len(msgs)
    i = 0
    while i < msgslen:
        global sent_date
        global sent_message
        global sent_sender
        sent_message = msgs[i].text
        sent_sender = msgs[i].number
        sent_date = msgs[i].date
        search(number=sent_sender, recieved_time= sent_date, content=sent_message)
        if found == False:
            cur.execute("INSERT INTO recieved_messages1 VALUES (?,?,?)",(sent_sender, sent_date, sent_message))
        msgs[i].delete()
        i = i + 1
    conn.commit()
    conn.close()

def send_sms(number ='', message = ''):
    m = sms.Modem('/dev/ttyUSB0')
    message = 'HI'
    number = '+27810394959'
    m.send(number, message)

# save_message()
send_sms()
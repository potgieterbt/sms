import sqlite3
import datetime
import serial
import time

def connect():
    conn=sqlite3.connect("message_content.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS message_content (id INTERGER PRIMARY KEY, content TEXT, reciepient_number INTERGER, time_stamp DATETIME )")
    conn.commit()
    conn.close()



def send_sms(content,reciepient_number):
    conn=sqlite3.connect("message_content.db")
    cur=conn.cursor()
    if reciepient_number[0] == "0":
        reciepient_number = reciepient_number[1:]
    ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
    time.sleep(1)
    ser.write('ATZ\r')
    time.sleep(1)
    ser.write('AT+CMGF=1\r')
    time.sleep(1)
    ser.write('''AT+CMGS="+27''' + reciepient_number + '''"\r''')
    time.sleep(1)
    ser.write(content + "\r")
    time.sleep(1)
    ser.write(chr(26))
    time.sleep(1)
    ser.close()
    conn.commit()
    conn.close()
    view()

def insert(content,reciepient_number):
    conn=sqlite3.connect("message_content.db")
    cur=conn.cursor()

    time_stamp = datetime.datetime.now()

    cur.execute("INSERT INTO message_content VALUES (NULL,?,?,?)",(content,reciepient_number,time_stamp))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("message_content.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM message_content")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(content="",reciepient_number="",time_stamp=""):
    conn=sqlite3.connect("message_content.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM message_content WHERE content=? OR reciepient_number=? OR time_stamp=?", (content,reciepient_number,time_stamp))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("message_content.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM message_content WHERE id=?",(id,))
    cur.execute("SELECT * FROM message_content")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows



connect()

















# def __init__(self, recipient1 = "+27810394959", message1 = "HI"):
#     recipient1 = recipient1
#     content = message1

# def setRecipient(self, number):
#     recipient = number

# def setContent(self, message):
#     content = message

# def connectPhone(self):
#     ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
#     time.sleep(1)

# def sendMessage(self):
#     ser.write('ATZ\r')
#     time.sleep(1)
#     ser.write('AT+CMGF=1\r')
#     time.sleep(1)
#     ser.write('''AT+CMGS="''' + recipient1 + '''"\r''')
#     time.sleep(1)
#     ser.write(content + "\r")
#     time.sleep(1)
#     ser.write(chr(26))
#     time.sleep(1)

# def disconnectPhone(self):
#     ser.close()
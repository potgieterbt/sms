import serial
import time
import sys
import sqlite3
import numpy
import datetime
import re



global data
data = ''

num = 0
x = ""
l = []

conn=sqlite3.connect("recieved_messages1.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS recieved_messages1 (id INTEGER PRIMARY KEY, state TEXT, number TEXT, recieved_time TEXT, content TEXT)")
conn.commit()
conn.close()

def view():
    conn=sqlite3.connect("recieved_messages1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM recieved_messages1")
    rows=cur.fetchall()
    conn.close()
    return rows
    print rows

def insert(data):
    conn=sqlite3.connect("recieved_messages1.db")
    cur=conn.cursor()

    time_stamp = datetime.datetime.now()
    print "this is a print out of data:"
    print "***************************"
    print data
    print "***************************"
    print type(data)
    print "***************************"
    print len(data)
    print "***************************"
    cur.execute("INSERT INTO recieved_messages1 VALUES (?)",(str(data),))
    conn.commit()
    conn.close()


class HuaweiModem(object):

    def __init__(self):
        self.open()

    def open(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 406800, timeout=5)
        self.SendCommand('ATZ\r')
        self.SendCommand('AT+CMGF=1\r')
        self.SendCommand('AT+CPMS="SM","SM"\r')


    def SendCommand(self,command, getline=True):
        self.ser.write(command)
        if getline:
            data=self.ReadLine()
        return data 

    def ReadLine(self):
        data = self.ser.readline()
        # insert(data)
        print data
        return data 


    def search(self, state="" ,number="",recieved_time="" ,content="" ):
        global found
        found = True
        conn=sqlite3.connect("recieved_messages1.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM recieved_messages1 WHERE state=? AND number=? AND recieved_time=? AND content=?", (str(state),str(number),str(recieved_time),str(content),))
        global rows
        rows=cur.fetchall()
        conn.close()
        print(rows)
        if rows == []:
            found = False



    def GetAllSMS(self):
        self.ser.flushInput()
        self.ser.flushOutput()





        command = 'AT+CMGL="ALL"\r\n'#gets incoming sms that has not been read
        print self.SendCommand(command,getline=True)
        data = self.ser.readall()
        print data
        # data = data.replace("+CMGL","/n")
        x=str(data)





        # date1 = re.compile(r'"([0-9]+.[0-9]+.[0-9]+,[0-9]+.[0-9]+.[0-9]+[+]?[0-9]+)"')
        # date_matches = date1.findall(data)
    
        # for match in date_matches:
        #     print(match)



        # content = re.compile(r'\s+\+CMGL:+.+\s+(.+)')
        # content_matches = content.findall(data)

        # sender = re.compile(r'"(\+\d+)"')
        # sender_matches = sender.findall(data)

        state = re.compile(r'("\w+\s\w+"),+"(.+)",+("[0-9]+.[0-9]+.[0-9]+,[0-9]+.[0-9]+.[0-9]+[+]?[0-9]+")?\s+(.+\S+\s+?.+\S+)+?')
        state_matches = state.findall(data)
        # print(state_matches)

        for match in state_matches:
            state_db = match[0]

            sender_db = match[1]
            
            date_db = match[2]
            
            content_db = match[3]
            print(state_db, sender_db, date_db, content_db)
            
            self.search(state = str(state_db), number = sender_db, recieved_time = date_db, content = content_db)

            if found == False and str(state_db) != '"STO SENT"':
                print match
                conn=sqlite3.connect("recieved_messages1.db")
                cur=conn.cursor()
                cur.execute("INSERT INTO recieved_messages1 VALUES (NULL,?,?,?,?)",(state_db, sender_db, date_db, content_db))
                
                
                conn.commit()
                conn.close()

        # for match in sender_matches:
        #     print(match)

        # for match in content_matches:
        #     print(match)

        data = str(data)
        # insert(data)



print data
h = HuaweiModem()
h.GetAllSMS()
# insert(data)
h.ReadLine()

# insert(data)
view()
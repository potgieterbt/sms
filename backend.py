import sqlite3

def connect():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, people TEXT, Surname TEXT, contacts_number integer, Staff_ID integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS message_content (id INTERGER PRIMARY KEY, content TEXT, sender_number INTERGER, time_stamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
#    self.recipient1 = recipient1
#    self.content = message1
    conn.commit()
    conn.close()

def insert(people,Surname,contacts_number,Staff_ID):
    conn=sqlite3.connect("message_content.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO contacts VALUES (NULL,?,?,?,?)",(people,Surname,contacts_number,Staff_ID))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(people="",Surname="",contacts_number="",Staff_ID=""):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE people=? OR Surname=? OR contacts_number=? OR Staff_ID=?", (people,Surname,contacts_number,Staff_ID))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?",(id,))
    cur.execute("SELECT * FROM contacts")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id,people,Surname,contacts_number,Staff_ID):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("UPDATE contacts SET people=?, Surname=?, contacts_number=?, Staff_ID=? WHERE id=?",(people,Surname,contacts_number,Staff_ID,id))
    conn.commit()
    conn.close()


connect()
















#def __init__(self, recipient1 = "", message1 = "HI"):
#    self.recipient1 = recipient1
#    self.content = message1
#
#def setRecipient(self, number):
#    self.recipient = number
#
#def setContent(self, message):
#    self.content = message
#
#def connectPhone(self):
#    self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
#    time.sleep(1)
#
#def sendMessage(self):
#    self.ser.write('ATZ\r')
#    time.sleep(1)
#    self.ser.write('AT+CMGF=1\r')
#    time.sleep(1)
#    self.ser.write('''AT+CMGS="''' + self.recipient1 + '''"\r''')
#    time.sleep(1)
#    self.ser.write(self.content + "\r")
#    time.sleep(1)
#    self.ser.write(chr(26))
#    time.sleep(1)
#
#def disconnectPhone(self):
#    self.ser.close()
#    
        
        
        
        
        
        
        
        
        
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(Surname="John Smooth"))

import serial
import time

message1 = "HI"
recipient1 = ""

class TextMessage:
    def __init__(self, recipient1 = "", message1 = "HI"):
        self.recipient1 = recipient1
        self.content = message1

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5, xonxoff = False,
         rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
        time.sleep(1)

    def sendMessage(self):
        self.ser.write('ATZ\r')
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r')
        time.sleep(1)
        self.ser.write('''AT+CMGS="''' + self.recipient1 + '''"\r''')
        time.sleep(1)
        self.ser.write(self.content + "\r")
        time.sleep(1)
        self.ser.write(chr(26))
        time.sleep(1)
        

    def disconnectPhone(self):
        self.ser.close()

sms = TextMessage(recipient1,message1)
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()
print "message sent successfully"

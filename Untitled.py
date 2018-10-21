import time
import serial
import sys, errno
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)


recipient = "+27810394959"
message = "Test"

phone = serial.Serial("/dev/ttyUSB1",  115200, timeout=5)


try:
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    time.sleep(0.5)
    phone.write(b'AT+CMGF=1\r')
    time.sleep(0.5)
    phone.write(b'ATD"'+recipient.encode() +b';"\r')
    time.sleep(0.5)
    phone.write(message.encode() + b"\r")
    time.sleep(0.5)
    phone.write(bytes([26]))
    time.sleep(0.5)
finally:
    phone.close()
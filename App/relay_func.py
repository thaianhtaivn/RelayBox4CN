import serial
import time

class Relay_Serial():
    def __init__(self, port, baudrate=9600):  
        self.port = port      
        self.baudrate = baudrate      
        self.ser = serial.Serial()
        self.ser.timeout = 0.5

    def open(self):
        self.ser = serial.Serial(self.port, self.baudrate)
    
    def send(self, command):
        self.ser.write(command.encode('utf-8'))
        time.sleep(0.02)
        self.ser.close()
    
    def close(self):
        self.ser.close()
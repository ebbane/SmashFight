import socket 
from main import * 


IP_LOCALHOST = "127.0.0.1"
PORT = 5005



class Connectitivity:

    def __init__(self):
        self.event_handler = Event()

    
    def command(self):

        message = socket.socket(
            socket.AF_INET, # Internet
            socket.SOCK_DGRAM) # UDP
        message.bind((IP_LOCALHOST, PORT)) 

        while True:
            data, addr = message.recvfrom(1024) # buffer size is 1024 bytes
            print("received message: %s" % data)
        
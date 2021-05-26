import socket 
from main import * 


IP_LOCALHOST = "127.0.0.1"
PORT = 5005


message = socket.socket(
    socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
message.bind((UDP_IP, UDP_PORT))
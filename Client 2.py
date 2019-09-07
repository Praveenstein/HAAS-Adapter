#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import socket module 
import socket  
# Create a socket object 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)          
  
# Define the port on which you want to connect 
port = 5051                
  
# connect to the server on local computer 
s.connect(('192.168.100.3', port)) 
s.send(("?Q500").encode("utf-8")) # just add an encoding

fullData = ""

while True:
    d = (s.recv(1024)).decode("utf-8")
    fullData += d

    if not d:
        print(fullData)
        s.close()
        break


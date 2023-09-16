# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  bufferSize = 32
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection

    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = None
      buffering = True
      while buffering:
        data = connectionSocket.recv(bufferSize).decode()#Fill in start -a client is sending you a message   #Fill in end
        if message == None:
          message = ""
        message += data
        if len(data) <= bufferSize and data[len(data) - 1] == "\n" and data[len(data) - 2] == "\r" and data[len(data) - 3] == "\n" and data[len(data) - 4] == "\r":  # if it's bufferSize exactly then need to check last char for /r/n
          buffering = False
          print("buffering false")

      filename = message.split()[1]
      print(filename)
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "rb") #fill in start #fill in end)
      #fill in end
      
      outputdata = b"HTTP/1.1 200 OK\r\nConnection: keep-alive\r\nServer: python3\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
      #Fill in start -This variable can store your headers you want to send for any valid or invalid request. 
      #Content-Type above is an example on how to send a header as bytes. There are more!
      #Fill in end

      #Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok? 
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in start

      #Fill in end
               

      #Send the content of the requested file to the client
        #Fill in start - send your html file contents #Fill in end
      bytes = f.read()
      outputdata += bytes
      encoded = outputdata
      connectionSocket.send(encoded)
      print(str(outputdata))
      f.close()
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      outputdata = b"HTTP/1.1 404 Not Found\r\nConnection: close\r\nServer: python3\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
      connectionSocket.send(outputdata)
      print(str(outputdata))
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()  # closing the connection socket
      #Fill in end

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  print("SERVER CLOSED")
  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)

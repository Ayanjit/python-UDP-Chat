# python-UDP-Chat
It is a small chat room application made with Python3.  
It uses UDP for data transfer between Server and Client Process.  
  
  
  
Step 1:  
In the CMD write -> python chat.py  
It creates a server and prints the IP address of the server.  
Server port is fixed at 5000.  
The IP addess is the one which is provided by the Wifi Router.  
It is not the external IP.  


Step 2:  
In another machine connected with the same Wifi or same machine where server is running,  
open another CMD and run -> python chat.py XXX.XXX.XXX.XXX  
XXX.XXX.XXX.XXX is the ServerIP.  
When you started the server, it prints it's IP.  
You can open more than one CMD and run the same command to spawn multiple client.  
  
  
  
Step 3:  
After spawning each client, write your name in the CMD.  
This is like your nickname.  
When the name is created, then server came to know about the client.  
  
  
  
Step 4:  
After naming all the client, when any client writes a message it goes to all the cliets which are connected to the same server.  
The message also gets printed in the Server.  

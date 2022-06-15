# Chat Room Application

## As the name says, this is a python application of for a chat room:

* Run in a local server 
* To use this app you will just have to manually run de file "Server.py", and then each one of the pyhton files with the "Client_#.py" name path.
* This app is configure to use till 5 client at the same time, but you can reconfigure it to increase the number of possible clients at the same time.

### About the App:
- Transmission Control Protocol (TCP):
Sockets can be configured to act as a server and listen for incoming messages, or connect to other applications as a client. 
After both ends of a TCP/IP socket are connected, communication is bi-directional.
See more: http://pymotw.com/2/socket/tcp.html#:~:text=Sockets%20can%20be%20configured%20to,%2C%20communication%20is%20bi%2Ddirectional.

- User Datagram Protocol (UDP):
Makes use of Internet Protocol of the TCP/IP suit. 
In communications using UDP, a client program sends a message packet to a destination server wherein the destination server also runs on UDP.
See more: https://pythontic.com/modules/socket/udp-client-server-example

- Socket:
Socket programming is a way of connecting two nodes on a network to communicate with each other. 
One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. 
The server forms the listener socket while the client reaches out to the server. 
They are the real backbones behind web browsing. In simpler terms, there is a server and a client. 
See more: https://www.geeksforgeeks.org/socket-programming-python/#:~:text=Socket%20programming%20is%20a%20way,reaches%20out%20to%20the%20server.
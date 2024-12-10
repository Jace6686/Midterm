import socket

class Server:

    def __init__(self, host, port):
        #create a new socket. AF_Inet is the address family for IPv4, 
        # SOCK_STREAM is the socket type for TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        #Enable the server to accept connections. The argument is the number of unaccepted connections that the system will allow before refusing new connections
        self.socket.listen(1)
        print('server waiting for connection...')
        self.conn, self.addr = self.socket.accept()
        print(f'Connection from {self.addr} has been established!')
        self.talk_to_client(self.conn)
        #talk to the client
        self.socket.close()
        #close the socket

    def talk_to_client(self, client_socket):
        while True:
            message = input('server: ')
            client_socket.sendall(message.encode())
            #send data to the client
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from client: {data.decode()}")
        
            shutdown = data.decode()
            if shutdown == 'yes':
                print('client is shutting down...')
                break
            #if the client sends yes, break the loop
        client_socket.close()
        #close the socket

Server('127.0.0.1', 12345)
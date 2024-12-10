import socket


class client:

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        #Connect to a remote socket at address. The return value is None.
        print ('client connected to server...')
        #connect to the server

    def talk_to_server(self):
        while True:
            message = input('client: ')
            self.socket.send(message.encode())
            #send data to the server
            if message == 'exit':
                break
            #if the message is exit, break the loop
            response = self.socket.recv(1024).decode()
            #receive data from the server
            print(f'server: {response}')
            #print the response from the server

        shutdown = input('Do you want to shutdown the server? (yes/no): ')
        if shutdown == 'yes':
            self.socket.send(shutdown.encode())
            #send data to the server
            print('server is shutting down...')
            #print the server is shutting down
        self.socket.close()
        #close the socket

client('127.0.0.1', 12345).talk_to_server()
import socket as sock


# socket API

# socket()
# .bind()
# .listen()
# .accept()
# .connect()
# .connect_ex()
# .send()
# .recv()
# .close()

# This class handle the all socket related server 

class TcpServer:
    def __init__(self,host="127.0.0.1",port=4999) -> None:
        self.socket = sock.socket(sock.AF_INET,sock.SOCK_STREAM)
        self.socket.bind((host,port))
    def listen(self):
        self.socket.listen(4)
        while True:
            conn,addr=self.socket.accept()
            self.onRecieved(conn,addr)
            conn.close()
    def addonRecieved(self,onRecieved):
        self.onRecieved=onRecieved
    def close(self):
        self.socket.close()
import server.tcp_server as tcp_server
import protocol.http_protocal as http_protocol





    


class WebServer:
    def __init__(self, host, port) -> None:
        self.tcp_server = tcp_server.TcpServer(host, port)
        self.tcp_server.addonRecieved(self.web_server_main_functionality)
        self.router={
            "GET":{},
            "PUT":{}
        }
        print(f"Initiaizing for host:{host} and port: {port}")

    def close(self):
        self.tcp_server.close()

    def run(self):
        print("Listening...........")
        self.tcp_server.listen()
    

    def web_server_main_functionality(self,connection, address):
        print(f"Get the connection from {address} ")
        data = connection.recv(1024).decode()
        request=http_protocol.HttpRequest.fromString(data)
        try:
            self.router[request.method][request.path](request,connection)
        except:
            print("Some error has occured")
    
    def onGet(self,route_path,handler):
        self.router["GET"][route_path]=handler

    def onPut(self,route_path,handler):
        self.router["PUT"][route_path]=handler
    



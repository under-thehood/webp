import protocol.http_protocal as http_protocal
import socket
import ssl





def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.google.com", 80))
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % "www.google.com"

    s.send(request.encode())
    response_string = s.recv(4096).decode()
    
    s.close()
    response = http_protocal.HttpResponse.fromString(response_string)
    response.display()


main()

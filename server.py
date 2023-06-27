import server.web_server as webserver
import protocol.http_protocal as http


def roothandler(request: http.HttpRequest, connection):
    print("Handling root route")
    resonse = http.HttpResponse(
        "HTTP/1.1", 200, "OK", {"Server": "Custom server"}, None
    )
    connection.send(resonse.toString().encode())

def faviconHandler(request: http.HttpRequest, connection):
    print("Handling favicon route")
    resonse = http.HttpResponse(
        "HTTP/1.1", 200, "OK", {"Server": "Custom server"}, None
    )
    connection.send(resonse.toString().encode())

def main():
    server = webserver.WebServer("127.0.0.1", 8001)
    server.onGet("/", roothandler)
    server.onGet("/favicon.ico", roothandler)
    server.run()


main()

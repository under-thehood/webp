SEPERATOR = "\r\n"


class HttpRequest:
    def __init__(self, method, path, protocol_version, header, body) -> None:
        self.method = method
        self.path = path
        self.http_protocol_version = protocol_version
        self.header = header
        self.body = body

    @staticmethod
    def fromString(request: str):
        seperated_string = request.split(SEPERATOR)
        method_line_splitted = seperated_string[0].split(" ")
        body_index = seperated_string.__len__()
        # get the method and the path
        method = method_line_splitted[0]
        path = method_line_splitted[1]
        protocol_version = method_line_splitted[2]

        # get the header
        header = {}
        for index, header_line in enumerate(seperated_string[1:]):
            if header_line == "":
                body_index = index + 1
                break
            header_line_splitted = header_line.split(" ")
            header[header_line_splitted[0][:-1]] = "".join(header_line_splitted[1:])
        # get the body to be implemented
        return HttpRequest(method, path, protocol_version, header, None)

    def display(self):
        print(f"HTTP Method:{self.method}")
        print(f"Router Path: {self.path}")
        print(f"Header: {self.header}")

    def headerToString(self) -> str:
        header_str = ""
        for key, value in self.header.items():
            header_str += f"{key}: {value}{SEPERATOR}"
        return header_str

    def toString(self):
        return f"{self.method} {self.path} {self.http_protocol_version}{SEPERATOR}{self.headerToString()}"


class HttpResponse:
    def __init__(
        self, protocol_version, status_code, status_message, header, body
    ) -> None:
        self.http_protocol_version = protocol_version
        self.status_code = status_code
        self.status_message = status_message
        self.header = header
        self.body = body

    @staticmethod
    def fromString(response: str):
        seperated_string = response.split(SEPERATOR)
        status_line_splitted = seperated_string[0].split(" ")
        body_index = seperated_string.__len__()
        # get the method and the path
        protocol_version = status_line_splitted[0]
        status_code = status_line_splitted[1]
        status_message = status_line_splitted[2]

        # get the header
        header = {}
        for index, header_line in enumerate(seperated_string[1:]):
            if header_line == "":
                body_index = index + 1
                break
            header_line_splitted = header_line.split(" ")
            header[header_line_splitted[0][:-1]] = "".join(header_line_splitted[1:])

        # get the body to be implemented
        return HttpResponse(protocol_version, status_code, status_message, header, None)

    def display(self):
        print(f"HTTP Status:{self.status_message}")
        print(f"Status code: {self.status_code}")
        print(f"Header: {self.header}")

    def headerToString(self) -> str:
        header_str = ""
        for key, value in self.header.items():
            header_str += f"{key}: {value}{SEPERATOR}"
        return header_str

    def toString(self):
        return f"{self.http_protocol_version} {self.status_code} {self.status_message}{SEPERATOR}{self.headerToString()}"

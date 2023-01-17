import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\r\nHost: "+ host.encode('utf-8') + b"\r\n\r\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Send request
    s.send(request)

    # Only shutdown the write buffer/pipe for the socket
    s.shutdown(socket.SHUT_WR)

    data = b""

    while len(newdata:= s.recv(BYTES_TO_READ)):
        data += newdata

    return data

if __name__ == "__main__":
    data = get("www.google.com", 80)

    print(data)

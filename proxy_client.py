import socket

BYTES_TO_READ = 4096

def get(host, port):

    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request)
        s.shutdown(socket.SHUT_WR)
        print("Waiting for response...")
        
        data = b""
        while len(chunk:= s.recv(BYTES_TO_READ)):
            data += chunk
        
        print(data)

if __name__ == "__main__":
    get("127.0.0.1", 8080) # IP of proxy_server running on same machine at port 8080
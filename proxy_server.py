"""
Proxy server for www.google.com
"""
import socket
from threading import Thread
import os

BYTES_TO_READ = 4096
PROXY_SERVER_HOST = "127.0.0.1"
PROXY_SERVER_PORT = 8080

def send_request(host, port, request_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Sending data to google
        client_socket.connect((host, port))
        client_socket.send(request_data)
        client_socket.shutdown(socket.SHUT_WR)

        # Getting response back from google
        data = client_socket.recv(BYTES_TO_READ)
        result = b""
        while (len(data)) > 0:
            data = client_socket.recv(BYTES_TO_READ)
            result += data

    return result


def handle_connection(conn, addr):
    
    with conn:
        print(f"Connected by: {addr}")
        request = b""
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            request += data

        response = send_request("www.google.com", 80, request)
        print(f"Got response from google: {response}")
        conn.sendall(response)
        conn.shutdown(socket.SHUT_RDWR)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        
        conn, addr = server_socket.accept()

        handle_connection(conn, addr)

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        
        while True:
            conn, addr = server_socket.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

def start_forked_server():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server_socket.bind((PROXY_SERVER_HOST, PROXY_SERVER_PORT))
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.listen(2)
        
        while True:
            conn, addr = server_socket.accept()
            
            pid = os.fork()

            if pid == 0:
                handle_connection(conn, addr)
                break
            


if __name__ == "__main__":
    start_forked_server()
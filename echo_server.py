import socket
import os

BYTES_TO_READ = 4096

HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by: {addr}")

        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)
            conn.shutdown(socket.SHUT_RDWR)

def start_server():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.listen()

        conn, addr = s.accept()

        handle_connection(conn, addr)


def start_forked_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.listen()

        conn, addr = s.accept()

        pid = os.fork()

        if pid == 0:
            handle_connection(conn, addr)
            exit()
        



if __name__ == "__main__":
    start_forked_server()
            
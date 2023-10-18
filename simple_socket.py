import socket

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Server listening on ", host, "port ", port)

        conn, addr = server_socket.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            conn.sendall(b'Hello, '+ data)

    
if __name__ == "__main__":
    start_server('127.0.0.1', 65432)
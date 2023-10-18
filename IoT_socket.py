import socket

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("server is runnning on ", host, "port ", port)

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                if not data:
                    break
                print('Recieved:', data.decode())
                # process the recieved information data (e.g, control IoT devices, store data, etc)

if __name__ == "__main__":
    start_server('127.0.0.1', 65432)
import socket

def send_data_to_server(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall((message.encode()))
        data = client_socket.recv(1024)


    return data.decode()

if __name__ == "__main__":
    response = send_data_to_server('127.0.0.1', 65432, 'world')
    print('Recieved from server:', response)
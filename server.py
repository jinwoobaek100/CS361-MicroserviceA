import socket
import threading
import zmq

clients = {}
lock = threading.Lock()

def handle_client(client_socket, client_address):
    nickname = client_socket.recv(1024).decode('utf-8')
    with lock:
        clients[nickname] = client_socket
    print(f"{nickname} has joined the chat from {client_address}")

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            recipient, message = data.split(':', 1)
            recipient = recipient.strip()
            message = message.strip()

            if recipient in clients:
                with lock:
                    log_files = [
                        open(f"{nickname}-{recipient}.txt", "a"),
                        open(f"{recipient}-{nickname}.txt", "a")
                    ]
                    for log_file in log_files:
                        log_file.write(f"{nickname}: {message}\n")
                        log_file.flush()
                        log_file.close()
                    clients[recipient].send(f"New message from '{nickname}'\nEnter recipient's nickname: ".encode('utf-8'))
            else:
                client_socket.send(f"Error: User '{recipient}' not found.\n".encode('utf-8'))
        except:
            break

    with lock:
        del clients[nickname]
    client_socket.close()

def zmq_listener():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        message = socket.recv_string()
        print(f"Received request: {message}")
        response = f"Server received: {message}"
        socket.send_string(response)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(10)
    print("Server is listening...")

    zmq_thread = threading.Thread(target=zmq_listener)
    zmq_thread.start()

    while True:
        client_socket, client_address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()

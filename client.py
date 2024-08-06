import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\n{message}", end = '') 
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))

    nickname = input("Enter your nickname: ")
    client_socket.send(nickname.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        recipient = input("Enter recipient's nickname: ")
        message = input("Enter your message: ")
        if message.lower() == 'exit':
            break
        client_socket.send(f"{recipient}: {message}".encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    main()
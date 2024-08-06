Microservice A - Chatting System
Communication Contract
Instructions for Programmatically Requesting Data
To request data from the microservice, you need to connect to the ZeroMQ socket and send a string message. Here is an example using Python:
python
import zmq

def request_data():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    
    request_message = "Hello from test program"
    print(f"Sending request: {request_message}")
    socket.send_string(request_message)
    
    response_message = socket.recv_string()
    print(f"Received reply: {response_message}")

if __name__ == "__main__":
    request_data()

Instructions for Programmatically Receiving Data
When you send a request to the microservice, it will respond with a string message. The example above shows how to receive this response. After sending the request, you use socket.recv_string() to get the reply from the microservice.
UML Sequence Diagram
Below is a UML sequence diagram illustrating how the request and response process works:
![image](https://github.com/user-attachments/assets/ae490f2b-d18e-4d76-8197-8e96a0042700)

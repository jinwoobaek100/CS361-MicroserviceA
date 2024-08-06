# Microservice A - Chatting System

## Communication Contract

### Instructions for Programmatically Requesting Data

To request data from the microservice, you need to connect to the ZeroMQ socket and send a string message. Here is an example using Python:

```python
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

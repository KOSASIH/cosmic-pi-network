import socket
import threading
from queue import Queue
from time import sleep

class Node:
    def __init__(self, node_id, host, port):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.clients = []
        self.data_queue = Queue()
        self.running = True
        self.discovery_thread = threading.Thread(target=self.discover_nodes)
        self.discovery_thread.start()

    def discover_nodes(self):
        while self.running:
            try:
                broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                message = f'Node Discovery: {self.node_id}'
                broadcast_socket.sendto(message.encode(), ('<broadcast>', 9000))
                sleep(5)
            except Exception as e:
                print(f'Error during node discovery: {e}')

    def connect_client(self, client_socket, client_address):
        print(f'New connection from {client_address}')
        self.clients.append((client_socket, client_address))
        client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
        client_thread.start()

    def handle_client(self, client_socket, client_address):
        while self.running:
            try:
                data = client_socket.recv(1024)
                if data:
                    self.data_queue.put((client_address, data))
                else:
                    break
            except Exception as e:
                print(f'Error handling client: {e}')
                break

        self.clients.remove((client_socket, client_address))
        client_socket.close()

    def send_data(self, data, destination_address):
        for client in self.clients:
            if client[1] == destination_address:
                client[0].sendall(data)

    def receive_data(self):
        while self.running:
            try:
                address, data = self.data_queue.get()
                print(f'Received data from {address}: {data.decode()}')
            except Exception as e:
                print(f'Error receiving data: {e}')

    def stop(self):
        self.running = False
        self.socket.close()
        self.discovery_thread.join()

if __name__ == '__main__':
    node = Node(1, '127.0.0.1', 9001)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        node.stop()

import threading
from Server.server import ServerObj
# main class contains some static methodes 
# which starts server
class Main:
    @staticmethod
    def handle_connection(client_connection):
          while True:
            try:
             client_connection.send(b"+PONG\r\n")
            except ConnectionError:
              break  # Stop serving if the client connection is closed

    @staticmethod
    def run_server(bind_ip : str = '127.0.0.1', port : int = 6689, reuse_port: bool = False):
        server_socket = ServerObj(bind=bind_ip, port=port, reuse_port=False).create_and_get_socket()
        while True:
          client_connection, _ = server_socket.accept()  # wait for client
          threading.Thread(target=Main.handle_connection, args=(client_connection,)).start()

if __name__ == "__main__":
    Main.run_server()  
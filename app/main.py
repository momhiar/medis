import threading
from Server.server import ServerObj
from Commands.managers import BasicCommandManager
from Store.db import SingletonInMemStore
import sys
# main class contains some static methodes 
# which starts server
class Main:
    @staticmethod
    def handle_connection(client_connection):
       while client_connection:
           try:
              conn = client_connection.recv(1024)
              res = BasicCommandManager(conn).handle_connection()
              client_connection.send(res)
           except ConnectionError:
               break  # Stop serving if the client connection is closed
    @staticmethod
    def initialize_db():
      print('initializing database')
      store = SingletonInMemStore()
      print('loading data from persist files')
      store.sync_data_from_persistor()
    @staticmethod
    def run_server(bind_ip : str = '127.0.0.1', port : int = 6689, reuse_port: bool = True):
        print('Welcome to Medis a beautiful redis wrote in python')
        server_socket = ServerObj(bind=bind_ip, port=port, reuse_port=False).create_and_get_socket()
        server_socket.listen()
        Main.initialize_db()
        print(f'server is listening on {bind_ip} and port {port} and ready to accept connections')
        while True:
          client_connection, _ = server_socket.accept()  # wait for client
        #   Main.handle_connection(client_connection)
          threading.Thread(target=Main.handle_connection, args=(client_connection,)).start()

if __name__ == "__main__":
    if len(sys.argv) == 3:
      args = [sys.argv[1], int(sys.argv[2])]
    elif len(sys.argv):
      args = []
    else:
      raise ReferenceError('arguments are not enough')
    Main.run_server(*args)  
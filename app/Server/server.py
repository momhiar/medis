import socket

class ServerObj:
    def __init__(self, bind: str, port: int, reuse_port: bool= False):
      self.__bind = bind
      self.__port = port
      self.__reuse_port = reuse_port
    
    def create_and_get_socket(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.__bind,self.__port))
        return  server_socket

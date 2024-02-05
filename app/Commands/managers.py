from .commands_lib import commands_list
from .decoders import RedisCommandDecoder

class BasicCommandManager:
    def __init__(self, connection_request) -> None:
        command, *self.args = RedisCommandDecoder(connection_request).decode()
        self.command = command.decode("utf-8").upper()
        self.set_command_class(command=self.command)
        
    def set_command_class(self, command: str):
        try:
            self.command_class = commands_list[command]
        except:
            self.command_class = commands_list['WRONG']
        
    def handle_connection(self):
        res =self.command_class(self.args).execute()
        return res
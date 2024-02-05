from . import basic_commands

commands_list = {
    'GET': basic_commands.GetCommand,
    'DEL': basic_commands.DeleteCommand,
    'PING': basic_commands.PingCommand,
    'TTL': basic_commands.TTLCommand,    
}
from . import basic_commands

commands_list = {
    'GET': basic_commands.GetCommand,
    'SET': basic_commands.SetCommand,
    'DEL': basic_commands.DeleteCommand,
    'PING': basic_commands.PingCommand,
    'TTL': basic_commands.TTLCommand,
    'COMMAND': basic_commands.StartCommand,
    'WRONG': basic_commands.ErrorCommand,    
}
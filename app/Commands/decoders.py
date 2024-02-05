class RedisCommandDecoder:
    def __init__(self, connection):
        self.connection = connection
    def decode(self):
        request = self.connection
        commands = request.split(b"\r\n")
        filtered_commands = [
            cmd for cmd in commands if not cmd.startswith(b"*") and not cmd.startswith(b"$")
        ]   
        return filtered_commands
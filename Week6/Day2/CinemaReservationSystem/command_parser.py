class CommandParser:

    def __init__(self):
        self.commands = {}

    def add_command(self, command, function):
        self.commands[command] = function

    def execute_command(self, command):
        self.commands[command]()

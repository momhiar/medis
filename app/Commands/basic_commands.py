from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass



class BaseCommand(Command):
    pass



class PingCommand(Command):
    pass

class GetCommand(Command):
    pass


class SetCommand(Command):
    pass

class DeleteCommand(Command):
    pass

class TTLCommand(Command):
    pass
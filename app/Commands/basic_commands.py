from __future__ import annotations
from abc import ABC, abstractmethod
from Store.db import SingletonInMemStore
import time
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class BaseCommandMixin():
    _db = SingletonInMemStore()
   
    def __init__(self, args):
        self._args = args

class ErrorCommand(Command, BaseCommandMixin):
    def execute(self, *args, **kwargs):
        return b"$-1\r\n"


class StartCommand(Command, BaseCommandMixin):
    def execute(self, *args, **kwargs):
        return b'+Welcome to Medis a beautiful redis wrote in python\r\n'    
class PingCommand(Command, BaseCommandMixin):
    def execute(self, *args, **kwargs):
        return b'+PONG\r\n'

class GetCommand(Command, BaseCommandMixin):
    def execute(self):
        return self._db.get_value_from_objects(key= self._args[0].decode('utf-8'))


class SetCommand(Command, BaseCommandMixin):
    def execute(self):
        if len(self._args) < 3: return b'+not enough args\r\n'
        return self._db.set_value_to_objects(key= self._args[0].decode('utf-8'), value= self._args[1],
                                             expiry_date=self.get_int_date(self._args[2]))
    def get_int_date(self, ttl):
        if ttl:
            return int(time.time() * 1000) + int(ttl.decode('utf-8'))
        return None

class DeleteCommand(Command, BaseCommandMixin):
    def execute(self):
        return self._db.delete_record_from_objects(key= self._args[0].decode('utf-8'))
class TTLCommand(Command, BaseCommandMixin):
    def execute(self):
        return self._db.get_ttl_from_objects(key= self._args[0].decode('utf-8'))
    
    
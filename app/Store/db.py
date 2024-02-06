from threading import Lock
import time
import pickle
from .persistors import Persistor, PicklePersistor
import warnings



# using singleton patter ( Thread-safe)
class SingletonInMemStoreMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """

        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonInMemStore(metaclass=SingletonInMemStoreMeta):
    __objects = {}
    
    #implementation of observer patterns (mono)
    # TODO: we should add dynamic multiple choices for users at runtime
    #currently we skip
    __persistor : Persistor = PicklePersistor()
    #TODO: we should add logic for dynamic persistor type
    # for now we skip because lack of time
    __persist_file = 'persistors/db_persist.pickle'
    def set_value_to_objects(self, key, value, expiry_date = None):
        self.__objects[key] = (value, expiry_date)
        self.sync_persistors_from_latest()
        return b"+OK\r\n"

    def get_value_from_objects(self, key):
        value = self.check_value(pair=self.__objects.get(key))
        if value is None: 
            self.delete_record_from_objects(key) 
            return b"$-1\r\n"
        return b"$%d\r\n%b\r\n" % (len(value), value)
    
    def check_value(self, pair):
        if not pair:
            return pair
        value = pair[0]
        expiry_date = pair[1]
        if (expiry_date is not None) and (int(time.time() * 1000)  <= expiry_date):
            return value
        if (expiry_date is None):
            return value
        return None
    def delete_record_from_objects(self, key):
        if self.__objects.get(key):
            del self.__objects[key]
            self.sync_persistors_from_latest()
            return  b"+OK\r\n"
        else:
            return b"$-1\r\n"
        
    def get_ttl_from_objects(self, key):
        record = self.__objects.get(key)
        if not record:
            return b"+-2\r\n"
        if record[1] is None:
            return b"$-1\r\n"
        ttl = record[1] - int(time.time() * 1000)
        if ttl < 0:
            self.delete_record_from_objects(key=key)
            return b"$-1\r\n"
        return b"$%d\r\n%b\r\n" % (len(str(ttl)), str(ttl).encode())
       
    #implementation of observer patterns but only one observer
    def sync_persistors_from_latest(self):
            self.__persistor.sync_latest_to_file(self.__objects, self.__persist_file)
    
    def sync_data_from_persistor(self):
        try:
            self.__objects = self.__persistor.read_latest_from_file(self.__persist_file)
        except FileNotFoundError:
            warnings.warn('no persis file is there')
        except:
            raise EOFError('Error: somthing happened during read persist files')
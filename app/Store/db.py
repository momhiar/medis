from threading import Lock
import time
import pickle
class SingletonInMemStoreMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's no
        # Singleton instance yet, multiple threads can simultaneously pass the
        # previous conditional and reach this point almost at the same time. The
        # first of them will acquire lock and will proceed further, while the
        # rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonInMemStore(metaclass=SingletonInMemStoreMeta):
    __objects = {}
    
    def set_value_to_objects(self, key, value, expiry_date: int = None):
        self.__objects[key] = (value, expiry_date)
        return 'OK'

    def get_value_from_objects(self, key):
        value = self.check_value(pair=self.__objects.get(key))
        if value is None: self.delete_record_from_objects(key) 
        return value
    
    def check_value(self, pair):
        if not pair:
            return pair
        value, expiry_date = pair
        if (expiry_date is None) or (int(time.time()) * 1000 <= expiry_date):
            return value
        return None
    def delete_record_from_objects(self, key):
        if self.__objects.get(key):
            del self.__objects[key]
            return 'OK'
        
    def get_ttl_from_objects(self, key):
        record = self.__objects.get(key)
        if not record:
            return -2
        if record[1] is None:
            return -1 
        return record[1]
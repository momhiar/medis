from abc import ABC, abstractmethod
import pickle

class Persistor(ABC):
    @abstractmethod
    def read_latest_from_file(self, file):
        pass
    @abstractmethod
    def sync_latest_to_file(self, data, file):
        pass
        

class PicklePersistor(Persistor):
    
    def read_latest_from_file(self, file):
        with open(file,"rb") as file_handle:
            res = pickle.load(file_handle)
            return res
    def sync_latest_to_file(self, data, file):
        with open(file,"wb") as file_handle:
            pickle.dump(data, file_handle, pickle.HIGHEST_PROTOCOL)
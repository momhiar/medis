#TODO: add more persistors tests
import os
from Store.persistors import PicklePersistor

def test_pickle_persistor_write_data():
    file = 'db_persist_test.pickle'
    data = {'record_1': ('test', 1707130406200), 'record_2': ('test2', None)}
    res = PicklePersistor().sync_latest_to_file(file=file, data=data)
    assert os.path.exists(file)

def test_pick_persistor_read_data():
    file = 'db_persist_test.pickle'
    res = PicklePersistor().read_latest_from_file(file=file)
    assert res is not None
    assert res.get('record_2') == ('test2', None)
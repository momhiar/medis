import pytest
from Store.db import SingletonInMemStore
import time
@pytest.fixture
def store():
    return SingletonInMemStore()

# currently these are our first test because lack of time
#TODO: add more tests
def test_value_is_set(store):
    res = store.set_value_to_objects(key='record_1', value='test', expiry_date=(int(time.time())*1000 + 200)) 
    assert res == 'OK'

def test_get_value(store):
    res = store.get_value_from_objects(key='record_1')
    assert res == 'test'
    
def test_get_ttl(store):
    res = store.get_ttl_from_objects(key='record_1')
    # test a brand new object is fine
    assert res > -1
    store.set_value_to_objects(key='record_2', value='test2', expiry_date=None)
    # test not timed data is -1
    res = store.get_ttl_from_objects(key='record_2')
    assert res == -1
    #test not exists object is -2
    res = store.get_ttl_from_objects(key='neve_submitted_record_here')
    assert res == -2
    
    
# def test_persistors_work(store):
#     store.sync_data_from_persistor()
#     print(store.get_value_from_objects('record_2'))
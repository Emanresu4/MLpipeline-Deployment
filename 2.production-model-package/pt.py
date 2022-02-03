import pytest

@pytest.fixture
def value():
   data = 100
   return data

def Test_func1(data):
   assert data % 3 == 0

def Test_sqrt(data):
   assert sqrt(data) == 10

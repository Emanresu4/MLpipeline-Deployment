from my_module import square

import pytest

@pytest.mark.parametrize(
	'inputs',[2,3,4])

def test_type(inputs):
	#when
	sub = square(inputs)

	#then
	assert isinstance(sub,int)
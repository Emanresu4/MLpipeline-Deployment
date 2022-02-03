from my_module import square

def test_type(input_value):
	#when
	sub = square(input_value)

	#then
	assert isinstance(sub,int)
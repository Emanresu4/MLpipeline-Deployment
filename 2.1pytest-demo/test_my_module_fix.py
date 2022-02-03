from my_module import square

def test_square_correct(input_value):
	#when
	subject = square(input_value)

	#then
	assert subject == 16
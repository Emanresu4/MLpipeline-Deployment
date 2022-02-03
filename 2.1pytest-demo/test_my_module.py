from my_module import square

def test_square_correct():
	#when
	subject = square(2)

	#then
	assert subject == 4
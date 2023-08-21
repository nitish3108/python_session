 
def run(column_number):
	if column_number <= 0:
		exit
	char_output = []
	while column_number > 0 :
		column_number -= 1
		output_char = (column_number % 26)  
		char_output.insert(0, chr(65+output_char))
		column_number = column_number // 26
	print(char_output)
	return char_output

assert run(52) == ['A', 'Z'] 
assert run(54) == ['B', 'B'] 
assert run(702) == ['Z','Z'] 
assert run(704) == ['A','A', 'B'] 
assert run(0) == []

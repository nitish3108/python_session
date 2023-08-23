
input_file = '/mnt/d/linux/python_session/machine-readable-business-employment-data-mar-2023-quarter.csv'  
output_file = '/mnt/d/linux/python_session/output_csv.csv'  

data_value_column_index = 2
subject_column_index = 7

def run():
	ifh = open(input_file)
	ofh = open(output_file, "w")
	for index, line in enumerate(ifh):
		output_string = ""
		line = line.strip()
		input_line_list = line.split(",")
		#print(columns)
		input_line_list[data_value_column_index], input_line_list[subject_column_index] = \
								input_line_list[subject_column_index],\
								input_line_list[data_value_column_index]

		line = ','.join(input_line_list) + '\n'
		ofh.write(line)
	ifh.close()
	ofh.close()
	print("Completed")

assert run() == None

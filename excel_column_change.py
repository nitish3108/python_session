
input_file = '/mnt/d/linux/python_session/input_csv.csv'  
output_file = '/mnt/d/linux/python_session/output_csv.csv'  

def run():
	ifh = open(input_file)
	ofh = open(output_file, "w")
	for line in ifh:
		line = line.strip()
		a,b,c,d,e,f = line.split(",")
		output_string = a + "," + d + "," +  c  + "," + b + "," +  e + "," + f + "\n"
		ofh.write(output_string)

assert run() == None

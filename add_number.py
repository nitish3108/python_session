
def add_numbers(list1, list2):
	result = []
	carry = 0

	index1 = len(list1) - 1
	index2 = len(list2) - 1

	while index1 >= 0 or index2 >= 0 or carry > 0:
		if index1 >= 0:
			digit_list1 = list1[index1] 
		else:
			digit_list1 = 0 
		
		if index2 >= 0: 
			digit_list2 = list2[index2] 
		else: 
			digit_list2 = 0 

		sum_num = digit_list1 + digit_list2 + carry
		carry = sum_num // 10
		result.insert(0, sum_num % 10)

		index1 -= 1
		index2 -= 1

	return result

def main():
	number1 = [1, 3, 5]
	number2 = [2, 5]
	output = add_numbers(number1, number2)
	print(output)


if __name__ == main():
	main()

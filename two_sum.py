
#def my_function(input_list, target):
#	target_eq_list = []
#	for num in input_list:
#		for num2 in input_list:
#			if num + num2 == target:
#				target_eq_list.append(num)
#				target_eq_list.append(num2)
#				return target_eq_list
#	return target_eq_list
#
#input_list = [1, 2, 3, 4]
#output = my_function(input_list, 5)
#print(output)


def my_function(input_list, target):
	num = 0
	target_eq_list = {}
	for i in range(len(input_list)):
		target_eq_list[input_list[i]] = input_list[i]
	for i in range(len(input_list)):
		num = target - target_eq_list[input_list[i]]
		if target_eq_list[num]:
			return [input_list[i], num]

input_list = [1, 2, 3, 4]
output = []
output = my_function(input_list, 5)

print(output)






























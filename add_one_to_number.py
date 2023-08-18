carry = 1
input_number = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
length = len(input_number)
# print(length)
for i in range(length):
    if input_number[ length - 1 ] + carry > 9 :
        carry = ( input_number[length - 1] + carry ) - 9
        input_number[ length - 1 ] = 0
    else :
        input_number[ length - 1 ] += carry
        carry = 0
    length -= 1
if carry == 1:
    input_number.insert(0, 1)
print(input_number)
# print(len(input_number))
decimal_list = []
num = input('Enter the binary number: ')
for i in num.split('.'):
    decimal = int(i, 2)  # Convert binary to decimal
    decimal_list.append(str(decimal))
print('.'.join(decimal_list))

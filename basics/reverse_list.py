number = [10, 20, 30, 40, 50]
reverse_number = []
for index in range(len(number) - 1, -1, -1):
    reverse_number.append(number[index])
print(reverse_number)
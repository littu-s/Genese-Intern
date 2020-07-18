number = 1015
sum = 0
result
for i in range(1, number + 1):
    if number % i == 0:
        sum += pow(i, 2)
result = sum % 109
print(result)

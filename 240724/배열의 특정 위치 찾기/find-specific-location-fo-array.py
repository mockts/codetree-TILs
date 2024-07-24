numbers = list(map(int, input().split()))

even_sum = sum(numbers[i] for i in range(1, 10, 2))
multiple_of_3_values = [numbers[i] for i in range(2, 10, 3)]
average_multiple_of_3 = round(sum(multiple_of_3_values) / len(multiple_of_3_values), 1)

print(even_sum, average_multiple_of_3)
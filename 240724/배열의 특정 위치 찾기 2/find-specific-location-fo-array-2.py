numbers = list(map(int, input().split()))

odd_sum = sum(numbers[i] for i in range(0, 10, 2))
even_sum = sum(numbers[i] for i in range(1, 10, 2))

difference = max(odd_sum, even_sum) - min(odd_sum, even_sum)

print(difference)
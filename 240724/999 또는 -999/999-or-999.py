numbers = list(map(int, input().split()))
end_index = numbers.index(999) if 999 in numbers else numbers.index(-999)
valid_numbers = numbers[:end_index]
max_value = max(valid_numbers)
min_value = min(valid_numbers)
print(max_value, min_value)
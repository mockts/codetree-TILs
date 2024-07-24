char_array = ['L', 'E', 'B', 'R', 'O', 'S']
search_char = input().strip()

if search_char in char_array:
    print(char_array.index(search_char))
else:
    print("None")
while True:
    input_data = input().split()
    width = int(input_data[0])
    height = int(input_data[1])
    character = input_data[2]

    area = width * height
    print(area)

    if character == 'C':
        break
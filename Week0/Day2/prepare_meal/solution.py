def prepare_meal(number):
    max_power = 0
    output_string = ''
    temp_number = number
    while temp_number % 3 == 0:
        max_power += 1
        temp_number = temp_number // 3

    for i in range(max_power):
        output_string += 'spam '

    if temp_number is not number and not number % 5:
        output_string += 'and '
    else:
        output_string = output_string[:-1]

    if number % 5 == 0:
        output_string += 'eggs'

    return output_string


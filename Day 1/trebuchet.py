import re

# Dict to replace number text strings with numbers
valid_num_strings = {'one': '1', 'two':'2', 'three': '3', 'four': '4', 'five': '5', 'six' : '6', 'seven': '7', 'eight' :'8', 'nine': '9'}

# Regex pattern
pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

# Testing with Example provided
with open('example_input.txt', 'r') as example_input:
    lines = example_input.readlines()
    product = 0
    for line in lines:
        digits = re.findall(pattern, line)
        for idx, digit in enumerate(digits):
            if digit in valid_num_strings.keys():
                replacement_val = valid_num_strings[digit]
                digits[idx] = replacement_val

        print(digits)

        calibration_value = int(str(digits[0]) + str(digits[-1]))
        product += calibration_value

    print(product)

# Duplicating Example with real input
with open('trebuchet_input.txt', 'r') as example_input:
    lines = example_input.readlines()
    product = 0
    cal_vals = []
    for line in lines:
        digits = re.findall(pattern, line)
        for idx, digit in enumerate(digits):
            if digit in valid_num_strings.keys():
                replacement_val = valid_num_strings[digit]
                digits[idx] = replacement_val

        # Convert string representation to integer
        calibration_value = int(str(digits[0]) + str(digits[-1]))
        cal_vals.append(calibration_value)
        product += calibration_value

    print(f"RESULT: {product}")

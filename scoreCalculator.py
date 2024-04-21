# Mapping from the image, as seen there are 24 positions with specified values, either with '+' or '*'
mapping = {
    4: 20, 
    5: '*3',
    6: '*3',
    7: '*2',
    8: '*2',
    9: '*2',
    10: 5, 
    11: 4, 
    12: 3, 
    13: 2, 
    14: 1,
    15: 2,
    16: 3, 
    17: 4, 
    18: 5, 
    19: '*2', 
    20: '*2',
    21: '*2', 
    22: '*3', 
    23: '*3', 
    24: 20,
}

# Inputs provided by the user
input1 = int(input("Enter first input (between 4 and 24): "))
input2 = int(input("Enter second input (between 4 and 24): "))
input3 = int(input("Enter third input (between 4 and 24): "))
input4 = int(input("Enter fourth input (between 4 and 24): "))
input5 = int(input("Enter fifth input (between 4 and 24): "))

inputs = [input1, input2, input3, input4, input5]

# Convert the inputs based on the mapping
converted_inputs = [mapping[i] if i in mapping else None for i in inputs]

# Adjusted code to account for the case when all five inputs are '*'

# Initialize sum for '+' and product for '*' values
plus_sum = 0
times_product = 1
star_count = 0  # Counter for '*' inputs

# Process each converted input
for value in converted_inputs:
    if isinstance(value, int):  # This is a '+' value
        plus_sum += value
    elif '*' in str(value):  # This is a '*' value
        star_count += 1
        times_product *= int(str(value).replace('*', ''))

# If all five inputs are '*', multiply by 1 first.
if star_count == 5:
    times_product *= 1

# Calculate final score
score = plus_sum * times_product if plus_sum > 0 else times_product

print(inputs)
print(converted_inputs)
print(score)

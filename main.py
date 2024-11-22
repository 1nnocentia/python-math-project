#import module
from feature.calculate_sum import calculate_sum
from feature.calculate_product import calculate_product
from feature.calculate_difference import calculate_difference
from feature.calculate_division import calculate_division

#user input
a = int(input('Input the first number: '))
b = int(input('Input the second number: '))

#assign calculation
product_result = calculate_product(a,b)
difference_result = calculate_difference(a,b)
sum_result = calculate_sum(a,b)
division_result = calculate_division(a,b)

#print output
print()
print(f'Product | {a} * {b}: {product_result}')
print(f'Difference | {a} - {b}: {difference_result}')
print(f"Sum | {a} + {b} = {sum_result}")
print(f"Division | {a} / {b}= {division_result}")
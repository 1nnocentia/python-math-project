#import module
from feature.calculate_sum import calculate_sum
from feature.calculate_difference import calculate_difference
from feature.calculate_product import calculate_product
from feature.calculate_division import calculate_division

#testing
a = 10
b = 5
sum_result = calculate_sum(a,b)
difference_result = calculate_difference(a,b)
product_result = calculate_product(a,b)
division_result = calculate_division(a,b)

print(f'Sum: {sum_result}')
print(f'Difference: {difference_result}')
print(f'Product: {product_result}')
print(f'Division: {division_result}')

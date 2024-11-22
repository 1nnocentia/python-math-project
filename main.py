#import module
from feature.calculate_sum import calculate_sum
from feature.calculate_product import calculate_product
from feature.calculate_difference import calculate_difference
from feature.calculate_division import calculate_division

a=10
b=5

product_result = calculate_product(a,b)
difference_result = calculate_difference(a,b)
sum_result = calculate_sum(a,b)
division_result = calculate_division(a,b)

print(f'Product: {product_result}')
print(f'Difference: {difference_result}')
print(f"Sum = {sum_result}")
print(f"Division = {division_result}")
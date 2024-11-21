#import module
from feature.calculate_product import calculate_product
from feature.calculate_difference import calculate_difference

#testing
a = 10
b = 5

product_result = calculate_product(a,b)
difference_result = calculate_difference(a,b)

print(f'Product: {product_result}')
print(f'Difference: {difference_result}')

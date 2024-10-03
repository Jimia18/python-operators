# Operator precedence
# This describes the order in which operations are performed in an expression
#operators with a higher precedence are evaluated first 
result = 3*4+5
print(result)
result_two = 3*(4+5)
print(result_two)
result_three = 3*4+5-1
print(result_three)
result_four = 3*(4+5)-1
print(result_four)
#what would be the out of the following expression
result_five = 5*3**2 
print(result_five)

result_six = (5+3)*2**2-10/2
print(result_six)

result_seven = 25/5+2*1
print(result_seven)

result_eight = (25/5)+2*1
print(result_eight)
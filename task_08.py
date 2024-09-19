def is_number(s):
    try:
        float(s) 
        return True
    except ValueError:
        return False

def multiply_numbers(*inputs):
    if not isinstance(inputs, str): inputs = str(inputs)
    nums = [i for i in inputs if is_number(i)]
    if len(nums) <= 0: return None

    num = 1
    for i in nums: num *= float(i)

    return num

multiply_numbers()          # => None
multiply_numbers('ss')      # => None
multiply_numbers('1234')    # => 24
multiply_numbers('sssdd34') # => 12
multiply_numbers(2.3)       # => 6
multiply_numbers([5, 6, 4]) # => 120
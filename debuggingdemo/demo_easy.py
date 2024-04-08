def divide_numbers(a, b):
    return a / b 

print(divide_numbers(2,23)) # happy case 
# print(divide_numbers(2,0)) # ->  division by zero


# print(divide_numbers('a',23)) # ->  unsupported operand type(s) for /: 'str' and 'int'

class SomeRandomError:
    type_error: str

def divide_numbers_fix_bug(a, b):
    if b == 0:
        print("B is invalid : B khong hop le")
        # return None
        return SomeRandomError()
    # elif type(a) is not int and type(b) is not int: 
    # elif type(a) is not int and type(b) is int: 
    # elif type(a) is int and type(b) is not int: 
        # Huy Hoang: A & B is not int (Lan, Ninh)
        # Ngoc: A || B is not int (Hoang, Ngoc)
        # divide_numbers_fix_bug( "asdfasdf", "asdfasdf") (a la string, b la string) . 
    elif type(a) is not int or type(b) is not int:
        print("Mot trong 2 thong so khong hop le") 
        return None
    return a / b


print(divide_numbers_fix_bug(2,0)) # happy case 
# B is invalid : B khong hop le
# None

print(divide_numbers_fix_bug('a',23)) # unhappy case 
# Mot trong 2 thong so khong hop le
# None


# divide_numbers_fix_bug(0.12312, -32e-1)

# Tip hiện tại cho mọi người demo việc tìm bug:
# NHỒI nhiều đầu vào cho hàm số
divide_numbers_fix_bug(2,0) 
divide_numbers_fix_bug(2,-123)
divide_numbers_fix_bug("ádf",23)
divide_numbers_fix_bug(234,"ádfasdf")
a = None
b = None
divide_numbers_fix_bug(a,b)
divide_numbers_fix_bug(_,_) 

# parameter 
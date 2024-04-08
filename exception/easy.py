def ham_chia_so(a,b):
    print("inside ham chia so")
    if b == 0:
        raise ZeroDivisionError
    return a /b

def ham_chia_so_2(a,b):
    print("inside ham chia so")
    if b is not int:
        raise ValueError
    return a /b

def ham_chia_so_exeption(a, b):
    print("inside exception")
    return (a + b)

try:
    print("normal")
    print("normal")
    print("not normal")
    print("normal")
    print("normal")
    print("normal")

    print(ham_chia_so(10,'a'))
    print(ham_chia_so_2(10,0))
except ZeroDivisionError as e:
    print("Error:", e)
    print(ham_chia_so_exeption(10, 0))
    ...
    ...


#-------------------------

# try:
#     file = open("nonexistent_file.txt", "r")
# except FileNotFoundError as e:
#     print("Error:", e)
#     file = None

#-------------------------

# try:
#     number = int("abc")
# except ValueError as e:
#     print("Error:", e)
#     number = None

from io import TextIOWrapper


file = open("test.txt", "r")
try:
    file = open("test.txt", "r") # loi
    number_str = file.readline().strip()


except FileNotFoundError as file_error:
    print("File Error:", file_error)
    # Handle file error
except FileExistsError as file_error:
    print("File Error:", file_error)
    # Handle file error
except ZeroDivisionError as division_error:
    print("Division Error:", division_error)
finally:
    if 'file' in locals():
        file.close()

 file = open("test.txt", "r") # loi co the o day
 number_str = file.readline().strip()
 number = int(number_str) # loi co the o day
 result = number / 0     # loi co the o day
 if 'file' in locals():
     file.close()

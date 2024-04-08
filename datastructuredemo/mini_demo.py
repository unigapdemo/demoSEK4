array = []

array.append("http:/gooogle.com")
array.append("https://facebook.com")
array.append("asdfa")
array.append(1) 
                  # 0                       1                   2     3  
print(array) # ['http:/gooogle.com', 'https://facebook.com', 'asdfa', 1]

# pop -> pop "1"
array = []
array[-1]

# [null ->'http:/gooogle.com' > 'https://facebook.com' -> 'asdfa' -> 1]

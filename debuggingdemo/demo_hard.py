import threading

counter = 0

def increment_counter():
    global counter
    for _ in range(100000):
        counter += 1

threads = []
for i in range(2):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")




# import threading

# counter = 0
# counter_lock = threading.Lock()

# def increment_counter():
#     global counter
#     for _ in range(100000):
#         with counter_lock:
#             counter += 1

# threads = []
# for i in range(2):
#     thread = threading.Thread(target=increment_counter)
#     threads.append(thread)

# for thread in threads:
#     thread.start()

# for thread in threads:
#     thread.join()

# print(f"Final counter value: {counter}")

counter = 0

def increment_counter():
    global counter
    counter = counter + 1

for i in range(5):
    increment_counter()
    print("Counter:", counter)
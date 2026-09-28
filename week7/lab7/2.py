def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


result = add(10, 20)
print("Result:", result)
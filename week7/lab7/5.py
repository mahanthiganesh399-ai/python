from functools import wraps

is_logged_in = True

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")

    return wrapper


@require_login
def view_profile():
    print("Profile opened")


view_profile()
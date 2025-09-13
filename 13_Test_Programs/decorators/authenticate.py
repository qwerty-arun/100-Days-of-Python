# Write a decorator that checks if the user is authenticated before running the function (simulate)

import functools

def require_authentication(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not getattr(user, "is_authenticated", False):
            raise PermissionError("User must be authenticated to call this function.")
        print(f"[Auth Check] User '{user.username}' is authenticated.")
        return func(user, *args, **kwargs)
    return wrapper

# Example of a simple user class
class User:
    def __init__(self, username, authenticated=False):
        self.username = username
        self.is_authenticated = authenticated

@require_authentication
def view_dashboard(user):
    return f"Welcome to {user.username}'s dashboard!"

# Testing
alice = User("alice", authenticated=True)
bob = User("bob", authenticated=False)

print(view_dashboard(alice))   # ✅ Allowed

print(view_dashboard(bob))     # ❌ Will raise PermissionError
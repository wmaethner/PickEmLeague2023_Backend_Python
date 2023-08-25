from functools import wraps

from flask import g, request


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        print("Token required")
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            g.token = token
        print(token)

        return f(*args, **kwargs)

    return decorator

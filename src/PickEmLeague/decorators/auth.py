from functools import wraps

from flask import g, request

from src.PickEmLeague.models.user import User


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        # print("Token required")
        token = None
        # print(request.headers)
        if "Authorization" in request.headers:
            print(f"Authorizations: {request.headers['Authorization']}")
            token = request.headers["Authorization"]
            result = User.decode_access_token(token.split(" ")[1])

            # print(result.value)
            g.token = token
            print(result.value["id"])
            user = User.find_by_id(result.value["id"])
            print(user)
            g.user = user
            # g.
        # print(token)

        return f(*args, **kwargs)

    return decorator

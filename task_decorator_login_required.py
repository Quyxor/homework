import hashlib


auth = False


def make_token(username, password):
    s = username + password

    return hashlib.md5(s.encode()).hexdigest()


def check_auth(input_token):
    with open('token.txt') as token_file:
        true_token = token_file.read()

    return input_token == true_token


def login_required(function):

    def decorator():
        global auth

        if not auth:
            for login_try in range(3):
                auth = check_auth(make_token(input(), input()))
                if auth:
                    break

        return function() if auth else None

    return decorator

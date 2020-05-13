from flask import abort, request


def get_token_from_header():
    authorization_header = request.headers.get('Authorization')
    if authorization_header:
        authorization_header = authorization_header.split()
        try:
            user_token_hs256 = authorization_header[1]
            return user_token_hs256
        except IndexError:
            abort(400)
    else:
        abort(400)

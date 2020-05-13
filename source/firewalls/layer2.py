from functools import wraps
from source import tools, session
from flask import request


def permission_validation_system(f):
    @wraps(f)
    def decorated_function(log_record_obj):
        print('L2')
        hs256_token = tools.get_token_from_header(request)
        log_record_obj.hs256_token = hs256_token
        session.commit()
        return f(log_record_obj)

    return decorated_function

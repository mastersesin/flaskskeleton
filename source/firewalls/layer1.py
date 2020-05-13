from functools import wraps
from flask import request, abort
from source import session, app
from source.classes.sql import Log
from datetime import datetime
import time


def init_logging_system(f):
    @wraps(f)
    def decorated_function():
        log_record_obj = Log(
            uri=request.full_path,
            header=str(request.headers),
            remote_addr=request.remote_addr,
            scheme=request.scheme,
            method=request.method,
            body_or_param=request.query_string.decode('utf-8') if request.method == 'GET' else str(
                request.get_json()
            ),
            timestamp_utc=time.time()
        )
        session.add(log_record_obj)
        session.commit()

        return f(log_record_obj)

    return decorated_function

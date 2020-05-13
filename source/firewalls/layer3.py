from flask import request, abort
from functools import wraps
from source import session
from source.classes.validator import InterfaceValidator


def input_validation_system(interface):
    def inner_input_validation_system(f):
        @wraps(f)
        def decorated_function(log_record_obj):
            print('L3')
            validator = InterfaceValidator(interface=interface, validate_type='input')
            validator.start_validate()
            validated_param = validator.get_validated_param()

            return f(log_record_obj, validated_param)

        return decorated_function

    return inner_input_validation_system

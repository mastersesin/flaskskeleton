from flask import request, abort, jsonify
from functools import wraps
from source import session
from source.classes.validator import InterfaceValidator


def output_validation_system(interface):
    def output_input_validation_system(f):
        @wraps(f)
        def decorated_function(log_record_obj, validated_param):
            print('L4')
            print(f(log_record_obj, validated_param))
            validator = InterfaceValidator(
                interface=interface,
                validate_type='output',
                output_body_param=f(log_record_obj, validated_param)
            )
            validator.start_validate()

            return jsonify(validator.get_validated_param())

        return decorated_function

    return output_input_validation_system

from flask import abort, request


class InterfaceValidator:
    def __init__(self, interface, validate_type, **kwargs):
        self.validate_type = validate_type
        if self.validate_type == 'input':
            post_body_param = request.get_json()
            url_param = {k: v for k, v in request.args.items()}
            post_body_param.update(url_param)
        elif self.validate_type == 'output':
            post_body_param = kwargs.get('output_body_param')
        self.input_request = post_body_param
        self.interface = interface

    def start_validate(self):
        self.dict_processor(self.interface, self.input_request)
        return True

    def dict_processor(self, interface: dict, input_request: dict):
        for interface_key, interface_value in interface.items():
            try:
                input_request[interface_key]
                if type(interface_value) is type:
                    if interface_value in [int, float, str]:
                        self.single_processor(interface_value, input_request[interface_key])
                    elif interface_value is bool:
                        self.bool_processor(interface_value, input_request[interface_key])
                elif type(interface_value) is dict:
                    self.dict_processor(interface_value, input_request[interface_key])
                elif type(interface_value) is list:
                    self.list_processor(interface_value, input_request[interface_key])
                else:
                    print('Current data type not support')
                    abort(400)
            except KeyError as e:
                print('ABORT require param not found')
                abort(400)
            except AssertionError as e:
                print(e)
                abort(400)
            except TypeError as e:
                print(e)
                abort(400)

    def list_processor(self, interface: list, input_request: list):
        value_interface = interface[0]
        for value_user in input_request:
            if type(value_interface) is type:
                if value_interface in [int, float, str]:
                    self.single_processor(value_interface, value_user)
                elif value_interface is bool:
                    self.bool_processor(value_interface, value_user)
            elif type(value_interface) is dict:
                self.dict_processor(value_interface, value_user)
            elif type(value_interface) is list:
                self.list_processor(value_interface, value_user)

    def single_processor(self, interface_value, input_request_value):
        try:
            assert interface_value == type(input_request_value), 'Data type violate in {}'.format(self.validate_type)
        except AssertionError as e:
            print(e)
            abort(400)

    @staticmethod
    def bool_processor(interface_value, input_request_value):
        try:
            assert type(input_request_value) == interface_value, 'Bool field violate'
        except AssertionError as e:
            print(e)
            abort(400)

    def get_validated_param(self):
        return self.input_request

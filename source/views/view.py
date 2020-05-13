from flask import request, jsonify, Blueprint, abort
from source import app
from source.firewalls import layer1, layer2, layer3, layer4
from source.views.register import I_input_register, I_output_register


@app.route('/register', methods=['POST'])
@layer1.init_logging_system
# @layer2.permission_validation_system | No need permission to register
@layer3.input_validation_system(interface=I_input_register)
@layer4.output_validation_system(interface=I_output_register)
def index(log_record_obj, validated_param):
    return {'code': 3221, 'message': 'hihi'}

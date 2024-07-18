from flask import Blueprint, jsonify, request
from src.v1.model.mdlempleado import MdlEmpleado
empleados=Blueprint('empleados_blueprint',__name__)


@empleados.route('/')
def home():
    try:
        return jsonify({'mensage':'{0}'.format("Hello world")}),200
    except Exception as e:
        return jsonify({'mensage':'{0}'.format(e)}),500

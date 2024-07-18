from flask import Blueprint, jsonify, request
from src.v1.model.mdlutil import MdlUtil
util=Blueprint('empleados_blueprint',__name__)

@util.route('/validardb')
def validarconexiondb():
    try:
        respuesta=MdlUtil.validarconexiondb()
        return jsonify({'mensage':'{0}'.format(respuesta)}),200
    except Exception as e:
        return jsonify({'mensage':'{0}'.format(e)}),500

@util.route('/health')
def check_api_health():
    try:
        resultado=MdlUtil.check_api_health()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as e:
        return jsonify({'mensage':'{0}'.format(e)}),500
from flask import Blueprint

suppliers_bp = Blueprint('suppliers', __name__)

@suppliers_bp.get('/suppliers')
def buscar():
    return 'Teste'


from flask import Blueprint, request, jsonify
from flask_pydantic_spec import Response, Request
from tinydb import Query

from entities.suppliers import Suppliers
from services.suppliers_service import SuppliersService
from startup import FlaskPydanticHandler


suppliers_bp = Blueprint('suppliers', __name__)
service = SuppliersService()
spec = FlaskPydanticHandler().getPydanticSpecInstance()


@suppliers_bp.get('/suppliers')
#@spec.validate(resp=Response(HTTP_200=Suppliers))
def read():
    """ GET - Obtém todos os fornecedores da base. """
    suppliers = service.get()
    return jsonify(suppliers)

@suppliers_bp.post('/suppliers')
@spec.validate(body=Request(Suppliers))
def create():
    """ POST - Inclui um novo fornecedor. """
    supplier = request.context.body.dict()
    service.insert(supplier)
    return supplier

@suppliers_bp.put('/suppliers/<string:id>')
@spec.validate(body=Request(Suppliers))
def update(id):
    """ PUT - Atualiza um fornecedor existente. """
    SupplierQry = Query()
    supplier = request.context.body.dict()
    service.update(supplier, SupplierQry.id == id)
    return supplier

@suppliers_bp.delete('/suppliers/<string:id>')
def delete(id):
    """ DELETE - Remove um fornecedor """
    SupplierQry = Query()
    service.remove(SupplierQry.id == id)
    return jsonify({})
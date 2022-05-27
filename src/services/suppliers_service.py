from .service_base import ServiceBase
from tinydb import TinyDB, Query

class SuppliersService(ServiceBase):
    def __init__(self):
        super().__init__()
        pass

    def get(self):
        return super().get()

    def insert(self, bodyRequest):
        #criar classe de validacao com consulta na base de dados
        #ex: consultar se ja existe um id existente na base antes de cadastrar
        super().insert(bodyRequest)

    def update(self, bodyRequest, query: Query):
        super().update(bodyRequest, query)

    def remove(self, query: Query):
        super().remove(query)


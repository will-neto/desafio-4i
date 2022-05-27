import datetime
from pydantic import BaseModel, constr, validator

class Suppliers(BaseModel):
    id: str
    name: str
    company: str
    created_at: datetime.date = None
    amount_products: int

    @validator('id')
    def id_deve_conter_16_caracteres(cls, v):
        length = 16
        
        if len(v) is not 16:
            raise ValueError(f'Id must be between {length} characters.')
        return v
    
    @validator('name')
    def name_deve_conter_maximo_3_a_50_caracteres(cls, v):
        min_length = 3
        max_length = 50

        if len(v) < min_length or len(v) > max_length:
            raise ValueError(f'''Name must be between {min_length}
                     and {max_length} characters.''')
        return v

    @validator('company')
    def name_deve_conter_maximo_2_a_50_caracteres(cls, v):
        min_length = 3
        max_length = 50

        if len(v) < min_length or len(v) > max_length:
            raise ValueError(f'''Company must be between {min_length} 
                    and {max_length} characters.''')
        return v

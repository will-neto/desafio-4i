from flask_pydantic_spec import FlaskPydanticSpec

class FlaskPydanticHandler:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print('cria classe')
            cls.instance = super(FlaskPydanticHandler, cls).__new__(cls)
            cls.spec = FlaskPydanticSpec(title= "API Rest - Desafio 4i",
                    version = "v1.0")
        else:
            print('reutiliza')
        return cls.instance
    
    @classmethod
    def getPydanticSpecInstance(cls):
        return cls.spec
    
    # spec: None
    
    # @staticmethod
    # def getPydanticSpecInstance():
    #     if (type(spec) is None):
    #         spec = FlaskPydanticSpec()
    #     return spec
         
    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(FlaskPydanticHandler, cls).__new__(cls)
    #     return cls.instance
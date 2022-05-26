from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

from desafio_4i.suppliers.suppliers import suppliers_bp 

app = Flask(__name__)
spec = FlaskPydanticSpec()
spec.register(app)

app.register_blueprint(suppliers_bp)

if __name__ == "__main__":
    app.run()
from flask import Flask
from startup import FlaskPydanticHandler

from controllers.suppliers_controller import suppliers_bp

app = Flask(__name__)
app.register_blueprint(suppliers_bp)

spec = FlaskPydanticHandler().getPydanticSpecInstance()
spec.register(app)

if __name__ == "__main__":
    app.run(debug=True)
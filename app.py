from flask import Flask
from routes.products import products_bp
from routes.admin import admin_bp

app = Flask(__name__)

app.register_blueprint(products_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)

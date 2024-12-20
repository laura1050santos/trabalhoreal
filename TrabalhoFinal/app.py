from flask import Flask
from database import init_app
from controller import campeoesController,userController, loginController

app=Flask(__name__)

app.secret_key = 'Chave_mega_secreta' 

app.register_blueprint (loginController)
app.register_blueprint(campeoesController)
app.register_blueprint(userController)

if __name__ == "__main__":
    init_app(app)
    app.run(debug=False)
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config ['SECRET KEY'] = 'API123'


    from website.Adicionar import add
    from website.delete import excluir
    from website.callApiTeste import call
    from website.ver import ver

    app.register_blueprint(excluir, url_prefix="/")
    app.register_blueprint(add, url_prefix="/")
    app.register_blueprint(ver, url_prefix="/")
    app.register_blueprint(call, url_prefix="/")


    return app

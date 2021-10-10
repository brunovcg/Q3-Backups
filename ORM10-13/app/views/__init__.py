from flask import Flask

def init_app(app: Flask) -> None:
    from .create_regiao import bp_create_regiao

    app.register_blueprint(bp_create_regiao)

    from .create_estado import bp_create_estado

    app.register_blueprint(bp_create_estado)

    from .create_capital import bp_create_capital

    app.register_blueprint(bp_create_capital)

    # Vamos adicionar as blueprints novas para registrarmos
    # em nosso app
    from .create_bacia_hidrografica import bp_create_bacia_hidrografica as bp_cbh

    app.register_blueprint(bp_cbh)

    from .create_bacia_estado import bp_create_bacia_estado

    app.register_blueprint(bp_create_bacia_estado)

import os
from flask import Flask

def create_app(config=None):
    app = Flask('matthew')

    app.config.update(dict(
        DEBUG=True,
        SECRET_KEY='123456',
        USERNAME='admin',
        PASSWORD='admin'
    ))
    app.config.update(config or {})
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)
    return app

app = create_app()

import blog.views


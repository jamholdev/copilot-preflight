"""ClaimsBot: a tiny, deliberately boring claims-status API.

All data is synthetic. This app exists to demo GitHub Copilot adoption
with guardrails (CodeQL, Copilot Autofix, rulesets) for regulated customers.
"""
import os

from flask import Flask

from . import db
from .claims import bp as claims_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "claimsbot.sqlite"),
    )
    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)
    app.register_blueprint(claims_bp)
    return app

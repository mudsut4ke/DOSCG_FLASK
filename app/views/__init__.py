import os
from flask import Blueprint
from app.controllers.DOSCG import *
from app.controllers.DOSCG_LINE import line_callback

template_dir = os.path.abspath("app/views/template")

DOSCG_blueprints = Blueprint("DOSCG", "api", template_folder=template_dir)
DOSCG_blueprints.add_url_rule("/", view_func=index, methods=["GET"])
DOSCG_blueprints.add_url_rule("/func1", view_func=func1, methods=["GET"])
DOSCG_blueprints.add_url_rule("/func2", view_func=func2, methods=["GET"])
DOSCG_blueprints.add_url_rule("/func3", view_func=func3, methods=["GET"])
DOSCG_blueprints.add_url_rule("/resume", view_func=resume, methods=["GET"])
DOSCG_blueprints.add_url_rule(
    "/line_callback", view_func=line_callback, methods=["POST"]
)

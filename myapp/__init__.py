from flask import Blueprint
from . import views

myapp=Blueprint("myapp",__name__)

# registry route
myapp.add_url_rule(rule="/",view_func=views.index)
myapp.add_url_rule(rule="/add",view_func=views.add)
myapp.add_url_rule(rule="/list",view_func=views.list)
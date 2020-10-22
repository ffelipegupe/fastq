from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.stores import *
from api.v1.views.foods import *
from api.v1.views.drinks import *
from api.v1.views.order import *

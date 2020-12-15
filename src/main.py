from aiohttp import web
import json
from api import get_routes


app = web.Application()
app.add_routes(get_routes())
web.run_app(app)
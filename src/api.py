import implementation
from aiohttp import web
import json

routes = web.RouteTableDef()

def get_routes():
    return routes

@routes.get('/user')
async def get_user_data(request):
    user = request.query['id']
    return await implementation.get_user_data(user)    
    

@routes.post('/user/{id}')
async def create_user_data(request):
    data = await request.json()
    print(data)
    user = request.match_info['id']
    print(user)
    return await implementation.set_user_data(user, data["name"], data["contactNumber"], data["businessName"])  

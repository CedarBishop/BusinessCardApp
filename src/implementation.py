from pymongo import MongoClient
from aiohttp import web
import json


def get_mongo_client():
    return MongoClient()


async def get_user_data(user):
    response_obj = {'status':'success'}
    return web.Response(text=json.dumps(response_obj), status=200)


async def set_user_data(user, name, number, business_name):
    response_obj = {'name':name}
    return web.Response(text=json.dumps(response_obj), status=200)
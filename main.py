import asyncio
from aiogram.utils.json import json
from aiohttp import web

import modules
from constants import stopcovidurl, stopcovidinfourl


async def region(request):
    reg = request.match_info['region']
    response = await modules.get_json(stopcovidurl, reg)
    return web.Response(text=json.dumps(response))


async def fucking_stats(url):
    response = await modules.get_fucking_stats(stopcovidinfourl)
    response = str(response)
    response = response.replace("'", '"')
    return web.Response(text=json.dumps(response))


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/get_region/{region}', region)])
    app.add_routes([web.get('/get_all', fucking_stats)])
    web.run_app(app, host="0.0.0.0")

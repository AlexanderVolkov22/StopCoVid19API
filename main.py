#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============
#      Main script file
# ==============
import asyncio
from aiogram.utils.json import json
from aiohttp import web

import modules
from constants import stopcovidurl, stopcovidinfourl, region_codes


async def region(request):
    reg = request.match_info['region']
    response = await modules.get_json(stopcovidurl, reg)
    return web.Response(text=json.dumps(response))


async def fucking_stats(url):
    response = await modules.get_fucking_stats(stopcovidinfourl)
    response = str(response)
    response = response.replace("'", '"')
    res = response.encode().decode("unicode_escape")
    return web.Response(text=res)


async def resp_data(request):
    code = request.match_info['code']
    if code == "region_code":
        return web.Response(text=json.dumps(region_codes))
    else:
        resp_obj = {'status': 'Wrong request'}
        return web.Response(text=json.dumps(resp_obj))


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/get_region/{region}', region)])
    app.add_routes([web.get('/get_all', fucking_stats)])
    app.add_routes([web.get('/data/{code}', resp_data)])
    web.run_app(app, host="0.0.0.0")

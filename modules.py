#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============
#      Main script file
# ==============
import datetime

import aiohttp
from aiogram.utils import json
from bs4 import BeautifulSoup


async def gettime():
    dateandtime = str(datetime.datetime.now())
    date1 = dateandtime.split(" ")[-2]
    date = date1.split("-")[-1]
    month = date1.split("-")[-2]
    year = date1.split("-")[-3]
    date = date + "." + month + "." + year
    return date

async def get_json(url, code):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + code) as resp:
            res = await resp.json(content_type='text/javascript')
            res = str(res)
            res = res.replace("'", '"')
            print(res)
            media = json.loads(res)
            date = media[0]["date"]
            sick_new = media[0]["sick"]
            sick_old = media[1]["sick"]
            sick_chng = int(sick_new) - int(sick_old)
            sick_chng = str(sick_chng)
            healed_new = media[0]["healed"]
            healed_old = media[1]["healed"]
            healed_chng = int(healed_new) - int(healed_old)
            healed_chng = str(healed_chng)
            died_new = media[0]["died"]
            died_old = media[1]["died"]
            died_chng = int(died_new) - int(died_old)
            died_chng = str(died_chng)
            response = {"date": date, "sick": sick_new, "sick_change": sick_chng, "healed": healed_new, "healed_change": healed_chng, "died": died_new, "died_change": died_chng}
            return response

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_fucking_stats(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        sp = soup.find("div", "cv-section__content").find("cv-stats-virus")
        sp = str(sp)
        sp = sp.split(":stats-data=")[1]
        sp = sp.replace("'></cv-stats-virus>", "")
        sp = sp.replace("'", "")
        print(sp)
        return sp

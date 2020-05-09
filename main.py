import asyncio
import aiohttp
from aiogram.utils.json import json
from bs4 import BeautifulSoup


import modules
from constants import stopcovidurl
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}


async def get_json(url, code):
    async with aiohttp.ClientSession() as session:
        async with session.get(url + code) as resp:
            json = await resp.json(content_type='text/javascript')
            return json


async def jsonget():
    response = await get_json(stopcovidurl, "RU-ARK")
    time = await modules.gettime()
    print(time)


async def get_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.text()
            return text


async def main():
    response = await get_html(stopcovidurl)
    soup = BeautifulSoup(response, 'html.parser')
    sup = soup.find('div', class_='cv-section__container _g-outer-width _g-inner-padding')
    print(sup)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

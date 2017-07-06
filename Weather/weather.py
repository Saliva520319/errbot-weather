#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
import requests

from errbot import BotPlugin, botcmd

# 和风天气key
TOKEN = ''

# api地址
URL = "https://free-api.heweather.com/v5/weather?city={0}&key={1}"


class Weather(BotPlugin):
    """Commands to get the weather info from heweather API."""
    @botcmd()
    def weather(self, msg, args):
        """
        Use !weather [city_name] to see the weather forcast.
        Default will be Beijing.
        """
        url = (URL.format(args) if len(args)
               else URL.format('beijing',TOKEN)).strip()
        res = requests.get(url)
        data = json.loads(res.text)
        day = data['HeWeather5'][0]['daily_forecast'][0]
        return '{} : 白天 {} 夜间 {} 气温 {}~{} {} {}'.format(data['HeWeather5'][0]['basic']['city'], day['cond']['txt_d'],
                                                        day['cond']['txt_n'], day['tmp']['max'], day['tmp']['min'], day['wind']['sc'],
                                                        day['wind']['dir'])

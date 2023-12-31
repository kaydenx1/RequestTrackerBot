#!/usr/bin/env python3


"""Importing"""
from os import environ


class Config(object):
    API_ID = int(environ.get("API_ID", 27473362))
    API_HASH = environ.get("API_HASH", "099c6626bcc1b0f8dc0183cc10cc4015")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6960032358:AAFuMp-BUqU1fl5Bql77_oiOND14bcb-Odg")
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://request:request@cluster0.x1eesbr.mongodb.net/?retryWrites=true&w=majority")

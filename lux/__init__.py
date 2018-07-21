import os

from flask import Flask

HOST_V = 'HOST'
PORT_V = 'PORT'

LUX_HOST = os.environ.get(HOST_V, "127.0.0.1")
LUX_PORT = os.environ.get(PORT_V, "5000")

lux = Flask(__name__)
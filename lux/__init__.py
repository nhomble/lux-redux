import os

from flask import Flask

HOST_V = 'HOST'
PORT_V = 'PORT'
AUTH_V = 'AUTH'

LUX_HOST = os.environ.get(HOST_V, "127.0.0.1")
LUX_PORT = os.environ.get(PORT_V, "5000")
LUX_AUTH = os.environ.get(AUTH_V, "local")

lux = Flask(__name__)
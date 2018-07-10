import os

from flask import Flask

PORT_V = 'PORT'

LUX_PORT = os.environ.get(PORT_V, 5000)

lux = Flask(__name__)
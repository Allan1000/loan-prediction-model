"""Waitress (Web Server Gateway Interface)
"""

from waitress import serve
import hello_world
serve(hello_world.app,host='0.0.0.0',port=8000)

# Code to run in terminal : python waitress_server.py
# Url link: http://LAPTOP-3M57MF1K:8000/users/Allan

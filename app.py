import socket
from logging.config import fileConfig

from flask import Flask

app = Flask(__name__)

fileConfig('logging.conf')


@app.route('/')
def base():
    app.logger.info('Ping')
    return "OK"


@app.route('/ip')
def get_ip():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    app.logger.info('Hostname %s IP Address is %s', hostname, ipaddress)
    return ipaddress


if __name__ == '__main__':
    app.run()

import socket
from logging.config import fileConfig

import boto3
import requests
from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask

app = Flask(__name__)

fileConfig('logging.conf')

xray_recorder.configure(service='py-app')
XRayMiddleware(app, xray_recorder)
patch_all()


@app.route('/')
def default():
    app.logger.info('healthcheck')
    return "healthcheck"


@app.route('/ip')
def ipAddress():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    app.logger.info('Hostname %s IP Address is %s', hostname, ipaddress)
    return ipaddress


# test http instrumentation
@app.route('/outgoing-http-call')
def callHTTP():
    resp = requests.get("https://aws.amazon.com")
    app.logger.info('Outgoing HTTP call to %s with status code %s', resp.url, resp.status_code)
    return "Ok! tracing outgoing http call. Resp: %s" % resp.url


# test aws sdk instrumentation
@app.route('/aws-sdk-call')
def callAWSSDK():
    client = boto3.client('s3')
    client.list_buckets()
    app.logger.info('Call to list s3 buckets')
    return 'Ok! tracing aws sdk call'


if __name__ == '__main__':
    app.run()

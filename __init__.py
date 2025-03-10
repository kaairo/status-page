import time
import json
import requests
import datetime
import threading
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from flask import Flask, render_template
from utils import samp

# Application
app = Flask(__name__)
f = open('config.json')
config = json.load(f)

# Services list
f = open('services.json')
services = json.load(f)

# Ping table
ping_table = {
    "HTTP/S": 200,
    "SAMP": 250,
    "UDP": 250,
    "TCP": 250
}

# Checker
def checkStatus(service):
    while True:
        problems = []

        # Check HTTP/S
        if service['type'] == 'HTTP/S':
            try:
                req = requests.get(service['destination'], timeout = 3, verify = False)
                service['message'] = f'{req.status_code} {requests.status_codes._codes[req.status_code][0]}'

                if req.status_code == 200:
                    service['status'] = 'online'
                else:
                    service['status'] = 'problems'
                    problems.append('The site backend is not working')

                service['response_time'] = round(req.elapsed.microseconds / 1000)
            
            except Exception as ex:
                service['message'] = type(ex).__name__
                service['status'] = 'offline'

        # Check SAMP
        elif service['type'] == 'SAMP':
            start = datetime.datetime.now()

            try:
                addr, port = service['destination'].split(':')
                req = samp.send_query(addr, int(port), 'i')
                if req:
                    service['status'] = 'online'
                else:
                    service['status'] = 'offline'

                service['message'] = f'query "i", {len(req)}'
            
            except Exception as ex:
                service['message'] = type(ex).__name__
                service['status'] = 'offline'
            
            service['response_time'] = round( (datetime.datetime.now() - start).microseconds / 1000 )

        # Default
        if service['response_time'] >= ping_table[service['type']]:
            service['status'] = 'problems'
            problems.append(f'The response time is higher than normal ({ping_table[service["type"]]}ms)')

        service['problems'] = problems
    
        time.sleep(5)

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html', services = services, config = config)

if __name__ == "__main__":
    for service in services:
        service['status'] = 'offline'
        service['response_time'] = 0
        service['message'] = 'checking...'

        thread = threading.Thread(name = service['name'], target = checkStatus, args = [service,])
        thread.daemon = True
        thread.start()

    app.run(host = config['host'], port = config['port'], debug = config['debug'])
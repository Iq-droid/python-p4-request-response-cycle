#!/usr/bin/env python3

#importing necessary modules
#1.The 'os' module provides a way of interacting with the operating system.
#2.Flask and related functions are imported from the 'flask' package for creating a web application
import os

from flask import Flask, request, current_app, g, make_response
from urllib.parse import quote #importing quote from urllib.parse

#creating the flask app instance. the '__name__' arg tells flask where to look for necessary resources i.e templates and static files
app = Flask(__name__)

#decorator for function to run before each request and setting the 'g.path' var to abslt path of crrnt wrkng dir of the app
@app.before_request
def app_path():
    g.path = quote(os.path.abspath(os.getcwd()), safe='') #using quote from urllib.parse

#defining route for URL.Flask will execute the'index()' func when user visits the root URL
@app.route('/')
def index():
    #Getting host from the request headers and the name of the flask app.
    host = request.headers.get('Host') #'request' holds all incoming request and data
    appname = current_app.name #'current_app' provides access to the current flask app being run.
    #builds string containing html content with placeholders for 'host', 'appname' and 'g.path' values.
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    
    #defining the http status code and headers for the response. code 200 means a successful response.
    status_code = 200
    headers = {}

    #creating a flask response object using 'make_response()' taking the response body,status code and headers as parameters then constructs HTTP response. the response obj is returned to clients web browser.
    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5557, debug=True)

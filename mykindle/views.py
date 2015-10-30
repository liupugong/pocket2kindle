from flask import Flask, render_template
from .pocketapi import PocketAPI

from .consts import Consts

from mykindle import app
# app = Flask(__name__)


@app.route('/')
def home():
    return 'hello, world'

@app.route('/index')
def index():
    __my_api = PocketAPI()
    request_token = __my_api.obtain_request_token()
    auth_url = Consts.POCKET_URL.format(request_token, Consts.RETURN_URL)
    return render_template("index.html",
                           auth_url=auth_url)


@app.route('/gettoken')
def gettoken():
    __my_api = PocketAPI()
    access_token = __my_api.obtain_access_token()
    return render_template("index.html",
                           auth_url=access_token)


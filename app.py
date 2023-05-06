import logging

from flask import Flask, current_app

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    current_app.logger.info('blah {}'.format('something'))
    logger.info('blah {}'.format('something'))
    return 'ok'

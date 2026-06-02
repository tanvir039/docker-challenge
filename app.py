from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), 
              port=int(os.environ.get("REDIS_PORT", 6379)))

@app.route('/')
def hello_world():
    return f'Hello, World!'

@app.route('/count')
def index():
    redis.incr('hits')
    return 'This page has been visited {} times.'.format(redis.get('hits').decode('utf-8'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
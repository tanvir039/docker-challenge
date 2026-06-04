from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis = Redis(host = redis_host, port = redis_port)

@app.route('/')
def welcome():
    return f'Welcome to the Docker Challenge! This is a simple Flask application that uses Redis to count the number of visits to this page. The Redis server is running on {redis_host}:{redis_port}.'

@app.route('/count')
def index():
    redis.incr('hits')
    return 'This page has been visited {} times.'.format(redis.get('hits').decode('utf-8'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
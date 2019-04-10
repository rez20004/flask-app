import logging
from flask import Flask

app = Flask(__name__)

@app.errorhandler(Exception)
def exception_handler(err):
    app.logger.error(str(err))
    return str(err), 500

@app.route('/health', methods=['GET'])
def health():
    return 'OK'

if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.logger.info('Starting app')
    app.run(host='192.168.99.100', port=8443)


from flask import Flask, jsonify

from . minos import __version__, __program_name__

app = Flask(__name__)

# curl -XGET localhost:5000/api/status
@app.route('/api/status', methods=['GET'])
def status():
    data = { 'name': __program_name__,
             'version': __version__ }
    resp = jsonify(data)
    return resp

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, abort, g

from . minos import __version__, __program_name__
from . experiment import Experiment, ExperimentList

app = Flask(__name__)


def db_open():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = app.minos.driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def db_close(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()

# curl -XGET localhost:5000/api/experiment/<ID>
@app.route('/api/experiment/<int:ident>', methods=['GET'])
def experiment(ident):
    exp = Experiment(ident)
    resp = jsonify(exp.export())
    return resp

# curl -XGET localhost:5000/api/experiment/_list
@app.route('/api/experiment/_list', methods=['GET'])
def experiment_list():
    exps = ExperimentList()
    resp = jsonify(exps.export())
    return resp

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

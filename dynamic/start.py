#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
from flask import abort, jsonify, make_response, request
from models.store import Store
from models.food import Food
from api.v1.views import app_views
#from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
# MySQL connection
#app.config['FASTQ_MYSQL_HOST'] = 'localhost'
#app.config['FASTQ_MYSQL_USER'] = 'fastq_user'
#app.config['FASTQ_MYSQL_PWD'] = 'fastq_dev_pwd'
#app.config['FASTQ_MYSQL_DB'] = 'fastq_dev_db'
#mysql = MySQL(app)

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

@app.route('/', methods=['GET'])
def index():
    #storez = storage.get(Store, store_id)
    return render_template('index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
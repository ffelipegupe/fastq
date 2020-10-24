#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
from flask import abort, jsonify, make_response, request
from models.store import Store
from models.food import Food
from models.drink import Drink
from api.v1.views import app_views

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
<<<<<<< HEAD
# MySQL connection
app.config['FASTQ_MYSQL_HOST'] = 'localhost'
app.config['FASTQ_MYSQL_USER'] = 'fastq_dev'
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

@app.route('/variables1', methods=['GET'])
def index():
<<<<<<< HEAD
    drink = storage.all(Drink).values()
    food = storage.all(Food).values()
    return render_template('index.html', drinks=drink,
                            foods=food)
=======
    drinks_list = storage.all(Drink).values()
    drinks_list = sorted(drinks_list, key=lambda k: k.name)
    return render_template('variables1.html',
                            drinks=drinks_list)
>>>>>>> de48ec698c49b9cb437d3f788bcd20bdd4c4dd6f

@app.route('/orders/<id>', methods=['POST'])
def order(id):
    """ Order checkout endpoint """
    orders = storage.all(Order).values()
    return render_template('checkout.html', orders = orders)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

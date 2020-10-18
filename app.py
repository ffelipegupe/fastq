#from models import 
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySQL connection
app.config['FASTQ_MYSQL_HOST'] = 'localhost'
app.config['FASTQ_MYSQL_USER'] = 'fastq_user'
app.config['FASTQ_MYSQL_PWD'] = 'fastq_dev_pwd'
app.config['FASTQ_MYSQL_DB'] = 'fastq_dev_db'
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM foods')
    data = cur.fetchall()
    return render_template('index.html', datas = data)



if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)

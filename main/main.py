from flask import Flask, render_template, request
import psycopg2
from db_connect import db_connect

app = Flask(__name__,template_folder='web')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def results():
    region = request.form['region']
    conn, cur = db_connect()
    cur.execute("""
        SELECT * FROM cafe
        WHERE address Like %s
        ORDER BY review_count DESC
        LIMIT 20
                """,(f'%{region}%'))
    cafes= cur.fetchall()
    return render_template('results.html', cafes=cafes,region=region)

if __name__ == '__main__':
    app.run(debug=True,port=3000)
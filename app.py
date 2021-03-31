from flask import Flask, request, jsonify
from utils import connect_db

app = Flask(__name__)

data = {}

@app.route('/using_postman', methods=['POST'])
def home():
    global data
    if request.path == '/using_postman':
        if request.method == 'POST':

            data = request.get_json()
            conn, cur=connect_db()
            
            cur.execute("SELECT * from DATA1")
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                if data['email'] in row:
                    return 'email is already exists'

            cur.execute( " INSERT INTO DATA1(first_name, last_name, email, password) VALUES (%s,%s,%s,%s)",
                        (data['first_name'], data['last_name'], data['email'], data['password']))
            conn.commit()

            if conn:
                return jsonify(data)


@app.route('/using_postman/<user>', methods=['GET', 'PATCH', 'DELETE'])
def fetch(user):
    conn, cur=connect_db()
    if request.method == 'GET':
        cur.execute("SELECT * from DATA1 where id=%s", user)
        rows = cur.fetchall()
        conn.commit()
        return str(rows)

    elif request.method == 'DELETE':
        cur.execute("DELETE from DATA1 where id=%s", user)
        conn.commit()
        return 'deleted successfully'


@app.route('/using_postman/<user>/<que>', methods = ['PATCH'])
def fetch1(user, que):
    conn, cur=connect_db()
    if request.method == 'PATCH':
        q_d = ("Update DATA1 set password=%s where id=%s")
        v_q = (user, que)
        cur.execute(q_d, v_q)
        conn.commit()
        return 'updated successfully'
    

if __name__ == '__main__':
    app.run(debug=True)
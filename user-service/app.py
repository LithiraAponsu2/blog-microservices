from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([
        {"id": 1, "username": "john_doe"},
        {"id": 2, "username": "jane_smith"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
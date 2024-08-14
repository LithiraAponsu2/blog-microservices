from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify([
        {"id": 1, "title": "First Post", "content": "Hello, World!"},
        {"id": 2, "title": "Second Post", "content": "This is a test post."}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
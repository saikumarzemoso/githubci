from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "This is a test endpoint"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

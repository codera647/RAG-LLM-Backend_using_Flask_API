from flask import Flask, request, jsonify
from flask_cors import CORS
from main import get_results

app = Flask(__name__)
CORS(app)

@app.route("/get-query", methods=["POST"])
def get_query():
    data = request.get_json()
    results = get_results(data['message'],data['files'])
    response = {"message":results}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
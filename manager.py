from flask import Flask, json, request, make_response, jsonify
import tempfile
from Helio.timer import timer

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_file():
    if request.method == 'POST':
        uploaded_file = request.files['file'].read()
        temp = tempfile.NamedTemporaryFile() # mode='w+t'
        try:
            temp.write(uploaded_file)
            temp.seek(0)
            timer(temp.name)

            return make_response(jsonify({"response": "Graph created, loaded in triple store and added to sql database."}), 201)
        finally:
            temp.close()

    return "KGG Service"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3306)
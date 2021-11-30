from flask import Flask, json, request, make_response, jsonify
import tempfile
from Helio.timer import timer
from Database.executeQueries import executeSPARQLquery

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_file():
    if request.method == 'POST':
        uploaded_file = request.files['file'].read()
        temp = tempfile.NamedTemporaryFile() # mode='w+t'
        try:
            temp.write(uploaded_file)
            temp.seek(0)
            response = timer(temp.name)
            executeSPARQLquery()
            return make_response(jsonify({"response": response[0]}), response[1])
        finally:
            temp.close()

    return "KGG Service"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
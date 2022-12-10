from flask import Flask, jsonify ,request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/create', methods=['GET', 'POST'])
def form_example():

    if request.method == 'POST':

        username = request.form['username']
        points = request.form['points']

        with open(f"accounts/{username}.json","w") as f:

          json.dump({"name":username,"points":points},f)

        return f"{username} Updated Successfully!!"

    # otherwise handle the GET request
    return "Nothing to do here"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

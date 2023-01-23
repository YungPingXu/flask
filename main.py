from flask import Flask, request
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return 'citrus website'

@app.route('/send', methods=['GET', 'POST'])
def send():
    args = request.args.to_dict()
    print(args)
    return args

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
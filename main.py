from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return 'citrus website'

console_list = []

@app.route('/send', methods=['GET', 'POST'])
def send():
    args = request.args.to_dict()
    print(args)
    console_list.append(args)
    return redirect('https://google.com')

@app.route('/backend', methods=['GET'])
def backend():
    return str(console_list)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
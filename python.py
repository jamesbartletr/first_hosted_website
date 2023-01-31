from flask import Flask, render_template, request

app = Flask(__name__)
counter = 0

@app.route('/')
def index():
    return render_template('index.html', counter=counter)

@app.route('/increment', methods=['POST'])
def increment():
    global counter
    counter += 1
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

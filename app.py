from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bangkok')
def bangkok():
    return render_template('bangkok.html')

@app.route('/huahin')
def huahin():
    return render_template('huahin.html')

@app.route('/seka')
def seka():
    return render_template('seka.html')

@app.route('/pattaya')
def pattaya():
    return render_template('pattaya.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
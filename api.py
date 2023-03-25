from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def game():
    return render_template('pong3.html')

if __name__ == '__main__':
    app.run(debug=True)

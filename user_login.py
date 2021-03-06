from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = True
    return render_template('user_login.html', user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask

# Creating an application object.
app = Flask (__name__)

# Route decorator
@app.route('/') # 127.0.0.1:500
def index():
    return '<h1> Hello Puppy !</h1>'

if __name__ == '__main__':
    app.run()
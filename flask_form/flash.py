from flask import Flask, render_template, session, redirect, url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask (__name__)

app.config['SECRET_KEY'] =  'my_key'

class SimpleForm(FlaskForm):
    breed = StringField('What breed are you ?')
    submit = SubmitField('Click Me')

@app.route('/', methods=["GET","POST"])
def flash_form():
    form = SimpleForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to:{session['breed']}")
        return redirect(url_for('flash_form'))
    return render_template('flash.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
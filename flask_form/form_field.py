from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm 
from wtforms import (StringField, BooleanField,  RadioField, 
                        SelectField,  TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you ?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:', 
                        choices=[('mood_one','Happy'), ('mood_two','Excited')])
    food_choice = SelectField(u'Pick your favourite food:',
                                    choices=[('chi','Chiken'), ('bf','Beef'),
                                                ('fish','Fish')])
    feed_back = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def form_field():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feed_back'] = form.feed_back.data

        return redirect(url_for('thankyou'))
    return render_template('form_field.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
    
if __name__ == '__main__':
    app.run(debug=True)
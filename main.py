from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "secret key"

test_pass = '12345678'
test_email = 'admin@email.com'

class LoginForms(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="login", validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET','POST'])
def login():
    login_form = LoginForms()
    if login_form.validate_on_submit():
        email_input = login_form.email.data
        pass_input = login_form.password.data
        if email_input == test_email and pass_input == test_pass:
            return render_template('success.html')
        else:
            return render_template('denied.html')


    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

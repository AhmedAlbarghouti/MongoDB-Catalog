from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AddForm(FlaskForm):
    product_name = StringField('Product Name',
                               validators=[DataRequired(), Length(min=2, max=20)])
    brand = StringField('Brand',
                        validators=[DataRequired(), Length(min=2, max=20)])
    price_cad = DecimalField('Price', validators=[DataRequired()])
    description = TextAreaField('Description',
                                validators=[DataRequired(), Length(min=5, max=100)])
    category = StringField('Category',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')

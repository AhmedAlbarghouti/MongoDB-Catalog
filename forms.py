from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, TextAreaField, FloatField, \
    SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

categories = []


class AddForm(FlaskForm):
    name = StringField('Product Name',
                       validators=[DataRequired(), Length(min=2, max=20)])
    brand = StringField('Brand',
                        validators=[DataRequired(), Length(min=2, max=20)])
    price = FloatField('Price', validators=[DataRequired()])
    description = TextAreaField('Description',
                                validators=[DataRequired(), Length(min=5, max=100)])

    category = SelectField('Category',
                           choices=categories)
    submit = SubmitField('Submit')


class AddCategoryForm(FlaskForm):
    category = StringField('Category Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Submit')


class DeleteCategoryForm(FlaskForm):
    category = SelectField('Category',
                           choices=categories)
    submit = SubmitField('Submit')

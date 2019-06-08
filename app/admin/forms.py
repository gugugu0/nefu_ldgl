# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField, \
    PasswordField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SubmitVulnsForm(FlaskForm):
    title = StringField(u'漏洞标题', validators=[DataRequired(), Length(1, 64)])
    describe = TextAreaField(u'漏洞描述', validators=[DataRequired()])
    rank = SelectField(u'危险等级', coerce=int, validators=[DataRequired()])
    publish_date = DateField(u'发布日期', validators=[DataRequired()])
    fix_date = DateField(u'修复日期', validators=[DataRequired()])

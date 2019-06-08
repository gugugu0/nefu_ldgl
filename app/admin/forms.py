# coding:utf-8
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField, \
    PasswordField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SubmitVulnsForm(FlaskForm):
    title = StringField(u'漏洞标题', validators=[DataRequired(), Length(1, 64)])
    describe = TextAreaField(u'漏洞描述', validators=[DataRequired()])
    type = SelectField('漏洞类型', coerce=int, validators=[DataRequired()])
    rank = SelectField(u'危险等级', coerce=int, validators=[DataRequired()])
    publish_date = DateField(u'发布日期', validators=[DataRequired()])
    fix_date = DateField(u'修复日期', validators=[DataRequired()])
    annex = StringField(u'附件', validators=[DataRequired(), Length(1, 64)])
    organization = StringField(u'所属组织', validators=[DataRequired(), Length(1, 64)])


class ManageVulnsForm(SubmitVulnsForm):
    pass


class DeleteVulnForm(FlaskForm):
    VulnsId = StringField(validators=[DataRequired(), Length(1, 64)])


class DeleteVulnsForm(FlaskForm):
    VulnsIds = StringField(validators=[DataRequired(), Length(1, 64)])


class ConfirmFixForm(FlaskForm):
    VulnsId = StringField(validators=[DataRequired(), Length(1, 64)])


class PlatformInfo(FlaskForm):
    about = TextAreaField(u'关于' ,validators=[DataRequired()])
    help = TextAreaField(u'帮助' ,validators=[DataRequired()])
    title = StringField(validators=[DataRequired(), Length(1, 64)])


class ChangePassowrdForm(FlaskForm):
    old_password = PasswordField(u'原来密码', validators=[DataRequired()])
    password = PasswordField(u'新密码', validators=[
        DataRequired(), EqualTo('password2', message=u'两次输入密码不一致！')])
    password2 = PasswordField(u'确认新密码', validators=[DataRequired()])


class EditUserInfoForm(FlaskForm):
    username = StringField(u'昵称', validators=[DataRequired()])
    email = StringField(u'电子邮件', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'密码确认', validators=[DataRequired()])


class ManagePlatformForm(FlaskForm):
    about = TextAreaField(u'关于' ,validators=[DataRequired()])
    help = TextAreaField(u'帮助' ,validators=[DataRequired()])
    title = StringField(validators=[DataRequired(), Length(1, 64)])
    password = PasswordField(u'密码确认', validators=[DataRequired()])


class ManageAnnouncement(FlaskForm):
    announcements = TextAreaField(u'公告', validators=[DataRequired()])
    password = PasswordField(u'密码确认', validators=[DataRequired()])
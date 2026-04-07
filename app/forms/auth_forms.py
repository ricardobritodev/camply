from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional


class RegisterForm(FlaskForm):
    name = StringField(
        "Nome completo",
        validators=[DataRequired(message="Nome é obrigatório."), Length(min=2, max=120)],
    )
    email = StringField(
        "E-mail",
        validators=[
            DataRequired(message="E-mail é obrigatório."),
            Email(message="E-mail inválido."),
            Length(max=180),
        ],
    )
    password = PasswordField(
        "Senha",
        validators=[
            DataRequired(message="Senha é obrigatória."),
            Length(min=8, message="Senha deve ter ao menos 8 caracteres."),
        ],
    )
    confirm_password = PasswordField(
        "Confirmar senha",
        validators=[
            DataRequired(),
            EqualTo("password", message="As senhas não coincidem."),
        ],
    )
    submit = SubmitField("Criar conta")

    # TODO: [BACKEND] Adicionar validação custom para e-mail único (validate_email)
    # TODO: [BACKEND] Adicionar campo 'role' se fluxo de cadastro de host for separado


class LoginForm(FlaskForm):
    email = StringField(
        "E-mail",
        validators=[
            DataRequired(message="E-mail é obrigatório."),
            Email(message="E-mail inválido."),
        ],
    )
    password = PasswordField(
        "Senha",
        validators=[DataRequired(message="Senha é obrigatória.")],
    )
    remember = BooleanField("Lembrar de mim")
    submit = SubmitField("Entrar")

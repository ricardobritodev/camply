from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.blueprints.auth import auth_bp
from app.extensions import db
from app.models.user import User
from app.forms.auth_forms import LoginForm, RegisterForm


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Cadastro de novo usuário."""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()

    # TODO: [BACKEND] Implementar lógica de registro:
    #   1. Validar form.validate_on_submit()
    #   2. Verificar se e-mail já existe
    #   3. Criar User, chamar set_password(), db.session.add/commit
    #   4. (Opcional) Enviar e-mail de verificação
    #   5. Redirecionar para login com flash de sucesso

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    """Autenticação de usuário existente."""
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()

    # TODO: [BACKEND] Implementar lógica de login:
    #   1. Validar form.validate_on_submit()
    #   2. Buscar usuário por e-mail
    #   3. Verificar senha com user.check_password()
    #   4. Verificar is_active
    #   5. Chamar login_user(user, remember=form.remember.data)
    #   6. Redirecionar para next ou main.index

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    """Encerra a sessão do usuário."""
    # TODO: [BACKEND] Adicionar logging da ação de logout
    logout_user()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("main.index"))

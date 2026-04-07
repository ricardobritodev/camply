from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.blueprints.messages import messages_bp
from app.extensions import db
from app.models.message import Message
from app.forms.message_forms import MessageForm


@messages_bp.route("/")
@login_required
def inbox():
    """Caixa de entrada de mensagens."""
    # TODO: [BACKEND] Agrupar mensagens por conversa (sender/receiver pair)
    # TODO: [BACKEND] Marcar mensagens como lidas ao abrir
    messages = Message.query.filter_by(receiver_id=current_user.id).order_by(
        Message.created_at.desc()
    ).all()
    return render_template("messages/inbox.html", messages=messages)


@messages_bp.route("/send", methods=["POST"])
@login_required
def send_message():
    """Enviar mensagem para host ou guest."""
    form = MessageForm()

    # TODO: [BACKEND] Implementar envio de mensagem:
    #   1. Validar form
    #   2. Criar Message com sender_id=current_user.id
    #   3. (Opcional) Enviar notificação por e-mail ao destinatário
    #   4. Redirecionar para a thread da conversa

    flash("Mensagem enviada!", "success")
    return redirect(url_for("messages.inbox"))

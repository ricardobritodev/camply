from flask import redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.blueprints.reviews import reviews_bp
from app.extensions import db
from app.models.review import Review
from app.models.booking import Booking
from app.forms.review_forms import ReviewForm


@reviews_bp.route("/", methods=["POST"])
@login_required
def create_review():
    """Criar avaliação após check-out."""
    form = ReviewForm()

    # TODO: [BACKEND] Implementar criação de review:
    #   1. Validar form
    #   2. Buscar Booking pelo booking_id do form
    #   3. Verificar que booking.guest_id == current_user.id
    #   4. Verificar que booking.status == 'completed'
    #   5. Verificar que ainda não existe review para este booking
    #   6. Salvar Review — o event listener atualizará avg_rating automaticamente
    #   7. Redirecionar para a propriedade com flash de sucesso

    flash("Avaliação enviada com sucesso!", "success")
    return redirect(url_for("main.index"))

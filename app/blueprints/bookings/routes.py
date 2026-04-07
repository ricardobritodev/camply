from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.blueprints.bookings import bookings_bp
from app.extensions import db
from app.models.booking import Booking
from app.models.property import Property
from app.forms.booking_forms import BookingForm


@bookings_bp.route("/", methods=["POST"])
@login_required
def create_booking():
    """Criar nova reserva."""
    form = BookingForm()

    # TODO: [BACKEND] Implementar criação de reserva:
    #   1. Validar form
    #   2. Buscar Property
    #   3. Verificar que current_user não é o dono
    #   4. Verificar disponibilidade (sem sobreposição de datas)
    #   5. Calcular nights, subtotal, cleaning_fee, service_fee, total_price
    #   6. Validar guests_count <= property.max_guests
    #   7. Validar nights entre min_nights e max_nights
    #   8. Salvar Booking com status='pending'
    #   9. Criar Payment associado
    #   10. Redirecionar para página de confirmação/pagamento

    flash("Reserva criada com sucesso! Aguardando confirmação.", "success")
    return redirect(url_for("bookings.my_bookings"))


@bookings_bp.route("/me")
@login_required
def my_bookings():
    """Lista as reservas do usuário logado."""
    # TODO: [BACKEND] Implementar paginação
    # TODO: [BACKEND] Filtrar por status (request.args.get('status'))
    bookings = Booking.query.filter_by(guest_id=current_user.id).order_by(
        Booking.created_at.desc()
    ).all()
    return render_template("bookings/my_bookings.html", bookings=bookings)


@bookings_bp.route("/<int:booking_id>/cancel", methods=["POST"])
@login_required
def cancel_booking(booking_id: int):
    """Cancelar uma reserva."""
    booking = Booking.query.get_or_404(booking_id)

    # Apenas o guest ou admin pode cancelar
    if booking.guest_id != current_user.id and not current_user.is_admin:
        abort(403)

    # TODO: [BACKEND] Implementar política de cancelamento:
    #   - Verificar se status permite cancelamento ('pending' ou 'confirmed')
    #   - Registrar cancellation_reason e cancelled_at
    #   - Processar reembolso se aplicável
    #   - Atualizar payment.status para 'refunded'
    #   - Notificar o host por e-mail

    flash("Reserva cancelada.", "info")
    return redirect(url_for("bookings.my_bookings"))

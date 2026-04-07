from datetime import datetime, timezone
from app.extensions import db


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(
        db.Integer,
        db.ForeignKey("bookings.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    method = db.Column(
        db.Enum("pix", "credit_card", "boleto", name="payment_method"),
        nullable=False,
    )
    status = db.Column(
        db.Enum("pending", "paid", "failed", "refunded", name="payment_status"),
        nullable=False,
        default="pending",
    )
    transaction_id = db.Column(db.String(120), nullable=True)  # ID externo (gateway)
    paid_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )

    # Relações
    booking = db.relationship("Booking", back_populates="payment")

    # TODO: [BACKEND] Integrar com gateway de pagamento (Stripe, Asaas, Mercado Pago)
    # TODO: [BACKEND] Implementar webhook para atualizar status automaticamente

    def __repr__(self) -> str:
        return f"<Payment id={self.id} booking_id={self.booking_id} status={self.status}>"

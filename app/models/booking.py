from datetime import datetime, timezone
from app.extensions import db


class Booking(db.Model):
    __tablename__ = "bookings"

    # Índice composto para busca de disponibilidade
    __table_args__ = (
        db.Index("ix_bookings_availability", "property_id", "check_in", "check_out"),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_id = db.Column(
        db.Integer,
        db.ForeignKey("properties.id", ondelete="RESTRICT"),
        nullable=False,
    )
    guest_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )

    # Datas
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)  # TODO: [BACKEND] validar > check_in

    # Hóspedes e noites
    guests_count = db.Column(db.Integer, nullable=False)  # TODO: [BACKEND] validar <= property.max_guests
    nights = db.Column(db.Integer, nullable=False)        # TODO: [BACKEND] calcular automaticamente

    # Valores
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    cleaning_fee = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    service_fee = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)

    # Status
    status = db.Column(
        db.Enum(
            "pending",
            "confirmed",
            "cancelled",
            "completed",
            "refunded",
            name="booking_status",
        ),
        nullable=False,
        default="pending",
    )
    cancellation_reason = db.Column(db.Text, nullable=True)
    cancelled_at = db.Column(db.DateTime, nullable=True)

    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relações
    property = db.relationship("Property", back_populates="bookings")
    guest = db.relationship("User", back_populates="bookings", foreign_keys=[guest_id])
    payment = db.relationship(
        "Payment", back_populates="booking", uselist=False, cascade="all, delete-orphan"
    )
    review = db.relationship(
        "Review", back_populates="booking", uselist=False, cascade="all, delete-orphan"
    )

    # ------------------------------------------------------------------ #
    # Regras de negócio (TODO)
    # ------------------------------------------------------------------ #
    # TODO: [BACKEND] Implementar validação de sobreposição de datas:
    #   SELECT * FROM bookings WHERE property_id = X
    #   AND status IN ('pending', 'confirmed')
    #   AND NOT (check_out <= :new_check_in OR check_in >= :new_check_out)
    #
    # TODO: [BACKEND] Validar nights entre property.min_nights e property.max_nights
    # TODO: [BACKEND] Impedir que o dono da propriedade faça reserva nela

    def __repr__(self) -> str:
        return f"<Booking id={self.id} property_id={self.property_id} status={self.status}>"

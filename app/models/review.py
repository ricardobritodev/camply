from datetime import datetime, timezone
from sqlalchemy import event
from app.extensions import db


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(
        db.Integer,
        db.ForeignKey("bookings.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
    )
    property_id = db.Column(
        db.Integer,
        db.ForeignKey("properties.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    author_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )

    # Avaliações (1-5)
    rating = db.Column(db.Integer, nullable=False)               # Geral
    cleanliness_rating = db.Column(db.Integer, nullable=True)    # Limpeza
    location_rating = db.Column(db.Integer, nullable=True)       # Localização
    value_rating = db.Column(db.Integer, nullable=True)          # Custo-benefício

    comment = db.Column(db.Text, nullable=False)
    host_reply = db.Column(db.Text, nullable=True)  # Resposta do anfitrião

    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )

    # Relações
    booking = db.relationship("Booking", back_populates="review")
    property = db.relationship("Property", back_populates="reviews")
    author = db.relationship("User", back_populates="reviews")

    # TODO: [BACKEND] Validar rating entre 1 e 5 (CheckConstraint)
    # TODO: [BACKEND] Validar que booking.status == 'completed' antes de criar review
    # TODO: [BACKEND] Apenas o guest da reserva pode criar a review

    def __repr__(self) -> str:
        return f"<Review id={self.id} property_id={self.property_id} rating={self.rating}>"


# ------------------------------------------------------------------ #
# Hooks SQLAlchemy para manter avg_rating e reviews_count atualizados
# ------------------------------------------------------------------ #

@event.listens_for(Review, "after_insert")
def after_review_insert(mapper, connection, target):
    """Recalcula avg_rating e reviews_count após inserção de review."""
    # TODO: [BACKEND] Executar em background para não bloquear a request
    _schedule_property_stats_update(connection, target.property_id)


@event.listens_for(Review, "after_delete")
def after_review_delete(mapper, connection, target):
    """Recalcula avg_rating e reviews_count após remoção de review."""
    _schedule_property_stats_update(connection, target.property_id)


def _schedule_property_stats_update(connection, property_id: int) -> None:
    """Agenda atualização de estatísticas da propriedade ao final da transação."""
    from sqlalchemy import event as sa_event, text

    @sa_event.listens_for(connection, "after_commit", once=True)
    def _do_update(conn):
        conn.execute(
            text(
                """
                UPDATE properties SET
                    avg_rating   = COALESCE((SELECT AVG(rating) FROM reviews WHERE property_id = :pid), 0),
                    reviews_count = (SELECT COUNT(*) FROM reviews WHERE property_id = :pid)
                WHERE id = :pid
                """
            ),
            {"pid": property_id},
        )

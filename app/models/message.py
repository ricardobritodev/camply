from datetime import datetime, timezone
from app.extensions import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    receiver_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    property_id = db.Column(
        db.Integer,
        db.ForeignKey("properties.id", ondelete="SET NULL"),
        nullable=True,
    )
    booking_id = db.Column(
        db.Integer,
        db.ForeignKey("bookings.id", ondelete="SET NULL"),
        nullable=True,
    )
    content = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )

    # Relações
    sender = db.relationship("User", back_populates="sent_messages", foreign_keys=[sender_id])
    receiver = db.relationship("User", back_populates="received_messages", foreign_keys=[receiver_id])
    property = db.relationship("Property", back_populates="messages")

    # TODO: [BACKEND] Implementar agrupamento de mensagens por conversa (thread)
    # TODO: [BACKEND] Implementar notificação em tempo real (WebSockets ou polling)

    def __repr__(self) -> str:
        return f"<Message id={self.id} sender_id={self.sender_id} receiver_id={self.receiver_id}>"

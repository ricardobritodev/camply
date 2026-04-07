from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    cpf = db.Column(db.String(14), unique=True, nullable=True)
    avatar_url = db.Column(db.String(500), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    role = db.Column(
        db.Enum("admin", "host", "guest", name="user_role"),
        nullable=False,
        default="guest",
    )
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    email_verified = db.Column(db.Boolean, default=False, nullable=False)
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
    properties = db.relationship(
        "Property", back_populates="owner", cascade="all, delete-orphan"
    )
    bookings = db.relationship(
        "Booking", back_populates="guest", foreign_keys="Booking.guest_id"
    )
    reviews = db.relationship("Review", back_populates="author")
    favorites = db.relationship(
        "Favorite", back_populates="user", cascade="all, delete-orphan"
    )
    sent_messages = db.relationship(
        "Message", back_populates="sender", foreign_keys="Message.sender_id"
    )
    received_messages = db.relationship(
        "Message", back_populates="receiver", foreign_keys="Message.receiver_id"
    )

    # ------------------------------------------------------------------ #
    # Métodos de senha
    # ------------------------------------------------------------------ #
    def set_password(self, password: str) -> None:
        """Gera hash seguro da senha e armazena."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Verifica se a senha fornecida corresponde ao hash armazenado."""
        return check_password_hash(self.password_hash, password)

    # ------------------------------------------------------------------ #
    # Properties auxiliares
    # ------------------------------------------------------------------ #
    @property
    def is_admin(self) -> bool:
        return self.role == "admin"

    @property
    def is_host(self) -> bool:
        return self.role in ("admin", "host")

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email} role={self.role}>"

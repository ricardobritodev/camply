from datetime import datetime, timezone
from app.extensions import db


class Favorite(db.Model):
    __tablename__ = "favorites"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    property_id = db.Column(
        db.Integer,
        db.ForeignKey("properties.id", ondelete="CASCADE"),
        primary_key=True,
    )
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )

    # Relações
    user = db.relationship("User", back_populates="favorites")
    property = db.relationship("Property", back_populates="favorites")

    def __repr__(self) -> str:
        return f"<Favorite user_id={self.user_id} property_id={self.property_id}>"

from app.extensions import db

# Tabela associativa N:N entre Property e Amenity
property_amenities = db.Table(
    "property_amenities",
    db.Column(
        "property_id",
        db.Integer,
        db.ForeignKey("properties.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "amenity_id",
        db.Integer,
        db.ForeignKey("amenities.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Amenity(db.Model):
    __tablename__ = "amenities"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    icon = db.Column(db.String(80), nullable=True)  # ex: "wifi", "pool"
    category = db.Column(
        db.Enum("basico", "lazer", "seguranca", "externo", name="amenity_category"),
        nullable=False,
        default="basico",
    )

    # Relação reversa (opcional, útil para queries)
    properties = db.relationship(
        "Property", secondary=property_amenities, back_populates="amenities"
    )

    def __repr__(self) -> str:
        return f"<Amenity id={self.id} name={self.name}>"

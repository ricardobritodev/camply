from datetime import datetime, timezone, time
from app.extensions import db
from app.models.amenity import property_amenities


class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Informações básicas
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(180), unique=True, index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    property_type = db.Column(
        db.Enum(
            "sitio",
            "chacara",
            "casa_campo",
            "casa_veraneio",
            "fazenda",
            "pousada",
            name="property_type_enum",
        ),
        nullable=False,
    )

    # Endereço
    cep = db.Column(db.String(9), nullable=True)
    street = db.Column(db.String(200), nullable=True)
    number = db.Column(db.String(20), nullable=True)
    neighborhood = db.Column(db.String(120), nullable=True)
    city = db.Column(db.String(120), nullable=False, index=True)
    state = db.Column(db.String(2), nullable=False, index=True)
    country = db.Column(db.String(60), nullable=False, default="Brasil")
    latitude = db.Column(db.Numeric(10, 7), nullable=True)
    longitude = db.Column(db.Numeric(10, 7), nullable=True)

    # Preços
    price_per_night = db.Column(db.Numeric(10, 2), nullable=False)
    cleaning_fee = db.Column(db.Numeric(10, 2), nullable=False, default=0)

    # Capacidade
    max_guests = db.Column(db.Integer, nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False, default=1)
    beds = db.Column(db.Integer, nullable=False, default=1)
    bathrooms = db.Column(db.Integer, nullable=False, default=1)
    area_m2 = db.Column(db.Integer, nullable=True)

    # Regras de estadia
    min_nights = db.Column(db.Integer, nullable=False, default=1)
    max_nights = db.Column(db.Integer, nullable=False, default=30)
    check_in_time = db.Column(db.Time, nullable=False, default=time(14, 0))
    check_out_time = db.Column(db.Time, nullable=False, default=time(12, 0))
    rules = db.Column(db.Text, nullable=True)

    # Status e métricas
    status = db.Column(
        db.Enum("draft", "published", "suspended", name="property_status"),
        nullable=False,
        default="draft",
    )
    avg_rating = db.Column(db.Numeric(3, 2), nullable=False, default=0)
    reviews_count = db.Column(db.Integer, nullable=False, default=0)

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
    owner = db.relationship("User", back_populates="properties")
    images = db.relationship(
        "PropertyImage", back_populates="property", cascade="all, delete-orphan"
    )
    amenities = db.relationship(
        "Amenity", secondary=property_amenities, back_populates="properties"
    )
    bookings = db.relationship(
        "Booking", back_populates="property", cascade="all, delete-orphan"
    )
    reviews = db.relationship(
        "Review", back_populates="property", cascade="all, delete-orphan"
    )
    favorites = db.relationship(
        "Favorite", back_populates="property", cascade="all, delete-orphan"
    )
    messages = db.relationship("Message", back_populates="property")

    # ------------------------------------------------------------------ #
    # Helpers
    # ------------------------------------------------------------------ #
    @property
    def cover_image(self):
        """Retorna a imagem de capa ou a primeira imagem disponível."""
        cover = next((img for img in self.images if img.is_cover), None)
        return cover or (self.images[0] if self.images else None)

    @property
    def type_label(self) -> str:
        labels = {
            "sitio": "Sítio",
            "chacara": "Chácara",
            "casa_campo": "Casa de Campo",
            "casa_veraneio": "Casa de Veraneio",
            "fazenda": "Fazenda",
            "pousada": "Pousada",
        }
        return labels.get(self.property_type, self.property_type)

    def __repr__(self) -> str:
        return f"<Property id={self.id} slug={self.slug}>"

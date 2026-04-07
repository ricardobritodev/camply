# Exporta todos os models para que o Flask-Migrate os detecte corretamente
from app.models.user import User
from app.models.amenity import Amenity, property_amenities
from app.models.property import Property
from app.models.property_image import PropertyImage
from app.models.booking import Booking
from app.models.payment import Payment
from app.models.review import Review
from app.models.favorite import Favorite
from app.models.message import Message

__all__ = [
    "User",
    "Amenity",
    "property_amenities",
    "Property",
    "PropertyImage",
    "Booking",
    "Payment",
    "Review",
    "Favorite",
    "Message",
]

"""
Seed script — popula o banco com dados de desenvolvimento.

Uso:
    flask seed            # popula (ignora se já existir)
    flask seed --reset    # apaga tudo e repopula
"""
import random
from datetime import date, timedelta


AMENITIES_DATA = [
    ("Wi-Fi", "wifi", "basico"),
    ("Piscina", "pool", "lazer"),
    ("Churrasqueira", "bbq", "lazer"),
    ("Lareira", "fireplace", "basico"),
    ("Ar-condicionado", "ac", "basico"),
    ("Estacionamento", "parking", "basico"),
    ("Pet friendly", "pet", "basico"),
    ("Vista para montanha", "mountain", "externo"),
    ("Lago / Rio", "lake", "externo"),
    ("Cozinha equipada", "kitchen", "basico"),
    ("Trilhas", "trail", "externo"),
    ("Campo de futebol", "soccer", "lazer"),
    ("Playground", "playground", "lazer"),
    ("Câmeras de segurança", "camera", "seguranca"),
]

PROPERTIES_DATA = [
    {
        "title": "Sítio Água Viva",
        "property_type": "sitio",
        "city": "Atibaia",
        "state": "SP",
        "description": "Lindo sítio com piscina, churrasqueira e vista para as montanhas da Serra da Mantiqueira. Ideal para famílias e grupos.",
        "price_per_night": 350.00,
        "cleaning_fee": 150.00,
        "max_guests": 12,
        "bedrooms": 4,
        "beds": 6,
        "bathrooms": 3,
        "area_m2": 5000,
        "min_nights": 2,
        "images": [
            ("https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?w=800&q=80", True),
            ("https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=800&q=80", False),
        ],
        "amenities": ["Wi-Fi", "Piscina", "Churrasqueira", "Estacionamento", "Pet friendly", "Vista para montanha"],
    },
    {
        "title": "Chácara das Pedras",
        "property_type": "chacara",
        "city": "Campos do Jordão",
        "state": "SP",
        "description": "Chácara rústica com lareira, trilhas particulares e muito conforto para curtir as baixas temperaturas de Campos do Jordão.",
        "price_per_night": 480.00,
        "cleaning_fee": 200.00,
        "max_guests": 8,
        "bedrooms": 3,
        "beds": 4,
        "bathrooms": 2,
        "area_m2": 3000,
        "min_nights": 2,
        "images": [
            ("https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800&q=80", True),
        ],
        "amenities": ["Wi-Fi", "Lareira", "Churrasqueira", "Trilhas", "Cozinha equipada", "Estacionamento"],
    },
    {
        "title": "Fazenda Horizonte Verde",
        "property_type": "fazenda",
        "city": "Pirenópolis",
        "state": "GO",
        "description": "Fazenda histórica no coração de Goiás, com cavalgada, piscina natural, tirolesa e muito mais. Uma experiência autêntica do interior.",
        "price_per_night": 620.00,
        "cleaning_fee": 300.00,
        "max_guests": 20,
        "bedrooms": 6,
        "beds": 10,
        "bathrooms": 4,
        "area_m2": 50000,
        "min_nights": 3,
        "images": [
            ("https://images.unsplash.com/photo-1587061949409-02df41d5e562?w=800&q=80", True),
        ],
        "amenities": ["Piscina", "Churrasqueira", "Lago / Rio", "Trilhas", "Campo de futebol", "Playground", "Câmeras de segurança"],
    },
    {
        "title": "Casa de Campo Bela Vista",
        "property_type": "casa_campo",
        "city": "Nova Friburgo",
        "state": "RJ",
        "description": "Casa aconchegante com jardim florido, lareira e vista deslumbrante para o vale. Perfeita para casais e pequenas famílias.",
        "price_per_night": 390.00,
        "cleaning_fee": 120.00,
        "max_guests": 6,
        "bedrooms": 2,
        "beds": 3,
        "bathrooms": 2,
        "area_m2": 1500,
        "min_nights": 2,
        "images": [
            ("https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800&q=80", True),
        ],
        "amenities": ["Wi-Fi", "Lareira", "Vista para montanha", "Cozinha equipada", "Estacionamento"],
    },
    {
        "title": "Sítio Recanto Verde",
        "property_type": "sitio",
        "city": "Ibiúna",
        "state": "SP",
        "description": "Sítio tranquilo em meio à natureza com pomar, horta orgânica e lago para pesca. O refúgio perfeito para desconectar.",
        "price_per_night": 290.00,
        "cleaning_fee": 100.00,
        "max_guests": 10,
        "bedrooms": 3,
        "beds": 5,
        "bathrooms": 2,
        "area_m2": 8000,
        "min_nights": 1,
        "images": [
            ("https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800&q=80", True),
        ],
        "amenities": ["Lago / Rio", "Churrasqueira", "Pet friendly", "Estacionamento", "Cozinha equipada"],
    },
    {
        "title": "Pousada Serra Azul",
        "property_type": "pousada",
        "city": "Visconde de Mauá",
        "state": "RJ",
        "description": "Pousada boutique com chalés independentes, café da manhã incluído e acesso exclusivo ao rio Preto. Romântica e sofisticada.",
        "price_per_night": 530.00,
        "cleaning_fee": 0.00,
        "max_guests": 4,
        "bedrooms": 1,
        "beds": 2,
        "bathrooms": 1,
        "area_m2": 80,
        "min_nights": 2,
        "images": [
            ("https://images.unsplash.com/photo-1575517111839-3a3843ee7f5d?w=800&q=80", True),
        ],
        "amenities": ["Wi-Fi", "Lago / Rio", "Trilhas", "Cozinha equipada", "Ar-condicionado"],
    },
    {
        "title": "Chácara Boa Esperança",
        "property_type": "chacara",
        "city": "Socorro",
        "state": "SP",
        "description": "Chácara espaçosa com quadra poliesportiva, piscina aquecida, salão de festas e área kids. Ideal para eventos e reuniões.",
        "price_per_night": 420.00,
        "cleaning_fee": 180.00,
        "max_guests": 15,
        "bedrooms": 4,
        "beds": 7,
        "bathrooms": 3,
        "area_m2": 4000,
        "min_nights": 2,
        "images": [
            ("https://images.unsplash.com/photo-1510798831971-661eb04b3739?w=800&q=80", True),
        ],
        "amenities": ["Piscina", "Churrasqueira", "Campo de futebol", "Playground", "Câmeras de segurança", "Wi-Fi", "Estacionamento"],
    },
    {
        "title": "Casa de Veraneio Litoral",
        "property_type": "casa_veraneio",
        "city": "Ubatuba",
        "state": "SP",
        "description": "Casa à beira-mar com acesso direto à praia, deck com hammock e vista para o oceano. Veraneio perfeito no litoral norte paulista.",
        "price_per_night": 700.00,
        "cleaning_fee": 250.00,
        "max_guests": 10,
        "bedrooms": 3,
        "beds": 5,
        "bathrooms": 2,
        "area_m2": 200,
        "min_nights": 3,
        "images": [
            ("https://images.unsplash.com/photo-1505577058444-a3dab90d4253?w=800&q=80", True),
        ],
        "amenities": ["Wi-Fi", "Ar-condicionado", "Cozinha equipada", "Estacionamento", "Pet friendly"],
    },
]


def _slugify(text: str) -> str:
    """Converte texto em slug URL-amigável."""
    import re
    import unicodedata
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text).strip("-")


def run_seed(reset: bool = False) -> None:
    from flask import current_app
    from app.extensions import db
    from app.models.user import User
    from app.models.amenity import Amenity
    from app.models.property import Property
    from app.models.property_image import PropertyImage
    from app.models.booking import Booking
    from app.models.review import Review

    with current_app.app_context():
        if reset:
            print("⚠️  Apagando dados existentes...")
            db.drop_all()
            db.create_all()
            print("✅ Tabelas recriadas.")

        # ------------------------------------------------------------------ #
        # 1. Admin
        # ------------------------------------------------------------------ #
        if not User.query.filter_by(email="admin@camply.com").first():
            admin = User(name="Administrador Camply", email="admin@camply.com", role="admin", email_verified=True)
            admin.set_password("admin123")
            db.session.add(admin)
            print("✅ Admin criado: admin@camply.com / admin123")

        # ------------------------------------------------------------------ #
        # 2. Hosts
        # ------------------------------------------------------------------ #
        hosts_data = [
            ("Carlos Mendonça", "carlos@host.com", "11999990001"),
            ("Fernanda Lima", "fernanda@host.com", "11999990002"),
            ("Roberto Alves", "roberto@host.com", "11999990003"),
        ]
        hosts = []
        for name, email, phone in hosts_data:
            user = User.query.filter_by(email=email).first()
            if not user:
                user = User(name=name, email=email, role="host", phone=phone, email_verified=True)
                user.set_password("host123")
                db.session.add(user)
            hosts.append(user)
        db.session.flush()
        print(f"✅ {len(hosts_data)} hosts criados.")

        # ------------------------------------------------------------------ #
        # 3. Guests
        # ------------------------------------------------------------------ #
        guests_data = [
            ("Ana Souza", "ana@guest.com"),
            ("Pedro Costa", "pedro@guest.com"),
            ("Julia Martins", "julia@guest.com"),
            ("Lucas Ferreira", "lucas@guest.com"),
            ("Mariana Santos", "mariana@guest.com"),
        ]
        guests = []
        for name, email in guests_data:
            user = User.query.filter_by(email=email).first()
            if not user:
                user = User(name=name, email=email, role="guest", email_verified=True)
                user.set_password("guest123")
                db.session.add(user)
            guests.append(user)
        db.session.flush()
        print(f"✅ {len(guests_data)} guests criados.")

        # ------------------------------------------------------------------ #
        # 4. Amenities
        # ------------------------------------------------------------------ #
        amenity_map = {}
        for name, icon, category in AMENITIES_DATA:
            amenity = Amenity.query.filter_by(name=name).first()
            if not amenity:
                amenity = Amenity(name=name, icon=icon, category=category)
                db.session.add(amenity)
            amenity_map[name] = amenity
        db.session.flush()
        print(f"✅ {len(AMENITIES_DATA)} amenities criadas.")

        # ------------------------------------------------------------------ #
        # 5. Propriedades
        # ------------------------------------------------------------------ #
        created_properties = []
        for i, pdata in enumerate(PROPERTIES_DATA):
            slug = _slugify(pdata["title"])
            prop = Property.query.filter_by(slug=slug).first()
            if not prop:
                owner = hosts[i % len(hosts)]
                prop = Property(
                    owner_id=owner.id,
                    title=pdata["title"],
                    slug=slug,
                    description=pdata["description"],
                    property_type=pdata["property_type"],
                    city=pdata["city"],
                    state=pdata["state"],
                    price_per_night=pdata["price_per_night"],
                    cleaning_fee=pdata["cleaning_fee"],
                    max_guests=pdata["max_guests"],
                    bedrooms=pdata["bedrooms"],
                    beds=pdata["beds"],
                    bathrooms=pdata["bathrooms"],
                    area_m2=pdata.get("area_m2"),
                    min_nights=pdata.get("min_nights", 1),
                    status="published",
                )

                # Imagens
                for j, (url, is_cover) in enumerate(pdata["images"]):
                    prop.images.append(PropertyImage(url=url, is_cover=is_cover, position=j))

                # Comodidades
                for amenity_name in pdata["amenities"]:
                    if amenity_name in amenity_map:
                        prop.amenities.append(amenity_map[amenity_name])

                db.session.add(prop)
            created_properties.append(prop)

        db.session.flush()
        print(f"✅ {len(PROPERTIES_DATA)} propriedades criadas.")

        # ------------------------------------------------------------------ #
        # 6. Reservas e avaliações de exemplo
        # ------------------------------------------------------------------ #
        from app.models.payment import Payment

        sample_bookings = [
            (created_properties[0], guests[0], date.today() - timedelta(days=30), date.today() - timedelta(days=27), 2, "completed"),
            (created_properties[1], guests[1], date.today() - timedelta(days=20), date.today() - timedelta(days=17), 3, "completed"),
            (created_properties[2], guests[2], date.today() + timedelta(days=10), date.today() + timedelta(days=14), 4, "confirmed"),
            (created_properties[0], guests[3], date.today() + timedelta(days=20), date.today() + timedelta(days=22), 2, "pending"),
        ]

        for prop, guest, check_in, check_out, guests_count, status in sample_bookings:
            existing = Booking.query.filter_by(property_id=prop.id, guest_id=guest.id, check_in=check_in).first()
            if existing:
                continue

            nights = (check_out - check_in).days
            subtotal = float(prop.price_per_night) * nights
            cleaning = float(prop.cleaning_fee)
            service = round(subtotal * 0.10, 2)
            total = subtotal + cleaning + service

            booking = Booking(
                property_id=prop.id,
                guest_id=guest.id,
                check_in=check_in,
                check_out=check_out,
                guests_count=guests_count,
                nights=nights,
                subtotal=subtotal,
                cleaning_fee=cleaning,
                service_fee=service,
                total_price=total,
                status=status,
            )
            db.session.add(booking)
            db.session.flush()

            # Payment
            payment = Payment(
                booking_id=booking.id,
                amount=total,
                method="pix",
                status="paid" if status in ("completed", "confirmed") else "pending",
            )
            db.session.add(payment)

            # Review para completed
            if status == "completed":
                review = Review(
                    booking_id=booking.id,
                    property_id=prop.id,
                    author_id=guest.id,
                    rating=random.randint(4, 5),
                    cleanliness_rating=random.randint(4, 5),
                    location_rating=random.randint(4, 5),
                    value_rating=random.randint(3, 5),
                    comment="Lugar incrível! Superou todas as expectativas. Com certeza voltarei em breve.",
                )
                db.session.add(review)

        db.session.commit()
        print("✅ Reservas e avaliações de exemplo criadas.")
        print("\n🌱 Seed concluído com sucesso!")
        print("   Acesse: http://localhost:5000")
        print("   Admin:  admin@camply.com / admin123")
        print("   Host:   carlos@host.com / host123")
        print("   Guest:  ana@guest.com / guest123")

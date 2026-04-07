from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SelectField, IntegerField,
    DecimalField, SubmitField, MultipleFileField, TimeField
)
from wtforms.validators import DataRequired, Length, NumberRange, Optional


PROPERTY_TYPE_CHOICES = [
    ("sitio", "Sítio"),
    ("chacara", "Chácara"),
    ("casa_campo", "Casa de Campo"),
    ("casa_veraneio", "Casa de Veraneio"),
    ("fazenda", "Fazenda"),
    ("pousada", "Pousada"),
]

STATE_CHOICES = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"), ("GO", "Goiás"), ("MA", "Maranhão"),
    ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"),
    ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"),
    ("SC", "Santa Catarina"), ("SP", "São Paulo"), ("SE", "Sergipe"),
    ("TO", "Tocantins"),
]


class PropertyForm(FlaskForm):
    # Informações básicas
    title = StringField(
        "Título",
        validators=[DataRequired(), Length(min=10, max=150)],
    )
    description = TextAreaField(
        "Descrição",
        validators=[DataRequired(), Length(min=50)],
    )
    property_type = SelectField(
        "Tipo de propriedade",
        choices=PROPERTY_TYPE_CHOICES,
        validators=[DataRequired()],
    )

    # Localização
    cep = StringField("CEP", validators=[Optional(), Length(max=9)])
    street = StringField("Rua/Endereço", validators=[Optional(), Length(max=200)])
    number = StringField("Número", validators=[Optional(), Length(max=20)])
    neighborhood = StringField("Bairro", validators=[Optional(), Length(max=120)])
    city = StringField("Cidade", validators=[DataRequired(), Length(max=120)])
    state = SelectField("Estado", choices=STATE_CHOICES, validators=[DataRequired()])

    # Preços
    price_per_night = DecimalField(
        "Preço por noite (R$)",
        validators=[DataRequired(), NumberRange(min=0)],
        places=2,
    )
    cleaning_fee = DecimalField(
        "Taxa de limpeza (R$)",
        validators=[Optional(), NumberRange(min=0)],
        places=2,
        default=0,
    )

    # Capacidade
    max_guests = IntegerField(
        "Máximo de hóspedes",
        validators=[DataRequired(), NumberRange(min=1)],
    )
    bedrooms = IntegerField("Quartos", validators=[Optional(), NumberRange(min=0)], default=1)
    beds = IntegerField("Camas", validators=[Optional(), NumberRange(min=0)], default=1)
    bathrooms = IntegerField("Banheiros", validators=[Optional(), NumberRange(min=0)], default=1)
    area_m2 = IntegerField("Área (m²)", validators=[Optional(), NumberRange(min=1)])

    # Regras
    min_nights = IntegerField("Mínimo de noites", validators=[Optional(), NumberRange(min=1)], default=1)
    max_nights = IntegerField("Máximo de noites", validators=[Optional(), NumberRange(min=1)], default=30)
    rules = TextAreaField("Regras da propriedade", validators=[Optional()])

    # TODO: [FRONTEND] Adicionar campo de upload de imagens com preview
    # TODO: [BACKEND] Implementar upload para storage (S3, Cloudinary, etc.)
    # TODO: [FRONTEND] Adicionar seleção de comodidades (checkboxes dinâmicos)
    # TODO: [BACKEND] Validar que min_nights <= max_nights

    submit = SubmitField("Salvar propriedade")

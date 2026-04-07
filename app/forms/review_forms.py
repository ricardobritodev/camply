from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional


class ReviewForm(FlaskForm):
    booking_id = HiddenField("booking_id", validators=[DataRequired()])
    rating = IntegerField(
        "Avaliação geral (1-5)",
        validators=[DataRequired(), NumberRange(min=1, max=5)],
    )
    cleanliness_rating = IntegerField(
        "Limpeza (1-5)",
        validators=[Optional(), NumberRange(min=1, max=5)],
    )
    location_rating = IntegerField(
        "Localização (1-5)",
        validators=[Optional(), NumberRange(min=1, max=5)],
    )
    value_rating = IntegerField(
        "Custo-benefício (1-5)",
        validators=[Optional(), NumberRange(min=1, max=5)],
    )
    comment = TextAreaField(
        "Comentário",
        validators=[DataRequired()],
    )
    submit = SubmitField("Enviar avaliação")

    # TODO: [FRONTEND] Implementar seleção de estrelas com Alpine.js

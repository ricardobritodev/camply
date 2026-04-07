from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField, DateField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class BookingForm(FlaskForm):
    property_id = HiddenField("property_id", validators=[DataRequired()])
    check_in = DateField("Check-in", validators=[DataRequired()])
    check_out = DateField("Check-out", validators=[DataRequired()])
    guests_count = IntegerField(
        "Número de hóspedes",
        validators=[DataRequired(), NumberRange(min=1)],
    )
    submit = SubmitField("Reservar")

    # TODO: [BACKEND] Validar que check_out > check_in
    # TODO: [BACKEND] Validar disponibilidade das datas
    # TODO: [BACKEND] Validar guests_count <= property.max_guests

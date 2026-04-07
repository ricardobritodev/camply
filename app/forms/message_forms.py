from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    receiver_id = HiddenField("receiver_id", validators=[DataRequired()])
    property_id = HiddenField("property_id")
    booking_id = HiddenField("booking_id")
    content = TextAreaField(
        "Mensagem",
        validators=[DataRequired()],
    )
    submit = SubmitField("Enviar")

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email


class WithdrawalForm ( FlaskForm ) :
    amount = StringField ( "Amount to Withdraw:", validators=[DataRequired ()] )
    submit = SubmitField ( "Submit" )

class DepositForm ( FlaskForm ) :
    amount = StringField ( "Amount to Deposit:", validators=[DataRequired ()] )
    submit = SubmitField ( "Submit" )

class EnterPINForm ( FlaskForm ) :
    pin = StringField ( "Enter PIN:", validators=[DataRequired ()] )
    submit = SubmitField ( "Submit" )





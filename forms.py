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

class AEWorkOrderForm ( FlaskForm ) :
    potHoleID = IntegerField ( "Pothole ID:", validators=[DataRequired ()] )
    repairCrewID = IntegerField ( "Repair Crew ID:", validators=[DataRequired ()] )
    numberOfWorkers = IntegerField ( "Number of Workers:", validators=[DataRequired ()] )
    equipmentAssigned = TextAreaField ( "Equipment Assigned:", validators=[DataRequired ()] )
    hoursApplied = IntegerField ( "Hours Applied:", validators=[DataRequired ()] )
    holeStatus = StringField ( "Hole Status:", validators=[DataRequired ()] )
    fillerMaterial = IntegerField ( "Filler Material Used:", validators=[DataRequired ()] )
    submit = SubmitField ( "Submit" )



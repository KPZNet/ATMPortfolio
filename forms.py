from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email


class AEPotHoleForm ( FlaskForm ) :
    streetAddress = StringField ( "Street:", validators=[DataRequired ()] )
    location = StringField ( "Pothole Location:", validators=[DataRequired ()] )
    size = IntegerField ( "Size 1-10:", validators=[DataRequired ()] )
    severity = StringField ( "Severity:", validators=[DataRequired ()] )
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

class AEDamageClaimForm ( FlaskForm ) :
    potHoleID = StringField ( "Pothole ID:", validators=[DataRequired ()] )
    name = StringField ( "Name:", validators=[DataRequired ()] )
    address = StringField ( "Address:", validators=[DataRequired ()] )
    phone = StringField ( "Phone:", validators=[DataRequired ()] )
    damageType = StringField ( "Damage Description:", validators=[DataRequired ()] )
    dollarAmount = StringField ( "Claim Amount:", validators=[DataRequired ()] )
    approved = BooleanField ( "Approval Status:" )
    submit = SubmitField ( "Submit" )

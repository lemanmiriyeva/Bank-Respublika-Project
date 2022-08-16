from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SelectField, RadioField, DateField, EmailField
from model import SeriyaHeading,NumberPrefix,OrderType,Filiallar
from wtforms.validators import DataRequired, Length, Email

class Card_order(FlaskForm):
    card = SelectField(label='Kartı əlavə et', choices=[('NeoKart Standard', 'NeoKart Standard'), ('NeoKart Premium', 'NeoKart Premium'), ('Mover Visa Platinium', 'Mover Visa Platinium'), ('Mover Visa Classic','Mover Visa Classic'), ('MasterCard Debet','MasterCard Debet'), ('MasterCard Platinum - Cümhuriyyət 100 il.','MasterCard Platinum - Cümhuriyyət 100 il.'), ('Visa Virtual','Visa Virtual'), ('VISA Gold','VISA Gold'), ('MasterCard Gold','MasterCard Gold'), ('VISA Classic','VISA Classic'), ('MasterCard Standard','MasterCard Standard')])
    currency = SelectField(label='Kartın valyutasını seç', choices=[('AZN', 'AZN'), ('ABS dollari', 'ABŞ dolları'), ('Avro', 'Avro')])
    name = StringField(label = 'Adınız', validators=[DataRequired(), Length(min=3, max=30)])
    surname = StringField(label = 'Soyadınız', validators=[DataRequired(), Length(min=3, max=30)])
    father_name = StringField(label = 'Ata adınız', validators=[DataRequired(), Length(min=3, max=30)])
    birthday = DateField(label = 'Doğum tarixi', format='%Y-%m-%d',validators=[DataRequired()])
    phone_number = StringField(label = 'Mobil nömrəniz', validators=[DataRequired(), Length(max=13)])
    address = StringField(label = 'Qeydiyyat ünvanınız', validators=[DataRequired()])
    email = EmailField(label = 'Email', validators=[DataRequired(), Email(), Length(max=35)])

class CardRenewForm(FlaskForm):
    card_number = IntegerField(label='Kartın son 8 rəqəmi:', validators=[DataRequired()])
    seriya_head = SelectField(u'Şəxsiyyəti təsdiq edən sənəd:', choices= [(seriya_head.id, seriya_head.seriya_head) for seriya_head in SeriyaHeading.query.all()],validators=[DataRequired()])
    seriya_number = IntegerField(label='', validators=[DataRequired()])    
    number_prefix = SelectField(label='Mobil nömrəniz',choices=[(prefix.id, prefix.title) for prefix in NumberPrefix.query.all()],validators=[DataRequired()])
    phone_number = IntegerField(label='', validators=[DataRequired()])
    order_type = RadioField(label='Sifariş növü', validators=[DataRequired()],choices= [(type.id, type.order_type) for type in OrderType.query.all()])
    filial = SelectField(u'Kart götürüləcək filial',validators=[DataRequired()], choices= [(filial.id, filial.title) for filial in Filiallar.query.all()] )
    security_code = StringField(label='security_code',validators=[])
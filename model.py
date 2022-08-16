from extensions import db , admin
from datetime import datetime
from admin import NewsAdmin, ProductCategoryAdmin, ProductsAdmin,FiliallarAdmin, SeriyaHeadingAdmin,CardreNewAdmin, NumberPrefixAdmin,OrderTypeAdmin, CardsAdmin, Card_order_modelAdmin


class News(db.Model):
    __tablename__ = "News"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable = False)
    slug = db.Column(db.Text, nullable = False)
    small_desc = db.Column(db.String(255), nullable = False)
    large_desc = db.Column(db.Text, nullable = False)
    img_url = db.Column(db.Text, nullable = False)
    kampaniya_desc = db.Column(db.Text, nullable = True)
    created_at =  db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at =  db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title, small_desc,large_desc, img_url, kampaniya_desc, slug):
        self.title = title 
        self.small_desc = small_desc
        self.large_desc = large_desc
        self.img_url = img_url
        self.kampaniya_desc = kampaniya_desc
        self.slug = slug

    def save(self):
        db.session.add(self)
        db.session.commit()


class ProductCategory(db.Model):
    __tablename__ = "ProductCategory"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable = False)
    created_at =  db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at =  db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title):
        self.title = title 

    def save(self):
        db.session.add(self)
        db.session.commit()


class Products(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('ProductCategory.id'))
    desc = db.Column(db.Text, nullable = True)
    created_at =  db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at =  db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title, category_id,desc):
        self.title = title 
        self.category_id = category_id
        self.desc = desc

    def save(self):
        db.session.add(self)
        db.session.commit()





class Filiallar(db.Model):
    __tablename__ = "Filiallar"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable = False)
    created_at =  db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at =  db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title):
        self.title = title 

    def save(self):
        db.session.add(self)
        db.session.commit()



class SeriyaHeading(db.Model):
    __tablename__ = "SeriyaHeading"
    id = db.Column(db.Integer, primary_key=True)
    seriya_head = db.Column(db.String(3), nullable = False)
    created_at =  db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at =  db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.seriya_head}'

    def __init__(self, seriya_head):
        self.seriya_head = seriya_head 

    def save(self):
        db.session.add(self)
        db.session.commit()



class NumberPrefix(db.Model):
    __tablename__ = "NumberPrefix"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title):
        self.title = title 

    def save(self):
        db.session.add(self)
        db.session.commit()


class OrderType(db.Model):
    __tablename__ = "OrderType"
    id = db.Column(db.Integer, primary_key=True)
    order_type = db.Column(db.String(25), nullable = False )
    order_payment = db.Column(db.Integer, nullable = False )


class CardreNew(db.Model):
    __tablename__ = "CardreNew"
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.Integer, nullable = False)
    seriya_head_id = db.Column(db.Integer, db.ForeignKey('SeriyaHeading.id'))
    seriya_number = db.Column(db.Integer, nullable = False)
    number_prefix_id = db.Column(db.Integer, db.ForeignKey('NumberPrefix.id'))
    phone_number = db.Column(db.Integer, nullable = False)
    order_type_id = db.Column(db.Integer, db.ForeignKey('OrderType.id'))
    filial_id = db.Column(db.Integer, db.ForeignKey('Filiallar.id'))
    created_at =  db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at =  db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.card_number}'

    def __init__(self, card_number, seriya_head_id,seriya_number, number_prefix_id, phone_number, order_type_id, filial_id):
        self.card_number = card_number 
        self.seriya_head_id = seriya_head_id
        self.seriya_number = seriya_number
        self.number_prefix_id = number_prefix_id
        self.phone_number = phone_number
        self.order_type_id = order_type_id
        self.filial_id = filial_id

    def save(self):
        db.session.add(self)
        db.session.commit()




class Cards(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    description=db.Column(db.Text,nullable=True)
    details=db.Column(db.Text,nullable=False)
    img = db.Column(db.String(255))
    buraxilma=db.Column(db.String(255),default="Buraxılma haqqı")
    buraxilma_d=db.Column(db.String(255))
    istifade=db.Column(db.String(255),default="İstifadə müddəti")
    istifade_d=db.Column(db.String(255))
    faiz=db.Column(db.String(255),default="Qalıq üzrə faiz AZN")
    faiz_d=db.Column(db.String(255))
    valyuta=db.Column(db.String(255),default="Valyuta")
    valyuta_d=db.Column(db.String(255))
    kredit=db.Column(db.String(255),default="Kredit xətti")
    kredit_d=db.Column(db.String(255))
    filter = db.Column(db.String(255))
    
    def __repr__(self):
        return self.title


    def save(self):
        db.session.add(self)
        db.session.commit()
    
class Card_order_model(db.Model):
    __tablename__ = 'Card_order_model'
    id = db.Column(db.Integer, primary_key = True)
    card = db.Column(db.String(50))
    currency = db.Column(db.String(50))
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    father_name = db.Column(db.String(30))
    birthday = db.Column(db.Date)
    phone_number = db.Column(db.String(13))
    address = db.Column(db.String(255))
    email = db.Column(db.String(35))

    
    def __repr__(self):
        return self.name

    def __init__(self, card, currency, name, surname, father_name, birthday, phone_number, address, email):
        self.card = card
        self.currency = currency
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.birthday = birthday
        self.phone_number = phone_number
        self.address = address
        self.email = email


    def save(self):
        db.session.add(self)
        db.session.commit()



admin.add_view(NewsAdmin(News, db.session))
admin.add_view(ProductCategoryAdmin(ProductCategory, db.session))
admin.add_view(ProductsAdmin(Products, db.session))
admin.add_view(FiliallarAdmin(Filiallar, db.session))
admin.add_view(NumberPrefixAdmin(NumberPrefix, db.session))
admin.add_view(SeriyaHeadingAdmin(SeriyaHeading, db.session))
admin.add_view(OrderTypeAdmin(OrderType, db.session))
admin.add_view(CardreNewAdmin(CardreNew, db.session))
admin.add_view(CardsAdmin(Cards, db.session))
admin.add_view(Card_order_modelAdmin(Card_order_model, db.session))


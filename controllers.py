from flask import  render_template,request, flash, redirect, url_for
from app import app
from model import *
from form import *
import requests, xmltodict
from datetime import datetime


@app.route("/")
def homepage():
    news_ = News.query.all()
    pro_category_ = ProductCategory.query.all()
    products_ = Products.query.all()
    currency=requests.get(f'https://www.cbar.az/currencies/{datetime.now().strftime("%d.%m.%Y")}.xml')
    currency_list=xmltodict.parse(currency.content)
    return render_template('homepage.html',currency=currency_list, news = news_ , procategory = pro_category_ , products = products_ , show=False)




@app.route("/news")
def news_page():
    news_ = News.query.all()
    return render_template('news.html', news = news_ ,show=False)


@app.route("/kampaniyalar")
def company_page():
    kampaniyalar_ = News.query.all()
    return render_template('allcompanies.html', kampaniyalar = kampaniyalar_ ,show=False)

@app.route("/kampaniyalar/<slug>")
def company(slug):
   
    news__ = News.query.filter(News.slug == slug).first()
 
    return render_template('kampaniyalar_details.html', news_one = news__)
@app.route("/news/<slug>")
def dinamic(slug):
    
    news__ = News.query.filter(News.slug == slug).first()
    news_ = News.query.all()

    return render_template('news_details.html', news_one = news__, news=news_)
    


@app.route("/cardrenew", methods=["GET", "POST"])
def renew():
    form = CardRenewForm()
    if request.method == "POST": 
        post_data = request.form
       
        form = CardRenewForm(data = post_data)
        print(request.form,form.validate_on_submit())
        if form.validate():
            
            renewcard = CardreNew(card_number = form.card_number.data, seriya_head_id=form.seriya_head.data,  seriya_number = form.seriya_number.data,  number_prefix_id=form.number_prefix.data, phone_number = form.phone_number.data, order_type_id= form.order_type.data, filial_id=form.filial.data)
            renewcard.save()
            return redirect('/cardrenew')
        
    
    return render_template('cardrenew.html', form =form)
    
@app.route('/cards/')
def cards():
    card = Cards().query.all()
    return render_template('cards.html', cards = card)

@app.route('/cards/<int:id>')
def detail(id):
    card = Cards.query.filter(Cards.id==id).first()
    return render_template('cardDetail.html', card = card)

@app.route("/card_order/", methods=['GET', 'POST'])
def card_order():
    post_data = request.form
    form = Card_order()
    if request.method == 'POST':
        form=Card_order(data=post_data)
        if form.validate_on_submit():
            card_order = Card_order_model(card = form.card.data , currency = form.currency.data, name = form.name.data, surname = form.surname.data, father_name = form.father_name.data, birthday = form.birthday.data, phone_number = form.phone_number.data, address = form.address.data, email = form.email.data)
            card_order.save()
    return render_template('cardOrder.html', form = form)
  


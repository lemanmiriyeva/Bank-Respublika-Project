from ast import Mod
from flask_admin.contrib.sqla import ModelView

class NewsAdmin(ModelView):
    can_View_details = True
  

class ProductCategoryAdmin(ModelView):
    can_View_details = True
    
    
class ProductsAdmin(ModelView):
    can_View_details = True
    column_display_pk = True 
    column_hide_backrefs = False
    column_list = ('id', 'title', 'category_id','desc')

class FiliallarAdmin(ModelView):
    can_View_details = True

class NumberPrefixAdmin(ModelView):
    can_View_details = True


class SeriyaHeadingAdmin(ModelView):
    can_View_details = True

class CardreNewAdmin(ModelView):
    can_View_details = True
    column_display_pk = True 
    column_hide_backrefs = False
    column_list = ('id', 'card_number', 'seriya_head_id','seriya_number','number_prefix_id','phone_number','order_type_id','filial_id')

class OrderTypeAdmin(ModelView):
    can_View_details = True

class CardsAdmin(ModelView):
    can_View_details = True

class CardsAdmin(ModelView):
    can_View_details = True

class Card_order_modelAdmin(ModelView):
    can_view_details = True
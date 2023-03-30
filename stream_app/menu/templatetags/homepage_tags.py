from django import template
from menu.models import *

register=template.Library()

# @register.simple_tag()
# def get_menu():
#     return Menu.objects.all()


@register.inclusion_tag('show_menu.html')
def show_menu(sort=None,cat_selected=0):
    if not sort:
        menu=Menu.objects.all()
    else:
        menu=Menu.objects.order_by(sort)    
    
    return {"menu":menu, "cat_selected":cat_selected,}
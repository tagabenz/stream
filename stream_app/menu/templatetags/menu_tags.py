from django import template
from menu.models import *

register=template.Library()


@register.inclusion_tag('show_menu.html')
def show_menu(sort=None,request_path=None):
    if not sort:
        menu=Menu.objects.all()
    else:
        menu=Menu.objects.order_by(sort)    
    return {"menu":menu,'request_path':request_path}

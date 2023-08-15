from django import template

from menu.models import *


register=template.Library()

# Show menu Item in header
@register.inclusion_tag('show_menu.html')
def show_menu(sort,request):
    if not sort:
        menu=Menu.objects.all()
    else:
        menu=Menu.objects.order_by(sort)    
    return {"menu":menu,'request_path': request.get_full_path }


#Show categories in /categories.html
@register.inclusion_tag('show_cat.html')
def show_cat(request):
    categories=Categories.objects.all()  

    return {"cats":categories,'request_path': request.get_full_path}
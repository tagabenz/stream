from django import template
from homepage.models import *

register=template.Library()

@register.simple_tag()
def get_menu():
    return Menu.objects.all()


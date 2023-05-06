from django import template
from studio.models import *


register=template.Library()

@register.inclusion_tag('show_stream_info.html')
def show_stream_info(user):
    info=Stream.objects.filter(autor=user)
    
    return  {'info': info}
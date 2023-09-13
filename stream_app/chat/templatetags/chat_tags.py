from django import template
from stream_app import settings

register=template.Library()

# Centrifugo chat 
@register.inclusion_tag('chat.html')
def chat(user):
    
    return {'user':user}
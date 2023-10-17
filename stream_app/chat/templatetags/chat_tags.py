from django import template
from stream_app import settings

register=template.Library()

# Centrifugo chat 
@register.inclusion_tag('chat.html')
def chat(request):
    connect_url = settings.CENTRIFUGE_HOST
    
    if 'studio' in request.get_full_path():room_name = request.user.username
    else: room_name = request.get_full_path().strip('/')
    
    return {
        'room_name':room_name,
        'connect_url':connect_url
    }
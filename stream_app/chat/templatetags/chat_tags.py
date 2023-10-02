from django import template
from stream_app import settings

register=template.Library()

# Centrifugo chat 
@register.inclusion_tag('chat.html')
def studio_chat(user):
    # in studio.html/
    connect_url = settings.CENTRIFUGE_HOST
    room_name = user.username
    
    return {
        'room_name':room_name,
        'connect_url':connect_url
    }

@register.inclusion_tag('chat.html')
def user_chat(request):
    # in userpage.html
    connect_url = settings.CENTRIFUGE_HOST
    room_name = request.get_full_path()
    
    return {
        'room_name':room_name.strip('/'),
        'connect_url':connect_url
    }
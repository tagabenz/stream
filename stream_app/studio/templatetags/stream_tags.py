from django import template
from app_users.models import Users


register=template.Library()

# Show Stream parametrs by user in studio.html
@register.inclusion_tag('show_stream_info.html')
def show_stream_info(user):
        
    return  {'user':user}
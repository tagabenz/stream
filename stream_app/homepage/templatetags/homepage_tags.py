from django import template
from studio.models import Stream

register=template.Library()

# Show Stream status button in header when User is login
@register.inclusion_tag('studio_button.html')
def show_button(request):
    instance=Stream.objects.get(autor=request.user)
    
    return {'state': instance.is_online, 'request_path':request.get_full_path}
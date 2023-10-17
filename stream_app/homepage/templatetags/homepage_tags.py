from django import template
from app_users.models import Users

register=template.Library()

# Show Stream status button in header when User is login
@register.inclusion_tag('studio_button.html')
def show_button(request):
    instance=Users.objects.get(username=request.user)
    
    return {'request_path':request.get_full_path}


# Show Sidebar with subscriptions
@register.inclusion_tag('sidebar.html')
def sidebar(request):
    
    return {'request':request}

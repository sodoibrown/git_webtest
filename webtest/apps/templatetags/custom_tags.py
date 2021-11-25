from django import templatetags,template
from django.contrib.auth.models import Group
# from test.models import cuser

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group =  Group.objects.get(name=group_name)
    return group in user.groups.all()

# def test_tag():
#     user1 = cuser.objects.all()
#     return user1
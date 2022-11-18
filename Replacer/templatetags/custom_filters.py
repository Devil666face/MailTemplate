from django.template import Library
from Replacer.models import Template

register = Library()

@register.inclusion_tag('Replacer/include/_template_bar.html')
def show_template_bar(path):
    template_list = Template.objects.all()
    return {'template_list':template_list, 'path':path}

@register.simple_tag(name='forindex')
def forindex(list_obj, index):
    return list_obj[index]
from django import template
register = template.Library()
@register.filter(name='cutt')
def cutt(value):
    #this cuts out all value of arg
    return value.replace(' ','@')
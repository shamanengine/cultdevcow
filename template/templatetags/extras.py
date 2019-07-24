from django import template

register = template.Library()

@register.filter(name = 'inc')
def inc(value, arg):
    pass

@register.filter
def devision(value, arg1, arg2):
    pass

from django import template
import math
register = template.Library()


@register.filter(name='safe_divide')
def  safe_divide(value):
    return round(int(value)/12,2)
 
 
 
@register.filter(name='divide_by_10')
def  divide_by_10(value):
    return int(int(value)/10)
 
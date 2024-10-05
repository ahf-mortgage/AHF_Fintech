from django import template
from num2words import num2words
import math
register = template.Library()




@register.filter(name='sum_list')
def sum_list(numbers):
    return sum(numbers)

@register.filter(name='safe_divide')
def  safe_divide(value):
    return float(value)/12
 
 
 
@register.filter(name='divide_by_10')
def  divide_by_10(value):
    return round(float(value)/10,2)


 
@register.filter(name='mul')
def  mul(value1,value2):
    return value1*value2


@register.filter(name='div')
def  div(value1,value2):
    return float(value1)/float(value2)


@register.filter(name='minus')
def  div(value1,value2):
    return float(value1) - float(value2)


@register.filter(name='add')
def  add(value1,value2):
    return float(value1) + float(value2)

@register.filter(name='divide_by_12')
def  divide_by_12(value):
    return float(value)/12




@register.filter('multiply')
def multiply(value, arg):
    """
    Multiplies the value by the argument.
    
    """
    arg = float(arg) / 100
    return value * arg


@register.filter(name='dict_get')
def dict_get(dictionary, key):
    return dictionary.get(key)

@register.filter("split_word")
def split_words(value):
    return " ".join(value.split("_"))


@register.filter("num_word")
def num_word(value):
    word = num2words(value)
    return word
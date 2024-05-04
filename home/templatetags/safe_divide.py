from django import template
import math
register = template.Library()




@register.filter(name='sum_list')
def sum_list(numbers):
    return sum(numbers)

@register.filter(name='safe_divide')
def  safe_divide(value):
    return math.ceil(int(value)/12)
 
 
 
@register.filter(name='divide_by_10')
def  divide_by_10(value):
    return round(int(value)/10,2)


 
@register.filter(name='mul')
def  mul(value1,value2):
    return value1




@register.filter(name='divide_by_12')
def  divide_by_12(value):
    return round(int(value)/12,2)




@register.filter(name='dict_get')
def dict_get(dictionary, key):
    return dictionary.get(key)



@register.filter("split_word")
def split_words(value):
    return " ".join(value.split("_"))
  
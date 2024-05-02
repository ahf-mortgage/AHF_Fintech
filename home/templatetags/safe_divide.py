from django import template
import math
register = template.Library()


@register.filter(name='safe_divide')
def  safe_divide(value):
    return math.ceil(int(value)/12)
 
 
 
@register.filter(name='divide_by_10')
def  divide_by_10(value):
    return round(int(value)/10,2)



@register.filter(name='divide_by_12')
def  divide_by_12(value):
    return round(int(value)/12,2)




@register.filter(name='dict_get')
def dict_get(dictionary, key):
    return dictionary.get(key)



@register.filter("split_word")
def split_words(value):
    print("split words",value, " ".join(value.split("_")))
    return " ".join(value.split("_"))
  
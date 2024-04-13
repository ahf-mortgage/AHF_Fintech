from django import template
from crispy_forms.utils import render_crispy_form

register = template.Library()

@register.simple_tag(takes_context=True)
def crispy(context, form):
    return render_crispy_form(form, context=context)
from django import template

register = template.Library()

@register.assingment_tag
def valutes():
    salute = "hello"

    return salute
from django import template
register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    THIS CUTES ALL VALUES OF"ARG" from the string!

    """
    return value.replace(arg,'')

#register.filter('cut',cut)

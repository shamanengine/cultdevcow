from django import template
from functools import reduce

register = template.Library()

MOON_DICT = {'a': '@',
             'b': '|3',
             'c': '(',
             'd': '|)',
             'e': '3',
             'f': '£',
             'g': '[,',
             'h': '|~|',
             'i': '¡',
             'j': ")'",
             'k': '|{',
             'l': '1',
             'm': '/˅\\',
             'n': '|\|',
             'o': '0',
             'p': 'π',
             'q': '0',
             'r': '|?',
             's': '$',
             't': '†',  # 't': '†',
             'u': 'µ',
             'v': '\/',
             'w': '\^/',
             'x': 'χ',
             'y': "'/",
             'z': '&'}


@register.filter
def moon(text):
    """Transforms normal text to moon_speak"""
    moon_dict_not_viewed = MOON_DICT.copy()
    for letter in text:
        if letter in moon_dict_not_viewed:
            text = text.replace(letter, moon_dict_not_viewed.pop(letter))
    return text


@register.filter
def underscore(text):
    """Transforms all whitespaces to '__'"""
    # return '__'+text.replace(' ','__') + '__'
    return text.replace(' ', '__')


@register.filter
def pre_underscore(text):
    """Adds "__" at the beginning and the end"""
    return f"__{text}__"

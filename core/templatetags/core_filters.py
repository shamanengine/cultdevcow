from django import template
from functools import reduce

register = template.Library()

MOON_DICT = {'a': '@',
             'b': '|3',
             'c': '(',
             'd': '|)',
             'e': '3',
             'f': '<|>',
             'g': '[,',
             'h': '|~|',
             'i': '1',
             'j': ")'",
             'k': '|{',
             'l': '|_',
             'm': '/v\\',
             'n': '|\|',
             'o': '0',
             'p': '|7',
             'q': '0',
             'r': '|?',
             's': '5',
             't': '7',
             'u': '#',
             'v': '\/',
             'w': '\^/',
             'x': 'x',
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
    """Transforms all whitespaces to "__" and adds "__" at the beginning and the end"""
    # return '__'+text.replace(' ','__') + '__'
    return f"__{text.replace(' ', '__')}__"

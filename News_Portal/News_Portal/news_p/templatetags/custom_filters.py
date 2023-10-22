from django import template

register = template.Library()

CENZ_LIST = ['сука', 'дурак', 'тварь', 'тупой', ]


@register.filter()
def censorship(value):
    if type(value) != str:
        raise TypeError('Необходимо передать строку!')
    else:
        text = value.split()
        for i in text:
            for j in range(len(text)):
                if i.lower() in CENZ_LIST:
                    a = (len(i) - 1) * '*'
                    b = i[0] + a
                    text[j] = b
                    result = ' '.join(text)
                    return result
            else:
                return value

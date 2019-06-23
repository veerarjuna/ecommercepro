from django.template import Library
register = Library()


@register.filter()
def convert_digit_to_word(digit):
    word_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}
    return word_dict.get(int(digit), 'Five')



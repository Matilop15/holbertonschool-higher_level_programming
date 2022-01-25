#!/usr/bin/python3
"""
5-text_indentation
a function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    text must be a string
    add two new lines when find ?:.
    """
    new_string = ''
    idx = 0
    in_text = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    while idx < len(text):
        if text[idx] == ' ' and in_text == 0:
            idx += 1
            continue
        in_text = 1

        if text[idx] in '?:.':
            new_string += text[idx]
            new_string += '\n'
            new_string += '\n'
            idx += 1

            while idx < len(text) and text[idx] == ' ':
                idx += 1
            continue

        if idx < len(text):
            new_string += text[idx]
            idx += 1

    print(new_string, end='')

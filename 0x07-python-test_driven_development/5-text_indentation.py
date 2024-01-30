#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """function that prints text with two new lines and ('.' '?' ':')

    Args:
        text (string): to be print.
    Raises:
        TypeError: if text isn't a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1

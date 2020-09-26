#!/usr/bin/python3
"""text_indentation"""


def text_indentation(text):
    """text_indentation

    Args:
        text ([str]): [description]

    Raises:
        TypeError: text must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    list = [".", "?", ":"]
    i = 0
    while i < len(text):
        if text[0] == " ":
            while text[i] == " ":
                i += 1
        print(text[i], end='')
        if text[i] in [".", "?", ":"]:
            print("\n")
            i += 1
            while text[i] == " ":
                i += 1
            continue
        i += 1

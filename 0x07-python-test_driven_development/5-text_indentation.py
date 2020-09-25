#!/usr/bin/python3

def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    list = [".", "?", ":"]
    flag = 0
    for i in range(len(text)):
        print(text[i], end='')
        if text[i] in [".", "?", ":"]:
            while text[i] != " ":
                i += 1
            print("\n")
        
#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        tupla_c = (len(sentence), sentence[0])
        return(tupla_c)
    else:
        tupla_c = (0, None)
        return(tupla_c)

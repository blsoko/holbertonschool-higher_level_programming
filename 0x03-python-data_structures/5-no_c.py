#!/usr/bin/python3
def no_c(my_string):
    varnew = ""
    for letra in my_string:
        if letra != "c" and letra != "C":
            varnew += letra
    return(varnew)

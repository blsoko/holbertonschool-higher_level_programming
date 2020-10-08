#!/usr/bin/python3
"""Write a script that adds all arguments to a
    Python list, and then save them to a file
"""

import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    vlist = load_from_json_file("add_item.json")
except:
    vlist = []
i = 1
for value in sys.argv:
    if i == 1:
        i += 1
        continue
    vlist.append(value)
save_to_json_file(vlist, "add_item.json")

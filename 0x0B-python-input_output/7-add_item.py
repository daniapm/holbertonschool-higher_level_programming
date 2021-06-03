#!/usr/bin/python3
"""Documentation for a  script that adds all arguments to a Python list"""


from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    try:
        json_list = load_from_json_file("add_item.json")
    except:
        json_list = []
    i = 1
    for i in range(1, len(argv)):
        json_list.append(argv[i])
        i += 1
    save_to_json_file(json_list, "add_item.json")

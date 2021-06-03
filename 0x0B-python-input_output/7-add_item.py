#!/usr/bin/python3
"""Documentation for a  script of python"""


from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    try:
        employee_dict = load_from_json_file("add_item.json")
    except:
        json_list = []
for i in range(1, len(argv)):
    json_list.append(argv[i])
save_to_json_file(json_list, "add_item.json")

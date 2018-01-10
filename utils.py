import pandas as pd

def create_script(func_str, output_script_file_path=r".\machine_induced_script.py"):
    output_script = \
"""import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

log_lines = open(input_file_path, "r").readlines()
{}
open(output_file_path, "w").write("\\n".join(output_list))
print(\"done writing\", output_file_path)""".format(func_str)
    open(output_script_file_path, "w").write(output_script)


def get_all_substrings(input_string):
    length = len(input_string)
    return set([input_string[i:j+1] for i in range(length) for j in range(i,length)])


def get_intersection_of_list_of_sets(list_of_sets):
    set_0 = list_of_sets[0]
    for a_set in list_of_sets[1:]:
        set_0 = set_0.intersection(a_set)
    return set_0


def get_max_length_common_string(string_1, string_2):
    union_list = [substring for substring in get_all_substrings(string_1) if substring in string_2]
    common_string = union_list[pd.Series(union_list).apply(len).argmax()]
    return common_string


def get_max_length_common_string_of_list(string_list):
    common_string = string_list[0]
    for string_2 in string_list[1:]:
        common_string = get_max_length_common_string(common_string, string_2)
    return common_string

import os
import experimental
import utils

all_lines = open(r".\simple_user_input.txt", "r").read().split("\n")
log_file_path = all_lines[0]
output_strings_list = [output_string for output_string in all_lines[1:] if output_string != ""]

log_lines = open(log_file_path, "r").readlines()

output_list, program_str = experimental.get_info_from_log(log_lines, output_strings_list)

utils.create_script(program_str)

os.system('.\machine_induced_script.py .\{} .\log_output_example.txt'.format(log_file_path))

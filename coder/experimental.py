import pandas as pd
import utils


def get_function(input_output_data_frame):
    prefix_list = []
    suffix_list = []
    for index, row in input_output_data_frame.iterrows():
        sub_string = row["output"]
        line = row["input"]
        start_index = line.find(sub_string)
        end_index = start_index + len(sub_string)
        prefix = line[:start_index][-15:]
        suffix = line[end_index:][:15]
        prefix_list.append(prefix)
        suffix_list.append(suffix)
    common_prefix = utils.get_max_length_common_string_of_list(prefix_list)
    common_suffix = utils.get_max_length_common_string_of_list(suffix_list)
    func_str = "x = x.split(\"{}\")[1].split(\"{}\")[0]".format(common_prefix, common_suffix)
    return func_str


def apply_func_on_log_lines(log_lines, func_str):
    log_lines = [line.replace("\n", "") for line in log_lines]
    d = {"log_lines": log_lines}
    exec(func_str, d)
    return d["output_list"]


def get_info_from_log(log_lines, output_strings_list):
    log_lines = [line.replace("\n", "") for line in log_lines]
    interesting_lines = []
    interesting_input_output_list = []
    for line in log_lines:
        for output_string in output_strings_list:
            if output_string in line:
                interesting_lines.append(line)
                interesting_input_output_list.append((line, output_string))

    common_string = utils.get_max_length_common_string_of_list(interesting_lines)

    common_string_no_numeric_trail = \
        common_string[:(-pd.Series(list(common_string)).str.isnumeric().values[::-1].argmin())]

    input_output_data_frame = pd.DataFrame(interesting_input_output_list, columns=["input", "output"])

    func_str = get_function(input_output_data_frame)

    program_str = """
output_list = []
for line in log_lines:
    if \"{}\" in line:
        x = line
        {}
        output_list.append(x)
""".format(common_string_no_numeric_trail, func_str)

    output_list = apply_func_on_log_lines(log_lines, program_str)

    return output_list, program_str

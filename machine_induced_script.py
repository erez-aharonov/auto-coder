import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

log_lines = open(input_file_path, "r").readlines()

output_list = []
for line in log_lines:
    if "]: Failed password for root from 218.49.183.17 port " in line:
        x = line
        x = x.split("49.183.17 port ")[1]
        x = x.replace("\n", "")
        output_list.append(x)

open(output_file_path, "w").write("\n".join(output_list))
print("done writing", output_file_path)
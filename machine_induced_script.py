import sys

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

log_lines = open(input_file_path, "r").readlines()

output_list = []
for line in log_lines:
    if "" in line:
        x = line
        x = x.split(" knight ")[1].split(": ")[0]
        output_list.append(x)

open(output_file_path, "w").write("\n".join(output_list))
print("done writing", output_file_path)
import os, sys

total_args = len(sys.argv)
if total_args != 2:
    print("Date not supplied")
    sys.exit(1)

current_date = sys.argv[1]

output_dir = f"../archived/{current_date}"
output_filename = os.path.join(output_dir, "list.md")

source_dir = "./tmp/prompts/"

with open(output_filename, "a") as output_file:
    for filename in os.listdir(source_dir):
        if filename.endswith(".txt"):
            source_filepath = os.path.join(source_dir, filename)
            with open(source_filepath, "r") as source_file:
                content = source_file.read()
                output_file.write(filename.split('-')[0] + " => `" + content + "`" + "  ")

# Sort entries
with open(output_filename, "r+") as output_file:
    lines = output_file.readlines()

# Remove empty lines
updated_lines = []
for line in lines:
    if line.strip() != "" and line.strip() != '`':
        updated_lines.append(line)

with open(output_filename, "w") as output_file:
    for line in sorted(updated_lines, key=lambda x: int(x.split(' => ')[0].strip(' `'))):
        output_file.write(line)

print(f"Prompts merging completed")
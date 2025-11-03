names_str = input("Enter names spaces separated = ")
names_list = names_str.split()
names_list.sort()
names_tuple = tuple(names_list)

with open("names_data.txt", "w") as output_file:
    output_file.write(f"List = {names_list}\n")
    output_file.write(f"Tuple = {names_tuple}\n")

with open("names_data.txt", "r") as outpt_file:
    content = outpt_file.read()
    print(content)
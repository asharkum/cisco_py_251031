words_seq = input("Enter a sequence of words separated by spaces : ")
print("You entered:", words_seq)
words_list = words_seq.split()
print("List of words:", words_list) 
words_tuple = tuple(words_list)
print("Tuple of words:", words_tuple)

# output_file = open("qn01_data.txt", "w")
# output_file.write("List of words: " + str(words_list) + "\n")
# output_file.write("Tuple of words: " + str(words_tuple) + "\n")
# output_file.close()

with open("qn01_data.txt", "w") as output_file:
    output_file.write("List of words: " + str(words_list) + "\n")
    output_file.write("Tuple of words: " + str(words_tuple) + "\n")

print("Data written to qn01_data.txt")

with open("qn01_data.txt", "r") as input_file:
    content = input_file.read()
    print("Content of qn01_data.txt:")
    print(content)
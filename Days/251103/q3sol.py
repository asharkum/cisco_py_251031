sentence = input("Enter a sentence: ")

words_list = sentence.split()
words_tuple = tuple(word.upper() for word in words_list)

with open("sentence_data.txt", "w") as file:
    file.write("List of words:\n")
    file.write(str(words_list) + "\n")
    file.write("Tuple of uppercase words:\n")
    file.write(str(words_tuple) + "\n")

with open("sentence_data.txt", "r") as file:
    content = file.read()
    print("Data read from file:")
    print(content)
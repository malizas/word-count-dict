"""Count words in file."""
# function version:
# def word_count(file):

#     text = open(file)
#     word_count_dict = {}

#     for line in text:
#         for word in line.split():
#             word_count_dict[word] = word_count_dict.get(word, 0) + 1

#     for word,count in word_count_dict.items():
#         return word,count

    #return word_count_dict.items()
# my_dict[key]: [value]
# word_count[word]: [count]

#print(word_count("test.txt"))

#non-function version
import sys

text = open(sys.argv[1])

word_count_dict = {}
for line in text:
    words = line.split()
    for word in words:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
        
for word,count in word_count_dict.items(): #makes the code more clean
    print(word, count)

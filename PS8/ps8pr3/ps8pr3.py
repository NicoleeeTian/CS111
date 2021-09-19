#
# ps8pr3.py - Problem Set 8, Problem 3
#
# Markov text generation
# pair work member: Chuning Shi
import random
def create_dictionary(filename):
    """This function takes a string representing the name of a text file and
    returns a dictionary of key-value pairs
    """
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()

    result={}
    current_word = '$'
    for next_word in words:
        if current_word not in result:
            result[current_word] = [next_word]
        else:
            result[current_word]+=[next_word]
        if next_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word
    return result

def generate_text(word_dict, num_words):
    """this function uses word_dict to generate num_words by creat_dictionary
    """
    current_word = '$'
    for i in range(num_words):
        wordlist=word_dict[current_word]
        next_word=random.choice(wordlist)
        print(next_word, end=' ')
        if next_word[-1] in ".?!":
            current_word = '$'
        elif next_word not in word_dict:
            current_word = "$"
        else:
            current_word=next_word
    print()
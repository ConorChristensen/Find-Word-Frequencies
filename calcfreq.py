#Conor Christensen
#Last edited 28/04/17

from hash_table import hash_table

file_name = 'splitwords.txt'
file = open(file_name)
word_count = 0
for line in file:
    word_count += 1
word_frequency = hash_table(10*word_count) #Gives a work load of 1/10
file.close()
file = open(file_name)
for line in file:
    line = line.rstrip()
    word_frequency[line] = 1
file.close()


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)



def print_freq(word_frequency, file_name):
    file = open(file_name)
    output_file = open("frequencies.txt", 'w')
    output_file.write("    Word        Frequency \n")
    output_file.write("------------------------------- \n")
    output_list = []
    for a_word in range(word_frequency.size):
        if word_frequency.array[a_word] != None:
            word = word_frequency.array[a_word][0]
            output_list.append([word, word_frequency.array[a_word][1]])
    quicksort(output_list)
    for i in range(len(output_list)):
        spaces = 14-len(output_list[i][0])
        output_file.write("    " + str(output_list[i][0]))
        for space in range(spaces):
            output_file.write(" ")
        output_file.write(str(output_list[i][1]) + "\n")

print_freq(word_frequency, file_name)

#Conor Christensen
#Last Edited 28/04/17

def str_replace(string, position, new_character):
    head = string[0:position]
    tail = string[position+1:len(string)]
    head += new_character
    new_string = head + tail
    return new_string

def read_contents():
    file_ = open(input("Please enter in the file name desired: "))
    lines_list = []
    final_list = []
    alphabet_list_lower = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',' ']
    alphabet_list_upper = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    for line in file_:
        lines_list.append(line)

    for line_loop in range(len(lines_list)):
        for character_loop in range(len(lines_list[line_loop])):
            if lines_list[line_loop][character_loop] not in alphabet_list_lower and lines_list[line_loop][character_loop] not in alphabet_list_upper:
                lines_list[line_loop] = str_replace(lines_list[line_loop], character_loop, ' ')
        lines_list[line_loop] = lines_list[line_loop].upper()
        lines_list[line_loop] = lines_list[line_loop].split(' ') #after this step we should have a list of lists with words

    for a_line in range(len(lines_list)):
        for a_word in range(len(lines_list[a_line])):
            if len(lines_list[a_line][a_word]) >=1:
                final_list.append(lines_list[a_line][a_word])

    return(final_list)

def print_split(word_list):
    output_file = open('splitwords.txt', 'w')
    print_loop = len(word_list)
    for a_word in range(print_loop):
        output_file.write(str(word_list[a_word]) + '\n')

print_split(read_contents())


#Conor Christensen
#Last Edited 28/04/17

class hash_table:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.array = size*[None]

    def hash(self, key):
        hash_index = 0
        a = 691
        b = 443
        for i in range(len(key)):
            hash_index = (ord(key[i]) + a * hash_index)%self.size
            a = a * b % (self.size - 1)
        return hash_index

    def __setitem__(self, key, value):
        index = self.hash(key)
        if self.array[index] == None:
            self.array[index] = [key, value]
            self.count += 1
        elif self.array[index][0] == key:
            self.array[index][1] += 1
        else:
            is_set = False
            jump = 1
            while jump < self.size - index and is_set == False:
                if self.array[index+jump] == None:
                    self.array[index+jump] = [key, value]
                    self.count += 1
                    is_set = True
                elif self.array[index + jump][0] == key:
                    self.array[index+jump][1] += 1
                    is_set = True
                jump *= jump
            if not is_set:
                for starting_point in range(1, self.size):
                    jump = 0
                    while jump < self.size - starting_point and is_set == False:
                        index = jump+starting_point
                        if self.array[index] == None:
                            self.array[index] = [key, value]
                            self.count += 1
                            is_set = True
                        elif self.array[index][0] == key:
                            self.array[index][1] += 1
                            is_set = True
                        jump *= jump
                if not is_set:
                    raise IndexError("The table is full and the word does not yet exist in it.")


    def __getitem__(self, key):
        index = self.hash(key)
        if self.array[index] == None:
            raise KeyError("Key does not exist in hash table.")
        elif self.array[index][0] == key:
            return self.array[index][1]
        else:
            jump = 1
            while jump < self.size - index:
                if self.array[index+jump] == None:
                    raise KeyError("Key does not exist in hash table.")
                elif self.array[index + jump][0] == key:
                    return self.array[index+jump][1]
                jump *= jump

            for starting_point in range(1, self.size):
                jump = 0
                while jump < self.size - starting_point:
                    index = jump+starting_point
                    if self.array[index] == None:
                        raise KeyError("Key does not exist in hash table.")
                    elif self.array[index][0] == key:
                        return self.array[index][1]
                    jump *= jump
            raise KeyError("Key does not exist in hash table.")

    def resize(self, new_size):
        if new_size <= self.size:
            raise ValueError ("The table cannot be reduced in size, only increased")
        self.array += (new_size-self.size) * [None]
        self.size = new_size
        for i in range(self.size):
            if self.array[i] != None:
                key = self.array[i][0]
                value = self.array[i][1]
                self.array[i] = None
                self[key] = value

    def delete(self, key):
        index = self.hash(key)
        if self.array[index] == None:
            raise KeyError("Key does not exist in hash table.")
        elif self.array[index][0] == key:
            self.array[index] = None
        else:
            jump = 1
            is_deleted = False
            while jump < self.size - index and is_deleted == False:
                if self.array[index+jump] == None:
                    raise KeyError("Key does not exist in hash table.")
                elif self.array[index + jump][0] == key:
                    self.array[index + jump] = None
                    is_deleted = True
                jump *= jump

            for starting_point in range(1, self.size):
                jump = 0
                while jump < self.size - starting_point and is_deleted == False:
                    index = jump+starting_point
                    if self.array[index] == None:
                        raise KeyError("Key does not exist in hash table.")
                    elif self.array[index][0] == key:
                        self.array[index] = None
                        is_deleted = True
                    jump *= jump
            raise KeyError("Key does not exist in hash table.")

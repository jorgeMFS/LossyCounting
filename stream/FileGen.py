'''
Created on 22/12/2016

@author: Jorge Miguel Ferreira da Silva
'''
import os.path
import random
import string


class FileGen(object):
    """
    FileGen is a python class that generates files txt with a x number of characters
    """

    def __init__(self, numb):
        """
        Constructor of FileGen Class
        """

        self.number_character = numb
        self.filename = str(self.number_character) + "stream.txt"

    def getfilename(self):
        return self.filename

    def set_file_txt(self):
        if os.path.isfile(self.filename):
            f = open(self.filename, 'w')
        else:
            f = open(self.filename, 'x')

        self.write_to_file(f)
        f.flush()
        f.close()

    def write_to_file(self, f):

        stream = ''
        for c in range(self.number_character-1):
            stream += random.choice(string.ascii_lowercase)

        stream_string = ''.join(stream)
        s = " ".join(stream_string)
        f.write(s)


def read_to_stream(string_name):
    assert isinstance(string_name, str)
    with open(string_name, 'r') as f:
        read_data = f.read()
    read_data = read_data.replace(" ", "")
    assert isinstance(read_data, str)
    return read_data

"""
Created on 27/12/2016

@author: Jorge Miguel Ferreira da Silva
"""

from stream.FileGen import FileGen
import os

if __name__ == '__main__':
    """
        Script that generates files to be tested
    """
    # Create Files
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = '.\\files'
    directory = os.path.dirname(__file__)
    director = os.path.join(directory, path)
    os.chdir(director)

    k_list = list()
    k_list = [10, 100, 1000, 10000, 100000]
    for number_characters in k_list:
        file = FileGen(number_characters)
        file.set_file_txt()

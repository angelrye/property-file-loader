import io
import os


class PropertyFileLoader:

    def __init__(self, file):
        '''
        Accepts a Text File object 
        '''
        self.__file__ = file
        self.properties = dict()
        self.__load_properties__()

    def __load_properties__(self):
        if isinstance(self.__file__, io.TextIOWrapper):
            self.__update_properties__(self.__file__)
        else:
            raise TypeError('Invalid file')

    def __yeild_line__(self, property_file):
        '''
        Returns a generator for the opened file and yields line by line.
        does not return comments and blank lines
        returns ValueError if property file is malformed.
        '''
        for line in property_file:
            if (line in ['\n', '\n\r']) or (len(line.strip()) == 0) or (line.strip()[0] == '#'):
                continue

            if (int(line.find('=')) < 0):
                raise ValueError(f'Malformed property file: {line}')

            yield line

    def __create_property_dict__(self, text):
        key, value = text.split('=')
        return {f'{key.strip()}': f'{value.strip()}'}

    def __update_properties__(self, file):
        for key_value in self.__yeild_line__(file):
            self.properties.update(
                self.__create_property_dict__(key_value))

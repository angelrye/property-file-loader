import io
import os


class PropertyFileLoader:

    def __init__(self, file):
        '''
        Accepts a Text File object or filename 
        '''
        self.__properties__ = dict()

        def yield_line(file):
            for line in file:
                if (line in ['\n', '\n\r']) or (len(line.strip()) == 0) or (line.strip()[0] == '#'):
                    continue

                if (int(line.find('=')) < 0):
                    raise ValueError(f'Malformed property file: {line}')

                yield line

        def new_dict(text):
            key, value = text.split('=')
            return {f'{key.strip()}': f'{value.strip()}'}

        def update_property(properties):
            for key_value in yield_line(properties):
                self.__properties__.update(new_dict(key_value))

        if isinstance(file, str):
            with open(file) as prop:
                update_property(prop)

        elif isinstance(file, io.TextIOWrapper):
            update_property(file)
        else:
            raise TypeError('Invalid file')

    def getpropertyvalue(self, key):
        value = self.__properties__.get(key)

        if not value:
            raise ValueError('Property is not defined.')

        return value

    def iskeyexist(self, key):
        return key in self.__properties__

    def getproperties(self):
        return self.__properties__

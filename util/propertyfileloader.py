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

        def yield_line():
            for line in self.__file__:
                if (line in ['\n', '\n\r']) or (len(line.strip()) == 0) or (line.strip()[0] == '#'):
                    continue

                if (int(line.find('=')) < 0):
                    raise ValueError(f'Malformed property file: {line}')

                yield line

        def new_dict(text):
            key, value = text.split('=')
            return {f'{key.strip()}': f'{value.strip()}'}

        if not (self.__file__):
            raise RuntimeError('PropertyFileLoader class was not initialized.')

        if isinstance(self.__file__, io.TextIOWrapper):

            for key_value in yield_line():
                self.properties.update(new_dict(key_value))
        else:
            raise TypeError('Invalid file')

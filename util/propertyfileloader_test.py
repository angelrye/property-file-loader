import os
from propertyfileloader import PropertyFileLoader

file_path = './prop.properties'


def test():

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, 'prop.properties')

    with open(path) as file:
        propertyfileloader = PropertyFileLoader(file)

    print(propertyfileloader.properties)


if __name__ == '__main__':
    test()

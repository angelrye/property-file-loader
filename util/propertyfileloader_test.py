import os
from propertyfileloader import PropertyFileLoader

file_path = './prop.properties'


def test():

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, 'prop.properties')

    with open(path) as file:
        propertyfileloader = PropertyFileLoader(file)

    print(propertyfileloader.__properties__)

    print(
        f"is Property 1 configured? {propertyfileloader.iskeyexist('property1')}")
    print(
        f"is Property 2 configured? {propertyfileloader.iskeyexist('property2')}")

    print(
        f"Value of property1 is {propertyfileloader.getpropertyvalue('property1')}")
    print(
        f"Value of property1 is {propertyfileloader.getpropertyvalue('property2')}")


if __name__ == '__main__':
    test()


from operator import methodcaller

from zeep import Client


def read_soap(instruction: dict):
    """
    Reads soap connection.

    """


    client = Client(instruction['adress'])
    caller = methodcaller(instruction['endpoint'])
    response = caller(client.service)

    for line in response:
        yield line


from operator import methodcaller

from zeep import Client

# result = client.service.ConvertSpeed(
#     100, 'kilometersPerhour', 'milesPerhour')

# assert result == 62.137





def read_soap(instruction: dict):
    """
    Reads soap connection.

    """


    client = Client(instruction['adress'])
    caller = methodcaller(instruction['endpoint'])
    response = caller(client.service)

    for line in response:
        yield line

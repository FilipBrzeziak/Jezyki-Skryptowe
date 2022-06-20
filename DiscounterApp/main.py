import Service
from Operations import Operations

if __name__ == '__main__':
    operations = Operations()
    service = Service.Service(operations)
    service.add_default_values()
    service.choose_version()

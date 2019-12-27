from dependency_injector import providers, containers


class Client(object):
    def __init__(self, config):
        self._config = config
        self.connect(self._config)

    def connect(self, config):
        pass


class Reader(object):
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e

    def read(self):
        pass


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')


class Clients(containers.DeclarativeContainer):
    client = providers.Singleton(Client, Configs.config)


class Readers(containers.DeclarativeContainer):
    reader = providers.Factory(Reader, client=Clients.client)


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')


class Clients(containers.DeclarativeContainer):
    client = providers.Singleton(Client, Configs.config)


class Readers(containers.DeclarativeContainer):
    reader = providers.Factory(Reader, client=Clients.client)


if __name__ == "__main__":
    Configs.config.override({
        "name": "Roman",
        "Surname": "Lynnyk",
        "password": "YOUR_PASSWORD",
    })
    reader = Readers.reader()
    print(reader.read())

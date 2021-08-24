from enum import Enum
from service_builders import SpotifyServiceBuilder


class ServiceBuilderFactory:
    """
    Main factory class to house all service builders, which are responsible for instantiating service instances.
    To create service, clients of this API must first register the service.
    """
    def __init__(self):
        self.builders = {}

    def register(self, service_name, builder):
        self.builders[service_name] = builder

    def create(self, service_name, **kwargs):
        builder = self.builders.get(service_name)
        if not builder:
            raise ValueError(f'Service {service_name} does not exist')

        return builder(**kwargs)


service_builder_factory = ServiceBuilderFactory()


# Service configurations
configs = {
    "client_key": "spotifyClientKey",
    "client_secret": "spotifyClientSecret"
}

# Register service builder
service_builder_factory.register('spotify', SpotifyServiceBuilder())
# Create new instance of Spotify service
spotify_service = service_builder_factory.create('spotify', **configs)
print(spotify_service.key)

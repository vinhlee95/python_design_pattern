"""
To make it easy to follow, this module will specify interfaces of all service builders
"""


class SpotifyService:
    """
    Base class for Spotify service
    Note: never use this class to create a new instance of the service. Clients should use corresponding service builder
    """
    key: str
    secret: str

    def __init__(self, client_key: str, client_secret: str):
        self.key = client_key
        self.secret = client_secret


class SpotifyServiceBuilder:
    """
    Spotify service builder class. Used to create an instance of SpotifyService.
    This is a bridge between the clients and SpotifyService.
    """
    instance: SpotifyService

    def __init__(self):
        self.instance = None

    def __call__(self, client_key, client_secret, **kwargs):
        if self.instance:
            return self.instance

        consumer_key, consumer_secret = self.authorize(client_key, client_secret)
        self.instance = SpotifyService(consumer_key, consumer_secret)
        return self.instance

    def authorize(self, client_key, client_secret):
        """
        For the sake of simplicity, only return client key and secret here.
        In reality, this method should e.g. call Spotify API to actually authorize the client
        """
        return client_key, client_secret

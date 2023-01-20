class TwitterConfiguration:
    consumer_key = None
    consumer_secret = None
    access_token_key = None
    access_token_secret = None

    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

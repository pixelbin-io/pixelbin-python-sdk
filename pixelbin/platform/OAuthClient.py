"""OAuth Client."""

class OAuthClient:
    def __init__(self, config):
        self._conf = config
        self.token = config.apiSecret


    async def getAccessToken(self):
        return self.token


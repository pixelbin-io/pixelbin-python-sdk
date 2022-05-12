"""Pixelbin Config."""

from typing import Dict

from ..common.constants import DEFAULT_DOMAIN
from .OAuthClient import OAuthClient


class PixelbinConfig:
    def __init__(self, config: Dict):
        self.domain = config.get("domain", DEFAULT_DOMAIN)
        self.apiSecret = config.get("apiSecret", "")
        self.oauthClient = OAuthClient(self)

    async def getAccessToken(self):
        token = await self.oauthClient.getAccessToken()
        return token

"""Pixelbin Config."""

from ..common.constants import DEFAULT_DOMAIN, APPLICATION_MIN_TOKEN_LENGTH
from .OAuthClient import OAuthClient
from ..common.exceptions import PixelbinInvalidCredentialError


class PixelbinConfig:
    """PixelbinConfig hold the configuration detail"""

    def __init__(self, config: dict):
        """
        summary: create instance of PixelbinConfig

        :param - config : configuration details in key value terms : Type - dict
        """
        self.domain = config.get("domain", DEFAULT_DOMAIN)
        self.apiSecret = config.get("apiSecret", "")
        self.options = config.get("options", {})
        self.oauthClient = OAuthClient(self)
        self.validate()

    async def getAccessToken(self) -> str:
        """
        summary: return the access token
        """
        token = await self.oauthClient.getAccessToken()
        return token

    def get_http_client_options(self) -> dict:
        """
        summary: return the HTTP client options

        :return: dictionary containing HTTP client options
        """
        http_options = self.options.get("httpClientOptions", {})
        trust_env = http_options.get("trust_env", False)
        return {"trust_env": trust_env}

    def validate(self):
        """Validates apiSecret."""
        if not self.apiSecret:
            raise PixelbinInvalidCredentialError("No API Secret Token Present")

        if len(self.apiSecret) < APPLICATION_MIN_TOKEN_LENGTH:
            raise PixelbinInvalidCredentialError("Invalid API Secret Token")

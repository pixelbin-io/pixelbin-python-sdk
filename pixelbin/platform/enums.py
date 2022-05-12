"""Platform Enums."""

from enum import Enum



class AccessEnum(Enum):
    
    PUBLIC_READ = "public-read"
    
    PRIVATE = "private"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid AccessEnum type")




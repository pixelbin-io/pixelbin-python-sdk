from datetime import datetime

import pytz

from .constants import TIMEZONE

timezone = pytz.timezone(TIMEZONE)


def get_ist_now():
    """Returns Indian Standard Time datetime object.

    Returns:
        object -- Datetime object
    """
    return datetime.now(timezone)

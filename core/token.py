from .hashing import hash_token
from .utils import get_cpu_uuid

import time


def token():
    uuid = get_cpu_uuid()

    full_token = uuid + "(:)" +time.strftime("%Y-%m-%d")
    return hash_token(full_token)

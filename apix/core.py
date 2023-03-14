from enum import StrEnum

import httpx
import pydantic


class HTTPMethod(StrEnum):
    """ Supported HTTP methods """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"




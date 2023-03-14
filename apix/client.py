"""
Contains all the base classes used to instantiate clients, both async and sync.
"""
from abc import ABC
from enum import StrEnum


class HTTPMethod(StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"


class Request:
    """ Generic request """


class Client:
    """ HTTP Client """
    url: str
    queue: list[Request]
    is_async: bool = False

    def create_request(self):
        """ Instanciate a Request and store it for execution later. """
        self.queue.append(Request())

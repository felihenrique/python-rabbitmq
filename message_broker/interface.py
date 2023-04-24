from typing import Any, Coroutine, Protocol
from collections.abc import Callable

class MessageBrokerInterface(Protocol):
    def connect(self, uri: str, parallel_messages: int = 5):
        raise NotImplementedError()

    def send_message(self, queue_name: str, data: bytes):
        raise NotImplementedError()

    def register_consumer(self, queue_name: str, consumer: Callable[[Any], Coroutine]):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

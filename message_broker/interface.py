from typing import Protocol

class MessageBrokerInterface(Protocol):
    def connect(self, uri: str, parallel_messages: int = 5):
        raise NotImplementedError()

    def send_message(self, queue_name: str, data: bytes):
        raise NotImplementedError()

    def register_consumer(self, queue_name: str, callback):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

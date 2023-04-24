
class MessageBrokerInterface:
    def connect(self, uri: str, parallel_messages: int = 5):
        pass

    def send_message(self, queue_name: str, data: dict):
        pass

    def register_consumer(self, queue_name: str, callback):
        pass

    def close():
        pass

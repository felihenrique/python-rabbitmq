from message_broker.MessageBrokerInterface import MessageBrokerInterface
import aio_pika
import json
from collections.abc import Callable
from typing import Any, Coroutine

class MessageBrokerRabbitMQ(MessageBrokerInterface):
    __connection: aio_pika.abc.AbstractRobustConnection = None
    __channel: aio_pika.abc.AbstractChannel = None
    __queues = {}

    async def __get_or_create_queue__(self, queue_name: str) -> aio_pika.abc.AbstractQueue:
        if self.__connection == None:
            raise Exception("RabbitMQ is not connected. Please call connect() first.")
        if self.__queues.get(queue_name):
            return self.__queues[queue_name]
        queue = await self.__channel.declare_queue(queue_name)
        self.__queues[queue_name] = queue
        return queue

    async def connect(self, uri: str, parallel_messages: int = 5):
        self.__connection = await aio_pika.connect_robust(uri)
        self.__channel = await self.__connection.channel()
        await self.__channel.set_qos(parallel_messages)

    async def send_message(self, queue_name: str, data: dict):
        queue = await self.__get_or_create_queue__(queue_name)
        queue.channel.basic_publish(data, routing_key=queue_name)

    async def register_consumer(self, queue_name: str, callback: Callable[[Any], Coroutine]):
        queue = await self.__get_or_create_queue__(queue_name)
        async def dummy_callback(message: aio_pika.abc.AbstractIncomingMessage):
            message_body = json.loads(message.body)
            try:
                await callback(message_body)
            except Exception as error:
                print('An error ocurred while processing message: ')
                print(error)
            finally:
                await message.ack()
        await queue.consume(dummy_callback)

    async def close(self):
        await self.__channel.close()
        await self.__connection.close()

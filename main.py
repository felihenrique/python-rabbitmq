import asyncio
from config import config
from message_broker import MessageBrokerRabbitMQ, MessageBrokerInterface
from typing import Any

async def main():
    broker: MessageBrokerInterface = MessageBrokerRabbitMQ()
    await broker.connect(
        config.rabbitmq_uri,
        config.rabbitmq_prefetch_count
    )

    async def consumer(message: Any):
        print(message)

    await broker.register_consumer('teste', consumer)

    try:
        print('Application started consuming')
        await asyncio.Future()
    finally:
        await broker.close()

if __name__ == "__main__":
    asyncio.run(main())

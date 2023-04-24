from message_broker.MessageBrokerRabbitMQ import MessageBrokerRabbitMQ
from config import config
import asyncio

async def main():
    broker = MessageBrokerRabbitMQ()
    await broker.connect(
        config.rabbitmq_uri,
        config.rabbitmq_prefetch_count
    )

    async def consumer(message):
        print(message)

    await broker.register_consumer('teste', consumer)

    try:
        print('Application started consuming')
        await asyncio.Future()
    finally:
        await broker.close()

if __name__ == "__main__":
    asyncio.run(main())

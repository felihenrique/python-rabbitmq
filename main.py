import asyncio
from config import config
from message_broker import MessageBrokerRabbitMQ, MessageBrokerInterface
from process_chat_responses import process

async def main():
    broker: MessageBrokerInterface = MessageBrokerRabbitMQ()
    await broker.connect(
        config.rabbitmq_uri,
        config.rabbitmq_prefetch_count
    )

    await broker.register_consumer(config.rabbitmq_queue_name, process)

    try:
        print('Application started consuming')
        await asyncio.Future()
    finally:
        await broker.close()

if __name__ == "__main__":
    asyncio.run(main())

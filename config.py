import os
from dotenv import load_dotenv

load_dotenv()

class ConfigObject:
    rabbitmq_uri: str = os.environ['RABBITMQ_URI']
    rabbitmq_prefetch_count: int = int(os.environ['RABBITMQ_PREFETCH_COUNT'])
    rabbitmq_queue_name: str = os.environ['RABBITMQ_QUEUE_NAME']
    mongodb_uri: str = os.environ['MONGODB_URI']

config = ConfigObject()

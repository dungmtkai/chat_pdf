import os
from dataclasses import dataclass


@dataclass
class Kafka:
    # Kafka admin client
    bootstrap_server = "localhost:9092"
    client_id = "chat_pdf"

    # Kafka topic
    kafka_topics = {
        "chat": {"input_topic": "chat.request", "output_topic": "chat.response"},
        "ingest": {"input_topic": "ingest.request", "output_topic": "ingest.response"},
    }

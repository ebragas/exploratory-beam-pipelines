"""Generate fake data and publish it to a configured Pub/Sub project/topic

Assumes use of Application Default Credentials
"""
import json
import time
from google.cloud import pubsub_v1

from rich.console import Console
console = Console()

from faker import Faker
fake = Faker()


PROJECT_ID = "beam-udemy"
TOPIC_ID = "beam-example-input"


def gen_fake_records(max_records=3):
    """Generate records; limited to avoid accidental cost overrun"""
    for i in range(max_records):
        record = {
            "name": fake.name(),
            "address": fake.address(),
            "transaction_amt": fake.pyfloat(
                right_digits=2, 
                max_value=100, 
                min_value=0
            )
        }
        yield record


def publish_record(record):
    publisher = pubsub_v1.PublisherClient()
    topic_name = f'projects/{PROJECT_ID}/topics/{TOPIC_ID}'

    publisher.publish(topic_name, json.dumps(record).encode('utf-8'))


if __name__ == "__main__":

    for record in gen_fake_records(max_records=10):
        publish_record(record)
        time.sleep(1)
        console.print("published record", record)

    console.print("All records published")
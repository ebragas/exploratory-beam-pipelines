"""Generate fake data and publish it to a configured Pub/Sub project/topic
"""
from faker import Faker
fake = Faker()

def gen_fake_record():
    yield fake.name(), fake.address(), fake.pyfloat(
        right_digits=2, 
        max_value=100, 
        min_value=0
    )

if __name__ == "__main__":
    print(gen_fake_record())
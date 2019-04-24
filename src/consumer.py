import sys
import os
import argparse
import json

from kafka import KafkaConsumer


def get_args():
    parser = argparse.ArgumentParser('consumer')
    parser.add_argument('--topic', type=str, default='test')
    return parser.parse_args()


def get_consumer(topic):
    return KafkaConsumer(topic)


def main():
    args = get_args()
    consumer = get_consumer(args.topic)
    distinct = set()
    for message in consumer:
        jmessage = json.loads(message.value)
        event_name = jmessage['event']['event_name']
        if event_name not in distinct:
            distinct.add(event_name)
            print(event_name)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

import sys
import os
import requests
import argparse

from kafka import KafkaProducer


def get_args():
    parser = argparse.ArgumentParser('producer')
    parser.add_argument("bootstrap_servers", type=str)
    parser.add_argument("url", type=str)
    parser.add_argument("--topic", type=str, default='test')
    return parser.parse_args()


def get_producer(bootstrap_servers):
    return KafkaProducer(bootstrap_servers=bootstrap_servers)


def get_messages(url):
    return requests.get(url, stream=True).iter_lines()


def main():
    args = get_args()
    producer = get_producer(args.bootstrap_servers)
    messages = get_messages(args.url)
    for message in messages:
        producer.send(args.topic, message)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

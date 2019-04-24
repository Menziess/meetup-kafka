# meetup-kafka

Obtaining event names from a kafka stream from meetup.com

## 1. Installation

Run the following commands in your terminal:

    pipenv install -d
    docker-compose up
    
## 2. Run

In a new terminal window, run the producer with python:

    pipenv shell
    python src/producer.py localhost:9092 http://stream.meetup.com/2/rsvps
    
In another terminal window run:
    
    pipenv shell
    python src/consumer.py
    

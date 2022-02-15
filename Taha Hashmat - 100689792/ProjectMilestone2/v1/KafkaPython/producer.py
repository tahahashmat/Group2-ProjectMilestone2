from kafka import KafkaProducer

TOPIC_NAME = ''
KAFKA_SERVER = "localhost:9093"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Test Message!!')
producer.flush()
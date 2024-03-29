import pika

connection_parameters = pika.ConnectionParameters(
  host="localhost",
  port=5672,
  credentials=pika.PlainCredentials(
    username='guest', password='guest'
  )
)

# Abrindo o canal de consumidor
channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
  exchange='data_exchange',
  routing_key="",
  body="algumaCoisa",
  properties=pika.BasicProperties(
    delivery_mode=2 # make message persistent
  )
)
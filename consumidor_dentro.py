import pika
from pika import PlainCredentials

class RabbitmqConsumer_in:
  def __init__(self, callback) -> None:
    self.__host = "localhost"
    self.__port = 5672
    self.__username = "guest"
    self.__password = "guest"
    self.__queue = "consumer_in"
    self.__callback = callback
    self.__channel = self.__create_channel()

  def __create_channel(self):
    connection_parameters = pika.ConnectionParameters(
      host=self.__host,
      port=self.__port,
      credentials=PlainCredentials(
        username=self.__username, password=self.__password
      )
    )

    # Abrindo o canal de consumidor
    channel = pika.BlockingConnection(connection_parameters).channel()
    channel.queue_declare(
      queue=self.__queue,
      durable=True,
    )
    # Fazendo um consumo basico
    channel.basic_consume(
      queue=self.__queue,
      auto_ack=True,
      on_message_callback=self.__callback
    )

    return channel
  
  def start(self):
    print(f'Listen RabbitMQ on Port 5672')
    self.__channel.start_consuming()

def minha_callback(ch, method, properties, body):
  print(body)

rabbitmq_consumer_in = RabbitmqConsumer_in(minha_callback)
rabbitmq_consumer_in.start()
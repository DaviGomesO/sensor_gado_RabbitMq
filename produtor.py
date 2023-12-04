import pika

class RabbitMqPublisher_out:
  def __init__(self) -> None:
    self.__host = "localhost"
    self.__port = 5672
    self.__username = "guest"
    self.__password = "guest"
    self.__exchange = "producer_out"
    self.__routing_key = "fora"
    self.__channel = self.__create_channel()

  def __create_channel(self):
    connection_parameters = pika.ConnectionParameters(
      host=self.__host,
      port=self.__port,
      credentials=pika.PlainCredentials(
        username=self.__username, password=self.__password
      )
    )

    # Abrindo o canal de consumidor
    channel = pika.BlockingConnection(connection_parameters).channel()
    return channel
  
  def send_message(self, body):
    self.__channel.basic_publish(
      exchange=self.__exchange,
      routing_key=self.__routing_key,
      body=body,
      properties=pika.BasicProperties(
        delivery_mode=2 # make message persistent
      )
    )

class RabbitMqPublisher_in:
  def __init__(self) -> None:
    self.__host = "localhost"
    self.__port = 5672
    self.__username = "guest"
    self.__password = "guest"
    self.__exchange = "producer_in"
    self.__routing_key = "dentro"
    self.__channel = self.__create_channel()

  def __create_channel(self):
    connection_parameters = pika.ConnectionParameters(
      host=self.__host,
      port=self.__port,
      credentials=pika.PlainCredentials(
        username=self.__username, password=self.__password
      )
    )

    # Abrindo o canal de consumidor
    channel = pika.BlockingConnection(connection_parameters).channel()
    return channel
  
  def send_message(self,body):
    self.__channel.basic_publish(
      exchange=self.__exchange,
      routing_key=self.__routing_key,
      body=body,
      properties=pika.BasicProperties(
        delivery_mode=2 # make message persistent
      )
    )

# rabbitmq_publisher_dentro = RabbitMqPublisher_in()
# rabbitmq_publisher_dentro.send_message()

# rabbitmq_publisher_fora = RabbitMqPublisher_out()
# rabbitmq_publisher_fora.send_message()